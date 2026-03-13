---
title: Checking a graph for acyclicity and finding a cycle in O(M)
tags: 
weight: 10
---
# $O(M)$-এ গ্রাফে অ্যাসাইক্লিসিটি পরীক্ষা করা এবং সাইকেল খুঁজে বের করা

লুপ ও মাল্টিপল এজবিহীন একটি ডিরেক্টেড বা আনডিরেক্টেড গ্রাফ কনসিডার করো। আমাদের পরীক্ষা করতে হবে এটি অ্যাসাইক্লিক কি না, এবং না হলে যেকোনো একটি সাইকেল খুঁজে বের করতে হবে।

আমরা [DFS](depth-first-search.md) ব্যবহার করে $O(M)$-এ এই সমস্যাটি সমাধান করতে পারি, যেখানে $M$ হল এজের সংখ্যা।

## অ্যালগরিদম

আমরা গ্রাফে DFS-এর একটি সিরিজ চালাব। শুরুতে সমস্ত ভার্টেক্স সাদা (০) রঙের। প্রতিটি ভিজিট না করা (সাদা) ভার্টেক্স থেকে DFS শুরু করি, প্রবেশের সময় ধূসর (১) চিহ্নিত করি এবং প্রস্থানের সময় কালো (২) চিহ্নিত করি। DFS যদি একটি ধূসর ভার্টেক্সে যায়, তাহলে আমরা একটি সাইকেল পেয়েছি (গ্রাফ আনডিরেক্টেড হলে, প্যারেন্টের দিকে যাওয়া এজটি কনসিডার করা হয় না)। সাইকেলটি প্যারেন্ট অ্যারে ব্যবহার করে পুনর্গঠন করা যায়।

## ইমপ্লিমেন্টেশন

এখানে ডিরেক্টেড গ্রাফের জন্য একটি ইমপ্লিমেন্টেশন দেওয়া হল।

```cpp
int n;
vector<vector<int>> adj;
vector<char> color;
vector<int> parent;
int cycle_start, cycle_end;

bool dfs(int v) {
    color[v] = 1;
    for (int u : adj[v]) {
        if (color[u] == 0) {
            parent[u] = v;
            if (dfs(u))
                return true;
        } else if (color[u] == 1) {
            cycle_end = v;
            cycle_start = u;
            return true;
        }
    }
    color[v] = 2;
    return false;
}

void find_cycle() {
    color.assign(n, 0);
    parent.assign(n, -1);
    cycle_start = -1;

    for (int v = 0; v < n; v++) {
        if (color[v] == 0 && dfs(v))
            break;
    }

    if (cycle_start == -1) {
        cout << "Acyclic" << endl;
    } else {
        vector<int> cycle;
        cycle.push_back(cycle_start);
        for (int v = cycle_end; v != cycle_start; v = parent[v])
            cycle.push_back(v);
        cycle.push_back(cycle_start);
        reverse(cycle.begin(), cycle.end());

        cout << "Cycle found: ";
        for (int v : cycle)
            cout << v << " ";
        cout << endl;
    }
}
```

এখানে আনডিরেক্টেড গ্রাফের জন্য একটি ইমপ্লিমেন্টেশন দেওয়া হল। লক্ষ্য কর যে আনডিরেক্টেড ভার্সনে, যদি একটি ভার্টেক্স `v` কালো রঙ করা হয়, তাহলে DFS আর কখনো সেটা ভিজিট করবে না। কারণ আমরা `v`-কে প্রথম ভিজিট করার সময়ই `v`-এর সমস্ত কানেক্টেড এজ অন্বেষণ করেছি। `v` ধারণকারী কানেক্টেড কম্পোনেন্ট (`v` এবং তার প্যারেন্টের মধ্যের এজ সরানোর পরে) অবশ্যই একটি ট্রি হবে, যদি DFS `v`-কে প্রসেস করার সময় কোনো সাইকেল না পায়। তাই আমাদের ধূসর এবং কালো অবস্থার মধ্যে পার্থক্য করারও দরকার নেই। এভাবে আমরা char ভেক্টর `color`-কে boolean ভেক্টর `visited`-এ রূপান্তর করতে পারি।

```cpp
int n;
vector<vector<int>> adj;
vector<bool> visited;
vector<int> parent;
int cycle_start, cycle_end;

bool dfs(int v, int par) { // passing vertex and its parent vertex
    visited[v] = true;
    for (int u : adj[v]) {
        if(u == par) continue; // skipping edge to parent vertex
        if (visited[u]) {
            cycle_end = v;
            cycle_start = u;
            return true;
        }
        parent[u] = v;
        if (dfs(u, parent[u]))
            return true;
    }
    return false;
}

void find_cycle() {
    visited.assign(n, false);
    parent.assign(n, -1);
    cycle_start = -1;

    for (int v = 0; v < n; v++) {
        if (!visited[v] && dfs(v, parent[v]))
            break;
    }

    if (cycle_start == -1) {
        cout << "Acyclic" << endl;
    } else {
        vector<int> cycle;
        cycle.push_back(cycle_start);
        for (int v = cycle_end; v != cycle_start; v = parent[v])
            cycle.push_back(v);
        cycle.push_back(cycle_start);

        cout << "Cycle found: ";
        for (int v : cycle)
            cout << v << " ";
        cout << endl;
    }
}
```
### অনুশীলন সমস্যা:

- [AtCoder : Reachability in Functional Graph](https://atcoder.jp/contests/abc357/tasks/abc357_e)
- [CSES : Round Trip](https://cses.fi/problemset/task/1669)
- [CSES : Round Trip II](https://cses.fi/problemset/task/1678/)
