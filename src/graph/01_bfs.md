---
tags:
  - Original
---

# ০-১ বিএফএস

এটি সুপরিচিত যে, একটি **ওয়েটবিহীন গ্রাফে** [ব্রেডথ ফার্স্ট সার্চ](breadth-first-search.md) ব্যবহার করে $O(|E|)$ সময়ে একটি একক সোর্স থেকে অন্য সকল ভার্টেক্সে শর্টেস্ট পাথ বের করা যায়, অর্থাৎ সোর্স থেকে অন্য একটি ভার্টেক্সে যেতে ন্যূনতম কতগুলো এজ অতিক্রম করতে হবে তা বের করা যায়।
আমরা এই ধরনের গ্রাফকে একটি ওয়েটেড গ্রাফ হিসেবেও ব্যাখ্যা করতে পারি, যেখানে প্রতিটি এজের ওয়েট $1$।
যদি গ্রাফের সকল এজের ওয়েট একই না হয়, তাহলে আমাদের আরও সাধারণ অ্যালগরিদম দরকার, যেমন [ডায়াক্সট্রা](dijkstra.md) যা $O(|V|^2 + |E|)$ বা $O(|E| \log |V|)$ সময়ে চলে।

তবে ওয়েটগুলো যদি আরও সীমাবদ্ধ হয়, আমরা প্রায়ই আরও ভালো করতে পারি।
এই নিবন্ধে আমরা দেখাব কীভাবে বিএফএস ব্যবহার করে SSSP (সিঙ্গেল-সোর্স শর্টেস্ট পাথ) সমস্যা $O(|E|)$-এ সমাধান করা যায়, যদি প্রতিটি এজের ওয়েট $0$ বা $1$ হয়।

## অ্যালগরিদম

আমরা ডায়াক্সট্রার অ্যালগরিদম ঘনিষ্ঠভাবে পর্যালোচনা করে এবং আমাদের বিশেষ গ্রাফের প্রভাব সম্পর্কে চিন্তা করে এই অ্যালগরিদম তৈরি করতে পারি।
ডায়াক্সট্রার অ্যালগরিদমের সাধারণ রূপ হলো (এখানে প্রায়োরিটি কিউ হিসেবে একটি `set` ব্যবহৃত হয়েছে):

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

আমরা লক্ষ্য করতে পারি যে কিউতে থাকা সোর্স `s` থেকে দুটি ভিন্ন ভার্টেক্সের দূরত্বের পার্থক্য সর্বাধিক এক।
বিশেষত, আমরা জানি প্রতিটি $u \in Q$-এর জন্য $d[v] \le d[u] \le d[v] + 1$।
এর কারণ হলো, প্রতিটি ইটারেশনে আমরা কিউতে শুধু সমান দূরত্ব বা দূরত্ব যোগ এক সহ ভার্টেক্স যোগ করি।
ধরুন কিউতে এমন একটি $u$ আছে যেখানে $d[u] - d[v] > 1$, তাহলে $u$-কে অবশ্যই ভিন্ন কোনো ভার্টেক্স $t$ দিয়ে কিউতে ঢোকানো হয়েছে যেখানে $d[t] \ge d[u] - 1 > d[v]$।
কিন্তু এটি অসম্ভব, কারণ ডায়াক্সট্রার অ্যালগরিদম ভার্টেক্সগুলো ক্রমবর্ধমান ক্রমে ইটারেট করে।

এর মানে, কিউর ক্রমটি এরকম দেখায়:

$$Q = \underbrace{v}_{d[v]}, \dots, \underbrace{u}_{d[v]}, \underbrace{m}_{d[v]+1} \dots \underbrace{n}_{d[v]+1}$$

এই কাঠামো এতটাই সরল যে আমাদের প্রকৃত প্রায়োরিটি কিউ দরকার নেই, অর্থাৎ একটি ব্যালেন্সড বাইনারি ট্রি ব্যবহার করা অতিরিক্ত হবে।
আমরা সহজভাবে একটি সাধারণ কিউ ব্যবহার করতে পারি, এবং সংশ্লিষ্ট এজের ওয়েট $0$ হলে নতুন ভার্টেক্স শুরুতে যোগ করব, অর্থাৎ $d[u] = d[v]$ হলে, অথবা এজের ওয়েট $1$ হলে শেষে যোগ করব, অর্থাৎ $d[u] = d[v] + 1$ হলে।
এভাবে কিউ সর্বদা সাজানো থাকবে।

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

এজের ওয়েট আরও বড় হলেও আমরা এটিকে আরও সম্প্রসারিত করতে পারি।
যদি গ্রাফের প্রতিটি এজের ওয়েট $\le k$ হয়, তাহলে কিউতে থাকা ভার্টেক্সগুলোর দূরত্ব সোর্স থেকে $v$-এর দূরত্ব থেকে সর্বাধিক $k$ পার্থক্য করবে।
তাই আমরা কিউতে থাকা ভার্টেক্সগুলোর জন্য $k + 1$ টি বাকেট রাখতে পারি, এবং যখনই সবচেয়ে ছোট দূরত্বের বাকেট খালি হয়ে যায়, পরবর্তী বড় দূরত্বের বাকেট পেতে একটি চক্রাকার শিফট করি।
এই সম্প্রসারণকে **ডায়ালের অ্যালগরিদম** বলা হয়।

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
