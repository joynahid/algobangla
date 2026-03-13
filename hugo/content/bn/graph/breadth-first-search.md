---
title: "Breadth First Search (BFS)"
tags: 
weight: 10
---
# Breadth First Search (BFS)

Breadth First Search (BFS) হলো গ্রাফে সার্চ করার সবচেয়ে বেসিক আর গুরুত্বপূর্ণ অ্যালগরিদমগুলোর একটা।

BFS যেভাবে কাজ করে, তাতে যেকোনো নোডে পৌঁছানোর পাথটা সবসময় শর্টেস্ট পাথ হয়। তারমানে আনওয়েটেড গ্রাফে সবচেয়ে কম এজ দিয়ে যে পাথ পাওয়া যায়, সেটাই পাবে।

এই অ্যালগরিদম $O(n + m)$ সময়ে কাজ করে, যেখানে $n$ হলো ভার্টেক্সের সংখ্যা আর $m$ হলো এজের সংখ্যা।

## অ্যালগরিদম

এই অ্যালগরিদম ইনপুট নেয় একটা আনওয়েটেড গ্রাফ আর একটা সোর্স ভার্টেক্স $s$। গ্রাফটা ডিরেক্টেড হোক বা আনডিরেক্টেড, কোনো ফারাক নেই।

অ্যালগরিদমটা গ্রাফে আগুন ছড়িয়ে পড়ার মতো করে ভাবতে পারো। শুরুতে শুধু সোর্স $s$-এ আগুন জ্বলছে। প্রতিটা ধাপে, যে ভার্টেক্সগুলোতে আগুন জ্বলছে সেগুলো থেকে আগুন তাদের সব প্রতিবেশীতে ছড়িয়ে পড়ে। প্রতি ইটারেশনে "আগুনের বলয়" এক ধাপ করে বাড়ে — এজন্যই অ্যালগরিদমটার এই নাম।

সোজা কথায়, অ্যালগরিদমটা এভাবে কাজ করে: একটা কিউ $q$ বানাও — এখানে ভার্টেক্সগুলো প্রসেসের জন্য অপেক্ষা করবে। আর একটা বুলিয়ান অ্যারে $used[]$ রাখো — কোন ভার্টেক্স ভিজিট হয়েছে সেটা ট্র্যাক করার জন্য।

প্রথমে সোর্স $s$-কে কিউতে পুশ করো আর $used[s] = true$ সেট করো। বাকি সব ভার্টেক্স $v$-এর জন্য $used[v] = false$ রাখো। এরপর কিউ খালি না হওয়া পর্যন্ত লুপ চালাও। প্রতি ইটারেশনে কিউয়ের সামনে থেকে একটা ভার্টেক্স পপ করো। এই ভার্টেক্স থেকে যত এজ বের হচ্ছে সেগুলো দেখো — যদি কোনো এজ এমন ভার্টেক্সে যায় যেটা এখনো ভিজিট হয়নি, তাহলে সেটাতে আগুন ধরিয়ে দাও আর কিউতে রাখো।

তাহলে কিউ খালি হয়ে গেলে, সোর্স $s$ থেকে যত ভার্টেক্সে পৌঁছানো সম্ভব সবগুলোতে আগুন পৌঁছে গেছে, আর প্রতিটাতে সবচেয়ে ছোট পাথ দিয়ে পৌঁছানো হয়েছে।
তুমি শর্টেস্ট পাথের দৈর্ঘ্যও বের করতে পারবে — শুধু একটা অ্যারে $d[]$ রাখো পাথের দৈর্ঘ্য স্টোর করার জন্য। আর পুরো পাথটা রিকভার করতে চাইলে আরেকটা অ্যারে $p[]$ রাখো যেটাতে প্রতি ভার্টেক্সের "প্যারেন্ট" থাকবে, মানে যে ভার্টেক্স থেকে এখানে এসেছো সেটা।

## ইমপ্লিমেন্টেশন

উপরের অ্যালগরিদমটা C++ আর Java-তে লিখলে এরকম দেখাবে:


**C++**

```cpp
vector<vector<int>> adj;  // adjacency list representation
int n; // number of nodes
int s; // source vertex

queue<int> q;
vector<bool> used(n);
vector<int> d(n), p(n);

q.push(s);
used[s] = true;
p[s] = -1;
while (!q.empty()) {
    int v = q.front();
    q.pop();
    for (int u : adj[v]) {
        if (!used[u]) {
            used[u] = true;
            q.push(u);
            d[u] = d[v] + 1;
            p[u] = v;
        }
    }
}
```

**Java**

```java
ArrayList<ArrayList<Integer>> adj = new ArrayList<>(); // adjacency list representation

int n; // number of nodes
int s; // source vertex


LinkedList<Integer> q = new LinkedList<Integer>();
boolean used[] = new boolean[n];
int d[] = new int[n];
int p[] = new int[n];

q.push(s);
used[s] = true;
p[s] = -1;
while (!q.isEmpty()) {
    int v = q.pop();
    for (int u : adj.get(v)) {
        if (!used[u]) {
            used[u] = true;
            q.push(u);
            d[u] = d[v] + 1;
            p[u] = v;
        }
    }
}
```

যদি সোর্স থেকে কোনো ভার্টেক্স $u$-তে শর্টেস্ট পাথটা বের করে প্রিন্ট করতে চাও, তাহলে এভাবে করতে পারো:


**C++**

```cpp
if (!used[u]) {
    cout << "No path!";
} else {
    vector<int> path;
    for (int v = u; v != -1; v = p[v])
        path.push_back(v);
    reverse(path.begin(), path.end());
    cout << "Path: ";
    for (int v : path)
        cout << v << " ";
}
```

**Java**

```java
if (!used[u]) {
    System.out.println("No path!");
} else {
    ArrayList<Integer> path = new ArrayList<Integer>();
    for (int v = u; v != -1; v = p[v])
        path.add(v);
    Collections.reverse(path);
    for(int v : path)
        System.out.println(v);
}
```

## BFS-এর অ্যাপ্লিকেশন

* আনওয়েটেড গ্রাফে একটা সোর্স থেকে বাকি সব ভার্টেক্সে শর্টেস্ট পাথ বের করা।

* $O(n + m)$ সময়ে একটা আনডিরেক্টেড গ্রাফের সব কানেক্টেড কম্পোনেন্ট বের করা:
এর জন্য প্রতিটা ভার্টেক্স থেকে BFS চালাও, তবে আগের রানে যেগুলো ভিজিট হয়ে গেছে সেগুলো বাদ দাও।
মূল ব্যাপার হলো প্রতিবার নতুন কম্পোনেন্ট পেলে $used[]$ অ্যারে রিসেট করো না, তাহলে মোট রানিং টাইম $O(n + m)$ থাকবে। $used[]$ অ্যারে রিসেট না করে একাধিক BFS চালানোকে BFS-এর সিরিজ বলে।

* কোনো প্রবলেম বা গেমের মিনিমাম মুভে সলিউশন বের করা — যদি গেমের প্রতিটা স্টেটকে গ্রাফের ভার্টেক্স আর এক স্টেট থেকে আরেক স্টেটে যাওয়াকে এজ হিসেবে মডেল করা যায়।

* 0 বা 1 ওয়েটের গ্রাফে শর্টেস্ট পাথ বের করা:
এর জন্য স্বাভাবিক BFS-এ একটু চেঞ্জ করতে হবে। $used[]$ অ্যারে রাখার বদলে চেক করো ভার্টেক্সের দূরত্ব আগে পাওয়া দূরত্বের চেয়ে কম কি না। এজের ওয়েট 0 হলে কিউয়ের সামনে পুশ করো, আর 1 হলে পেছনে পুশ করো। এটা নিয়ে [0-1 BFS](01_bfs.md) আর্টিকেলে বিস্তারিত আছে।

* ডিরেক্টেড আনওয়েটেড গ্রাফে শর্টেস্ট সাইকেল বের করা:
প্রতিটা ভার্টেক্স থেকে BFS শুরু করো।
যখনই বর্তমান ভার্টেক্স থেকে সোর্সে ফিরে যেতে পারবে, তখনই সেই সোর্সকে ধারণ করা শর্টেস্ট সাইকেল পেয়ে গেছো।
এই পয়েন্টে BFS থামাও আর পরের ভার্টেক্স থেকে নতুন BFS শুরু করো।
সব সাইকেলের মধ্যে (প্রতিটা BFS থেকে বড়জোর একটা) সবচেয়ে ছোটটা নাও।

* ভার্টেক্স জোড়া $(a, b)$-এর মধ্যে যেকোনো শর্টেস্ট পাথে থাকা সব এজ বের করা:
এর জন্য দুইটা BFS চালাও — একটা $a$ থেকে, আরেকটা $b$ থেকে।
ধরো $d_a []$ হলো $a$ থেকে BFS করে পাওয়া শর্টেস্ট দূরত্বের অ্যারে, আর $d_b []$ হলো $b$ থেকে পাওয়া।
এখন প্রতিটা এজ $(u, v)$-এর জন্য চেক করো সেটা $a$ আর $b$-এর কোনো শর্টেস্ট পাথে আছে কি না।
শর্ত হলো $d_a [u] + 1 + d_b [v] = d_a [b]$।

* ভার্টেক্স জোড়া $(a, b)$-এর মধ্যে যেকোনো শর্টেস্ট পাথে থাকা সব ভার্টেক্স বের করা:
এটার জন্যও দুইটা BFS চালাও — একটা $a$ থেকে, আরেকটা $b$ থেকে।
ধরো $d_a []$ হলো $a$ থেকে BFS করে পাওয়া শর্টেস্ট দূরত্বের অ্যারে, আর $d_b []$ হলো $b$ থেকে পাওয়া।
এখন প্রতিটা ভার্টেক্স $v$-এর জন্য চেক করো সেটা $a$ আর $b$-এর কোনো শর্টেস্ট পাথে আছে কি না।
শর্ত হলো $d_a [v] + d_b [v] = d_a [b]$।

* আনওয়েটেড গ্রাফে সোর্স $s$ থেকে টার্গেট $t$-এ জোড় দৈর্ঘ্যের শর্টেস্ট ওয়াক বের করা:
এর জন্য একটা সহায়ক গ্রাফ বানাতে হবে যেখানে ভার্টেক্সগুলো হলো স্টেট $(v, c)$ — $v$ হলো বর্তমান নোড, আর $c = 0$ বা $c = 1$ হলো বর্তমান প্যারিটি।
মূল গ্রাফের যেকোনো এজ $(u, v)$ এই নতুন গ্রাফে দুইটা এজ হবে: $((u, 0), (v, 1))$ আর $((u, 1), (v, 0))$।
এরপর $(s, 0)$ থেকে $(t, 0)$-এ শর্টেস্ট ওয়াক বের করতে BFS চালাও।<br>**লক্ষ্য কর:** এখানে "_পাথ_"-এর বদলে "_ওয়াক_" বলা হচ্ছে, কারণ জোড় দৈর্ঘ্য পেতে গেলে ওয়াকে ভার্টেক্স রিপিট হতে পারে। জোড় দৈর্ঘ্যের শর্টেস্ট _পাথ_ বের করা ডিরেক্টেড গ্রাফে NP-Complete, আর আনডিরেক্টেড গ্রাফে [লিনিয়ার টাইমে সমাধান করা যায়](https://onlinelibrary.wiley.com/doi/abs/10.1002/net.3230140403), তবে অনেক বেশি জটিল পদ্ধতিতে।

## প্র্যাকটিস প্রবলেম

* [SPOJ: AKBAR](http://spoj.com/problems/AKBAR)
* [SPOJ: NAKANJ](http://www.spoj.com/problems/NAKANJ/)
* [SPOJ: WATER](http://www.spoj.com/problems/WATER)
* [SPOJ: MICE AND MAZE](http://www.spoj.com/problems/MICEMAZE/)
* [Timus: Caravans](http://acm.timus.ru/problem.aspx?space=1&num=2034)
* [DevSkill - Holloween Party (archived)](http://web.archive.org/web/20200930162803/http://www.devskill.com/CodingProblems/ViewProblem/60)
* [DevSkill - Ohani And The Link Cut Tree (archived)](http://web.archive.org/web/20170216192002/http://devskill.com:80/CodingProblems/ViewProblem/150)
* [SPOJ - Spiky Mazes](http://www.spoj.com/problems/SPIKES/)
* [SPOJ - Four Chips (hard)](http://www.spoj.com/problems/ADV04F1/)
* [SPOJ - Inversion Sort](http://www.spoj.com/problems/INVESORT/)
* [Codeforces - Shortest Path](http://codeforces.com/contest/59/problem/E)
* [SPOJ - Yet Another Multiple Problem](http://www.spoj.com/problems/MULTII/)
* [UVA 11392 - Binary 3xType Multiple](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2387)
* [UVA 10968 - KuPellaKeS](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1909)
* [Codeforces - Police Stations](http://codeforces.com/contest/796/problem/D)
* [Codeforces - Okabe and City](http://codeforces.com/contest/821/problem/D)
* [SPOJ - Find the Treasure](http://www.spoj.com/problems/DIGOKEYS/)
* [Codeforces - Bear and Forgotten Tree 2](http://codeforces.com/contest/653/problem/E)
* [Codeforces - Cycle in Maze](http://codeforces.com/contest/769/problem/C)
* [UVA - 11312 - Flipping Frustration](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2287)
* [SPOJ - Ada and Cycle](http://www.spoj.com/problems/ADACYCLE/)
* [CSES - Labyrinth](https://cses.fi/problemset/task/1193)
* [CSES - Message Route](https://cses.fi/problemset/task/1667/)
* [CSES - Monsters](https://cses.fi/problemset/task/1194)
