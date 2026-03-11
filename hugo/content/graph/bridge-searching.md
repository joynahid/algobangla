---
title: $O(N+M)$ এ গ্রাফে ব্রিজ খোঁজা
tags: 
weight: 20
---
# $O(N+M)$ এ গ্রাফে ব্রিজ খোঁজা

আমাদের একটি অনির্দেশিত গ্রাফ দেওয়া আছে। একটি ব্রিজ হলো এমন একটি এজ যেটি সরিয়ে দিলে গ্রাফ বিচ্ছিন্ন হয়ে যায় (বা আরও সুনির্দিষ্টভাবে, গ্রাফে কানেক্টেড কম্পোনেন্টের সংখ্যা বাড়ে)। কাজ হলো দেওয়া গ্রাফে সমস্ত ব্রিজ খুঁজে বের করা।

অনানুষ্ঠানিকভাবে, সমস্যাটি এভাবে তৈরি করা হয়: রাস্তা দিয়ে সংযুক্ত শহরগুলোর একটি মানচিত্র দেওয়া আছে, সমস্ত "গুরুত্বপূর্ণ" রাস্তা খুঁজে বের করুন, অর্থাৎ এমন রাস্তা যেগুলো সরিয়ে দিলে কিছু শহরের জোড়ার মধ্যে পাথ বিলুপ্ত হয়ে যায়।

এখানে বর্ণিত অ্যালগরিদমটি [ডেপথ-ফার্স্ট সার্চ](depth-first-search.md) এর উপর ভিত্তি করে এবং এর কমপ্লেক্সিটি $O(N+M)$, যেখানে $N$ হলো ভার্টেক্সের সংখ্যা এবং $M$ হলো গ্রাফে এজের সংখ্যা।

লক্ষ্য করুন যে [অনলাইনে ব্রিজ খোঁজা](bridge-searching-online.md) নিবন্ধটিও আছে - এখানে বর্ণিত অফলাইন অ্যালগরিদমের বিপরীতে, অনলাইন অ্যালগরিদম একটি পরিবর্তনশীল গ্রাফে সমস্ত ব্রিজের তালিকা বজায় রাখতে সক্ষম (ধরে নিচ্ছি যে একমাত্র পরিবর্তন হলো নতুন এজ যোগ করা)।

## অ্যালগরিদম

গ্রাফের একটি ইচ্ছামতো ভার্টেক্স $root$ নিন এবং সেখান থেকে [ডেপথ-ফার্স্ট সার্চ](depth-first-search.md) চালান। নিম্নলিখিত তথ্যটি লক্ষ্য করুন (যা প্রমাণ করা সহজ):

- ধরা যাক আমরা DFS-এ আছি, ভার্টেক্স $v$ থেকে শুরু করে এজগুলো দেখছি। বর্তমান এজ $(v, to)$ একটি ব্রিজ হবে যদি এবং কেবল যদি ভার্টেক্স $to$ এবং DFS ট্রাভার্সাল ট্রি-তে এর কোনো বংশধরের ভার্টেক্স $v$ বা এর কোনো পূর্বসূরিতে কোনো ব্যাক-এজ না থাকে। প্রকৃতপক্ষে, এই শর্তের মানে হলো এজ $(v, to)$ ছাড়া $v$ থেকে $to$ যাওয়ার অন্য কোনো পথ নেই।

এখন আমাদের প্রতিটি ভার্টেক্সের জন্য এই তথ্যটি দক্ষতার সাথে পরীক্ষা করা শিখতে হবে। আমরা ডেপথ-ফার্স্ট সার্চ দ্বারা গণিত "নোডে প্রবেশের সময়" ব্যবহার করব।

তাই, $\mathtt{tin}[v]$ দিয়ে নোড $v$ এর প্রবেশ সময় বোঝাই। আমরা একটি অ্যারে $\mathtt{low}$ প্রবর্তন করি যেটি আমাদের DFS সার্চে পাওয়া সর্বনিম্ন প্রবেশ সময় সংরক্ষণ করতে দেবে যা একটি নোড $v$ তার নিজের বা তার বংশধরদের কাছ থেকে একটি একক এজ দিয়ে পৌঁছাতে পারে। $\mathtt{low}[v]$ হলো $\mathtt{tin}[v]$, ব্যাক-এজ $(v, p)$ দ্বারা নোড $v$ এর সাথে সংযুক্ত প্রতিটি নোড $p$ এর প্রবেশ সময় $\mathtt{tin}[p]$ এবং DFS ট্রি-তে $v$ এর প্রত্যক্ষ বংশধর প্রতিটি ভার্টেক্স $to$ এর $\mathtt{low}[to]$ মানের মধ্যে সর্বনিম্ন:

$$\mathtt{low}[v] = \min \left\{
    \begin{array}{l}
    \mathtt{tin}[v] \\
    \mathtt{tin}[p]  &\text{ for all }p\text{ for which }(v, p)\text{ is a back edge} \\
    \mathtt{low}[to] &\text{ for all }to\text{ for which }(v, to)\text{ is a tree edge}
    \end{array}
\right\}$$

এখন, ভার্টেক্স $v$ বা এর কোনো বংশধর থেকে এর কোনো পূর্বসূরিতে একটি ব্যাক এজ আছে যদি এবং কেবল যদি ভার্টেক্স $v$ এর একটি চাইল্ড $to$ থাকে যার জন্য $\mathtt{low}[to] \leq \mathtt{tin}[v]$। যদি $\mathtt{low}[to] = \mathtt{tin}[v]$ হয়, তাহলে ব্যাক এজ সরাসরি $v$ তে আসে, অন্যথায় এটি $v$ এর কোনো পূর্বসূরিতে আসে।

অতএব, DFS ট্রি-তে বর্তমান এজ $(v, to)$ একটি ব্রিজ হবে যদি এবং কেবল যদি $\mathtt{low}[to] > \mathtt{tin}[v]$।

## ইমপ্লিমেন্টেশন

ইমপ্লিমেন্টেশনে তিনটি ক্ষেত্র আলাদা করা প্রয়োজন: যখন আমরা DFS ট্রি-তে এজ বরাবর নিচে যাই, যখন আমরা ভার্টেক্সের পূর্বসূরিতে একটি ব্যাক এজ খুঁজে পাই এবং যখন আমরা ভার্টেক্সের প্যারেন্টে ফিরে আসি। এই ক্ষেত্রগুলো হলো:

- $\mathtt{visited}[to] = false$ - এজটি DFS ট্রি-র অংশ;
- $\mathtt{visited}[to] = true$ && $to \neq parent$ - এজটি কোনো পূর্বসূরিতে ব্যাক এজ;
- $to = parent$ - এজটি DFS ট্রি-তে প্যারেন্টে ফিরে যায়।

এটি ইমপ্লিমেন্ট করতে, আমাদের একটি ডেপথ-ফার্স্ট সার্চ ফাংশন দরকার যেটি বর্তমান নোডের প্যারেন্ট ভার্টেক্স গ্রহণ করে।

মাল্টিপল এজের ক্ষেত্রে, প্যারেন্ট থেকে আসা এজ উপেক্ষা করার সময় আমাদের সতর্ক থাকতে হবে। এই সমস্যা সমাধানের জন্য, আমরা একটি `parent_skipped` ফ্ল্যাগ যোগ করতে পারি যেটি নিশ্চিত করবে যে আমরা প্যারেন্টকে শুধুমাত্র একবার স্কিপ করি।

```cpp
void IS_BRIDGE(int v,int to); // some function to process the found bridge
int n; // number of nodes
vector<vector<int>> adj; // adjacency list of graph

vector<bool> visited;
vector<int> tin, low;
int timer;

void dfs(int v, int p = -1) {
    visited[v] = true;
    tin[v] = low[v] = timer++;
    bool parent_skipped = false;
    for (int to : adj[v]) {
        if (to == p && !parent_skipped) {
            parent_skipped = true;
            continue;
        }
        if (visited[to]) {
            low[v] = min(low[v], tin[to]);
        } else {
            dfs(to, v);
            low[v] = min(low[v], low[to]);
            if (low[to] > tin[v])
                IS_BRIDGE(v, to);
        }
    }
}

void find_bridges() {
    timer = 0;
    visited.assign(n, false);
    tin.assign(n, -1);
    low.assign(n, -1);
    for (int i = 0; i < n; ++i) {
        if (!visited[i])
            dfs(i);
    }
}
```

মূল ফাংশন হলো `find_bridges`; এটি প্রয়োজনীয় ইনিশিয়ালাইজেশন সম্পাদন করে এবং গ্রাফের প্রতিটি কানেক্টেড কম্পোনেন্টে ডেপথ-ফার্স্ট সার্চ শুরু করে।

`IS_BRIDGE(a, b)` ফাংশন হলো একটি ফাংশন যেটি এজ $(a, b)$ ব্রিজ হওয়ার তথ্য প্রক্রিয়া করবে, উদাহরণস্বরূপ, এটি প্রিন্ট করবে।

লক্ষ্য করুন যে গ্রাফে মাল্টিপল এজ থাকলে এই ইমপ্লিমেন্টেশন সঠিকভাবে কাজ করে না, যেহেতু এটি সেগুলো উপেক্ষা করে। অবশ্যই, মাল্টিপল এজ কখনোই উত্তরের অংশ হবে না, তাই `IS_BRIDGE` অতিরিক্তভাবে পরীক্ষা করতে পারে যে রিপোর্ট করা ব্রিজটি একটি মাল্টিপল এজ নয়। বিকল্পভাবে, প্যারেন্ট ভার্টেক্সের পরিবর্তে ভার্টেক্সে প্রবেশ করতে ব্যবহৃত এজের ইনডেক্স `dfs` তে পাস করা সম্ভব (এবং সমস্ত ভার্টেক্সের ইনডেক্স সংরক্ষণ করা)।

## অনুশীলন সমস্যা

- [UVA #796 "Critical Links"](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=737) [difficulty: low]
- [UVA #610 "Street Directions"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=551) [difficulty: medium]
- [Case of the Computer Network (Codeforces Round #310 Div. 1 E)](http://codeforces.com/problemset/problem/555/E) [difficulty: hard]
* [UVA 12363 - Hedge Mazes](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3785)
* [UVA 315 - Network](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=251)
* [GYM - Computer Network (J)](http://codeforces.com/gym/100114)
* [SPOJ - King Graffs Defense](http://www.spoj.com/problems/GRAFFDEF/)
* [SPOJ - Critical Edges](http://www.spoj.com/problems/EC_P/)
* [Codeforces - Break Up](http://codeforces.com/contest/700/problem/C)
* [Codeforces - Tourist Reform](http://codeforces.com/contest/732/problem/F)
* [Codeforces - Non-academic problem](https://codeforces.com/contest/1986/problem/F)
