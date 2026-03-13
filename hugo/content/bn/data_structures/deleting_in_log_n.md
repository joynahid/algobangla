---
title: Deleting from a data structure in O(T(n) log n)
tags: 
weight: 10
---
# একটি ডাটা স্ট্রাকচার থেকে $O(T(n)\log n)$-এ মুছে ফেলা

ধরো তোমার কাছে এমন একটি ডাটা স্ট্রাকচার আছে যা **প্রকৃত** $O(T(n))$-এ উপাদান যোগ করতে পারে।
এই আর্টিকেলে এমন একটি কৌশল বর্ণনা করা হবে যা অফলাইনে $O(T(n)\log n)$-এ মুছে ফেলতে সক্ষম করে।

## অ্যালগরিদম

প্রতিটি উপাদান যোগ এবং মুছে ফেলার মধ্যবর্তী সময়ের কিছু সেগমেন্টে ডাটা স্ট্রাকচারে বেঁচে থাকে।
কুয়েরিগুলোর উপর একটি সেগমেন্ট ট্রি তৈরি করি।
কোনো উপাদান যতক্ষণ জীবিত থাকে সেই সেগমেন্টটি ট্রি-র $O(\log n)$ নোডে বিভক্ত হয়।
যখন আমরা স্ট্রাকচার সম্পর্কে কিছু জানতে চাই সেই কুয়েরিটি সংশ্লিষ্ট লিফে রাখি।
এখন সব কুয়েরি প্রক্রিয়া করতে আমরা সেগমেন্ট ট্রি-তে একটি DFS চালাব।
কোনো নোডে প্রবেশ করার সময় আমরা সেই নোডের ভেতরের সব উপাদান যোগ করব।
তারপর এই নোডের চাইল্ডে যাব অথবা কুয়েরির উত্তর দেব (যদি নোডটি একটি লিফ হয়)।
নোড থেকে বের হওয়ার সময়, আমাদের যোগ করাগুলো পূর্বাবস্থায় ফেরাতে হবে।
লক্ষ্য করো যে আমরা যদি $O(T(n))$-এ স্ট্রাকচার পরিবর্তন করি তাহলে পরিবর্তনের একটি স্ট্যাক রেখে $O(T(n))$-এ পরিবর্তনগুলো রোলব্যাক করতে পারি।
লক্ষ্য করো রোলব্যাক অ্যামোর্টাইজড কমপ্লেক্সিটি ভেঙে দেয়।

## নোট

কোনো কিছু জীবিত থাকার সেগমেন্টের উপর সেগমেন্ট ট্রি তৈরি করার ধারণাটি শুধু ডাটা স্ট্রাকচার সমস্যার জন্য নয়, অন্যত্রও ব্যবহার করা যায়।
নিচে কিছু সমস্যা দেখো।

## ইমপ্লিমেন্টেশন

এই ইমপ্লিমেন্টেশনটি [ডায়নামিক কানেক্টিভিটি](https://en.wikipedia.org/wiki/Dynamic_connectivity) সমস্যার জন্য।
এটাএজ যোগ করতে, এজ সরাতে এবং কানেক্টেড কম্পোনেন্টের সংখ্যা গুনতে পারে।

```cpp
struct dsu_save {
    int v, rnkv, u, rnku;

    dsu_save() {}

    dsu_save(int _v, int _rnkv, int _u, int _rnku)
        : v(_v), rnkv(_rnkv), u(_u), rnku(_rnku) {}
};

struct dsu_with_rollbacks {
    vector<int> p, rnk;
    int comps;
    stack<dsu_save> op;

    dsu_with_rollbacks() {}

    dsu_with_rollbacks(int n) {
        p.resize(n);
        rnk.resize(n);
        for (int i = 0; i < n; i++) {
            p[i] = i;
            rnk[i] = 0;
        }
        comps = n;
    }

    int find_set(int v) {
        return (v == p[v]) ? v : find_set(p[v]);
    }

    bool unite(int v, int u) {
        v = find_set(v);
        u = find_set(u);
        if (v == u)
            return false;
        comps--;
        if (rnk[v] > rnk[u])
            swap(v, u);
        op.push(dsu_save(v, rnk[v], u, rnk[u]));
        p[v] = u;
        if (rnk[u] == rnk[v])
            rnk[u]++;
        return true;
    }

    void rollback() {
        if (op.empty())
            return;
        dsu_save x = op.top();
        op.pop();
        comps++;
        p[x.v] = x.v;
        rnk[x.v] = x.rnkv;
        p[x.u] = x.u;
        rnk[x.u] = x.rnku;
    }
};

struct query {
    int v, u;
    bool united;
    query(int _v, int _u) : v(_v), u(_u) {
    }
};

struct QueryTree {
    vector<vector<query>> t;
    dsu_with_rollbacks dsu;
    int T;

    QueryTree() {}

    QueryTree(int _T, int n) : T(_T) {
        dsu = dsu_with_rollbacks(n);
        t.resize(4 * T + 4);
    }

    void add_to_tree(int v, int l, int r, int ul, int ur, query& q) {
        if (ul > ur)
            return;
        if (l == ul && r == ur) {
            t[v].push_back(q);
            return;
        }
        int mid = (l + r) / 2;
        add_to_tree(2 * v, l, mid, ul, min(ur, mid), q);
        add_to_tree(2 * v + 1, mid + 1, r, max(ul, mid + 1), ur, q);
    }

    void add_query(query q, int l, int r) {
        add_to_tree(1, 0, T - 1, l, r, q);
    }

    void dfs(int v, int l, int r, vector<int>& ans) {
        for (query& q : t[v]) {
            q.united = dsu.unite(q.v, q.u);
        }
        if (l == r)
            ans[l] = dsu.comps;
        else {
            int mid = (l + r) / 2;
            dfs(2 * v, l, mid, ans);
            dfs(2 * v + 1, mid + 1, r, ans);
        }
        for (query q : t[v]) {
            if (q.united)
                dsu.rollback();
        }
    }

    vector<int> solve() {
        vector<int> ans(T);
        dfs(1, 0, T - 1, ans);
        return ans;
    }
};
```

## সমস্যা

- [Codeforces - Connect and Disconnect](https://codeforces.com/gym/100551/problem/A)
- [Codeforces - Addition on Segments](https://codeforces.com/contest/981/problem/E)
- [Codeforces - Extending Set of Points](https://codeforces.com/contest/1140/problem/F)
