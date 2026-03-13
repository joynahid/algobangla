---
title: "০-১ বিএফএস"
tags: 
weight: 40
---
# ০-১ বিএফএস

এটা বেশ জানা কথা যে, একটা **ওয়েটবিহীন গ্রাফে** [BFS](breadth-first-search.md) দিয়ে $O(|E|)$ সময়ে একটা সোর্স থেকে বাকি সব ভার্টেক্সে শর্টেস্ট পাথ বের করা যায়। মানে সোর্স থেকে অন্য একটা ভার্টেক্সে যেতে কমপক্ষে কতগুলো এজ পার হতে হবে সেটা বের করা যায়।
এই ধরনের গ্রাফকে আমরা একটা ওয়েটেড গ্রাফ হিসেবেও ভাবতে পারি, যেখানে প্রতিটা এজের ওয়েট $1$।
যদি গ্রাফের সব এজের ওয়েট একই না হয়, তাহলে আমাদের আরও সাধারণ অ্যালগরিদম দরকার, যেমন [ডায়াক্সট্রা](dijkstra.md) যেটা $O(|V|^2 + |E|)$ বা $O(|E| \log |V|)$ সময়ে চলে।

তবে ওয়েটগুলো যদি আরও সীমাবদ্ধ হয়, আমরা প্রায়ই আরও ভালো করতে পারি।
এই আর্টিকেলে আমরা দেখব কীভাবে BFS দিয়ে SSSP (সিঙ্গেল-সোর্স শর্টেস্ট পাথ) সমস্যা $O(|E|)$-এ সমাধান করা যায়, যদি প্রতিটা এজের ওয়েট $0$ বা $1$ হয়।

## অ্যালগরিদম

ডায়াক্সট্রার অ্যালগরিদম ভালো করে দেখলে এবং আমাদের বিশেষ গ্রাফের প্রভাব নিয়ে চিন্তা করলে আমরা এই অ্যালগরিদম বানাতে পারি।
ডায়াক্সট্রার অ্যালগরিদমের সাধারণ রূপটা এরকম (এখানে প্রায়োরিটি কিউ হিসেবে একটা `set` ব্যবহার করা হয়েছে):

```cpp
d.assign(n, INF);
d[s] = 0;
set<pair<int, int>> q;
q.insert({0, s});
while (!q.empty()) {
    int v = q.begin()->second;
    q.erase(q.begin());

    for (auto edge : adj[v]) {
        int u = edge.first;
        int w = edge.second;

        if (d[v] + w < d[u]) {
            q.erase({d[u], u});
            d[u] = d[v] + w;
            q.insert({d[u], u});
        }
    }
}
```

লক্ষ্য করো, কিউতে থাকা সোর্স `s` থেকে দুটো ভিন্ন ভার্টেক্সের দূরত্বের পার্থক্য সর্বাধিক এক।
বিশেষ করে, আমরা জানি প্রতিটা $u \in Q$-এর জন্য $d[v] \le d[u] \le d[v] + 1$।
কারণটা হলো, প্রতিটা ইটারেশনে আমরা কিউতে শুধু সমান দূরত্ব বা দূরত্ব যোগ এক সহ ভার্টেক্স যোগ করি।
ধরো কিউতে এমন একটা $u$ আছে যেখানে $d[u] - d[v] > 1$, তাহলে $u$-কে অবশ্যই ভিন্ন কোনো ভার্টেক্স $t$ দিয়ে কিউতে ঢোকানো হয়েছে যেখানে $d[t] \ge d[u] - 1 > d[v]$।
কিন্তু এটা অসম্ভব, কারণ ডায়াক্সট্রার অ্যালগরিদম ভার্টেক্সগুলো ক্রমবর্ধমান ক্রমে ইটারেট করে।

তারমানে, কিউর ক্রমটা এরকম দেখায়:

$$Q = \underbrace{v}_{d[v]}, \dots, \underbrace{u}_{d[v]}, \underbrace{m}_{d[v]+1} \dots \underbrace{n}_{d[v]+1}$$

এই স্ট্রাকচারটা এতটাই সিম্পল যে আমাদের আসল প্রায়োরিটি কিউ দরকার নেই। মানে একটা ব্যালেন্সড বাইনারি ট্রি ব্যবহার করা ওভারকিল হবে।
আমরা সিম্পলি একটা সাধারণ কিউ ব্যবহার করতে পারি। সংশ্লিষ্ট এজের ওয়েট $0$ হলে নতুন ভার্টেক্স শুরুতে যোগ করব (মানে $d[u] = d[v]$ হলে), আর এজের ওয়েট $1$ হলে শেষে যোগ করব (মানে $d[u] = d[v] + 1$ হলে)।
এভাবে কিউ সবসময় সাজানো থাকবে।

```cpp
vector<int> d(n, INF);
d[s] = 0;
deque<int> q;
q.push_front(s);
while (!q.empty()) {
    int v = q.front();
    q.pop_front();
    for (auto edge : adj[v]) {
        int u = edge.first;
        int w = edge.second;
        if (d[v] + w < d[u]) {
            d[u] = d[v] + w;
            if (w == 1)
                q.push_back(u);
            else
                q.push_front(u);
        }
    }
}
```

## ডায়ালের অ্যালগরিদম

এজের ওয়েট আরও বড় হলেও আমরা এটাকে আরও এক্সটেন্ড করতে পারি।
যদি গ্রাফের প্রতিটা এজের ওয়েট $\le k$ হয়, তাহলে কিউতে থাকা ভার্টেক্সগুলোর দূরত্ব সোর্স থেকে $v$-এর দূরত্ব থেকে সর্বাধিক $k$ পার্থক্য করবে।
তাই আমরা কিউতে থাকা ভার্টেক্সগুলোর জন্য $k + 1$ টা বাকেট রাখতে পারি, আর যখনই সবচেয়ে ছোট দূরত্বের বাকেট খালি হয়ে যায়, পরের বড় দূরত্বের বাকেট পেতে একটা চক্রাকার শিফট করি।
এই এক্সটেনশনকে **ডায়ালের অ্যালগরিদম** বলে।

## অনুশীলন সমস্যা

- [CodeChef - Chef and Reversing](https://www.codechef.com/problems/REVERSE)
- [Labyrinth](https://codeforces.com/contest/1063/problem/B)
- [KATHTHI](http://www.spoj.com/problems/KATHTHI/)
- [DoNotTurn](https://community.topcoder.com/stat?c=problem_statement&pm=10337)
- [Ocean Currents](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2620)
- [Olya and Energy Drinks](https://codeforces.com/problemset/problem/877/D)
- [Three States](https://codeforces.com/problemset/problem/590/C)
- [Colliding Traffic](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2621)
- [CHamber of Secrets](https://codeforces.com/problemset/problem/173/B)
- [Spiral Maximum](https://codeforces.com/problemset/problem/173/C)
- [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid)
