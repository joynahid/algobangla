---
title: "২-স্যাট"
tags: 
weight: 40
---
# ২-স্যাট

SAT (বুলিয়ান স্যাটিসফায়াবিলিটি প্রবলেম) হলো একটা দেওয়া বুলিয়ান ফর্মুলা সিদ্ধ করার জন্য ভেরিয়েবলগুলোতে বুলিয়ান মান অ্যাসাইন করার সমস্যা।
বুলিয়ান ফর্মুলাটা সাধারণত CNF (কনজাঙ্কটিভ নর্মাল ফর্ম)-এ দেওয়া থাকে, যেটা একাধিক ক্লজের কনজাঙ্কশন, যেখানে প্রতিটা ক্লজ হলো লিটারেলগুলোর (ভেরিয়েবল বা ভেরিয়েবলের নেগেশন) ডিসজাঙ্কশন।
২-স্যাট (২-স্যাটিসফায়াবিলিটি) হলো SAT সমস্যার একটা সীমাবদ্ধতা, ২-স্যাটে প্রতিটা ক্লজে ঠিক দুটো লিটারেল থাকে।
এখানে এরকম একটা ২-স্যাট সমস্যার উদাহরণ দেওয়া হলো।
এমন $a, b, c$-এর অ্যাসাইনমেন্ট বের করো যেন নিচের ফর্মুলাটা সত্য হয়:

$$(a \lor \lnot b) \land (\lnot a \lor b) \land (\lnot a \lor \lnot b) \land (a \lor \lnot c)$$

SAT হলো NP-complete, এর জন্য কোনো পরিচিত দক্ষ সমাধান নেই।
তবে ২-স্যাট $O(n + m)$ সময়ে দক্ষভাবে সমাধান করা যায় যেখানে $n$ হলো ভেরিয়েবলের সংখ্যা এবং $m$ হলো ক্লজের সংখ্যা।

## অ্যালগরিদম:

প্রথমে আমাদের সমস্যাটাকে একটা ভিন্ন রূপে রূপান্তর করতে হবে, যেটাকে ইমপ্লিকেটিভ নর্মাল ফর্ম বলে।
লক্ষ্য করো $a \lor b$ রাশিটা $\lnot a \Rightarrow b \land \lnot b \Rightarrow a$ এর সমতুল্য (যদি দুটো ভেরিয়েবলের একটা মিথ্যা হয়, তাহলে অন্যটা অবশ্যই সত্য)।

এখন আমরা এই ইমপ্লিকেশনগুলোর একটা ডিরেক্টেড গ্রাফ (directed graph) বানাই:
প্রতিটা ভেরিয়েবল $x$-এর জন্য দুটো ভার্টেক্স $v_x$ এবং $v_{\lnot x}$ থাকবে।
এজগুলো ইমপ্লিকেশনের সাথে সঙ্গতিপূর্ণ হবে।

চলো ২-CNF ফর্মে উদাহরণটা দেখি:

$$(a \lor \lnot b) \land (\lnot a \lor b) \land (\lnot a \lor \lnot b) \land (a \lor \lnot c)$$

ওরিয়েন্টেড গ্রাফে নিচের ভার্টেক্স এবং এজ থাকবে:

$$\begin{array}{cccc}
\lnot a \Rightarrow \lnot b & a \Rightarrow b & a \Rightarrow \lnot b & \lnot a \Rightarrow \lnot c\\
b \Rightarrow a & \lnot b \Rightarrow \lnot a & b \Rightarrow \lnot a & c \Rightarrow a
\end{array}$$

তুমি নিচের ছবিতে ইমপ্লিকেশন গ্রাফটা দেখতে পারো:

<div style="text-align: center;">
  <img src="/images/graph/2SAT.png" alt=""Implication Graph of 2-SAT example"">
</div>

ইমপ্লিকেশন গ্রাফের একটা গুরুত্বপূর্ণ বৈশিষ্ট্য খেয়াল করো:
যদি $a \Rightarrow b$ এজ থাকে, তাহলে $\lnot b \Rightarrow \lnot a$ এজও থাকে।

এছাড়াও লক্ষ্য করো, যদি $x$ থেকে $\lnot x$ পৌঁছানো যায়, এবং $\lnot x$ থেকে $x$ পৌঁছানো যায়, তাহলে সমস্যার কোনো সমাধান নেই।
ভেরিয়েবল $x$-এর জন্য আমরা যে মানই বেছে নিই না কেন, এটা সবসময় একটা দ্বন্দ্বে গিয়ে শেষ হবে — যদি $x$-কে $\text{true}$ অ্যাসাইন করা হয় তাহলে ইমপ্লিকেশন বলে যে $\lnot x$-ও $\text{true}$ হওয়া উচিত এবং উল্টোটাও।
দেখা যায়, এই শর্তটা শুধু প্রয়োজনীয়ই না, যথেষ্টও।
আমরা নিচের কয়েকটা প্যারাগ্রাফে এটা প্রুফ করব।
প্রথমে মনে করো, যদি একটা ভার্টেক্স দ্বিতীয়টা থেকে পৌঁছানোযোগ্য হয়, এবং দ্বিতীয়টা প্রথমটা থেকে পৌঁছানোযোগ্য হয়, তাহলে এই দুটো ভার্টেক্স একই স্ট্রংলি কানেক্টেড কম্পোনেন্টে (strongly connected component) আছে।
তাই আমরা সমাধানের অস্তিত্বের শর্তটা এভাবে লিখতে পারি:

এই ২-স্যাট সমস্যার সমাধান থাকার জন্য, প্রয়োজনীয় ও যথেষ্ট শর্ত হলো যেকোনো ভেরিয়েবল $x$-এর জন্য ভার্টেক্স $x$ এবং $\lnot x$ ইমপ্লিকেশন গ্রাফের স্ট্রং কানেকশনের বিভিন্ন স্ট্রংলি কানেক্টেড কম্পোনেন্টে থাকবে।

এই শর্তটা সব স্ট্রংলি কানেক্টেড কম্পোনেন্ট খুঁজে $O(n + m)$ সময়ে চেক করা যায়।

নিচের ছবিতে উদাহরণটার সব স্ট্রংলি কানেক্টেড কম্পোনেন্ট দেখানো হয়েছে।
আমরা সহজেই চেক করতে পারি যে চারটা কম্পোনেন্টের কোনোটাতেই একটা ভার্টেক্স $x$ এবং তার নেগেশন $\lnot x$ একসাথে নেই, তাই উদাহরণটার একটা সমাধান আছে।
পরের প্যারাগ্রাফগুলোতে আমরা শিখব কীভাবে একটা বৈধ অ্যাসাইনমেন্ট বের করতে হয়, তবে শুধু দেখানোর জন্য $a = \text{false}$, $b = \text{false}$, $c = \text{false}$ সমাধানটা দেওয়া হলো।

<div style="text-align: center;">
  <img src="/images/graph/2SAT_SCC.png" alt=""Strongly Connected Components of the 2-SAT example"">
</div>

এখন আমরা ২-স্যাট সমস্যার সমাধান খোঁজার অ্যালগরিদম তৈরি করি এই অনুমানে যে সমাধান বিদ্যমান।

লক্ষ্য করো, সমাধান থাকলেও, ইমপ্লিকেশন গ্রাফে $x$ থেকে $\lnot x$ পৌঁছানো যেতে পারে, অথবা (কিন্তু একই সাথে না) $\lnot x$ থেকে $x$ পৌঁছানো যেতে পারে।
সেক্ষেত্রে $x$-এর জন্য $\text{true}$ বা $\text{false}$-এর একটা বাছাই দ্বন্দ্ব তৈরি করবে, অন্যটা করবে না।
চলো শিখি কীভাবে এমন মান বাছাই করতে হয় যেন আমরা দ্বন্দ্ব তৈরি না করি।

আমরা স্ট্রংলি কানেক্টেড কম্পোনেন্টগুলো টপোলজিক্যাল ক্রমে সাজাই (মানে $v$ থেকে $u$-তে পাথ থাকলে $\text{comp}[v] \le \text{comp}[u]$) এবং $\text{comp}[v]$ দিয়ে $v$ ভার্টেক্স যে স্ট্রংলি কানেক্টেড কম্পোনেন্টে আছে তার ইনডেক্স বোঝানো হোক।
তাহলে, যদি $\text{comp}[x] < \text{comp}[\lnot x]$ হয় তাহলে আমরা $x$-কে $\text{false}$ অ্যাসাইন করি, নাহলে $\text{true}$।

চলো প্রুফ করি যে ভেরিয়েবলগুলোর এই অ্যাসাইনমেন্টে আমরা দ্বন্দ্বে পড়ি না।
ধরো $x$-কে $\text{true}$ অ্যাসাইন করা হয়েছে।
অন্য ক্ষেত্রটি একইভাবে প্রুফ করা যায়।

প্রথমে আমরা প্রুফ করি যে ভার্টেক্স $x$ থেকে ভার্টেক্স $\lnot x$ পৌঁছানো সম্ভব নয়।
যেহেতু আমরা $\text{true}$ অ্যাসাইন করেছি, তাই $x$-এর স্ট্রংলি কানেক্টেড কম্পোনেন্টের ইনডেক্স $\lnot x$-এর কম্পোনেন্টের ইনডেক্সের চেয়ে বড়।
তারমানে $\lnot x$, $x$ ধারণকারী কম্পোনেন্টের বামে আছে, এবং পরেরটা থেকে প্রথমটাতে পৌঁছানো সম্ভব না।

দ্বিতীয়ত আমরা প্রুফ করি যে এমন কোনো ভেরিয়েবল $y$ নেই, যেন ইমপ্লিকেশন গ্রাফে $x$ থেকে $y$ এবং $\lnot y$ দুটোই পৌঁছানোযোগ্য।
এটা একটা দ্বন্দ্ব তৈরি করত, কারণ $x = \text{true}$ মানে $y = \text{true}$ এবং $\lnot y = \text{true}$।
চলো পরোক্ষ প্রুফ করি।
ধরো $y$ এবং $\lnot y$ দুটোই $x$ থেকে পৌঁছানোযোগ্য, তাহলে ইমপ্লিকেশন গ্রাফের বৈশিষ্ট্য অনুযায়ী $\lnot x$, $y$ এবং $\lnot y$ দুটো থেকেই পৌঁছানোযোগ্য।
ট্রানজিটিভিটি থেকে এর ফলে $\lnot x$, $x$ থেকে পৌঁছানোযোগ্য, যেটা অনুমানের সাথে দ্বন্দ্ব করে।

তাহলে আমরা এমন একটা অ্যালগরিদম বানিয়েছি যেটা ভেরিয়েবলগুলোর প্রয়োজনীয় মান খুঁজে বের করে এই অনুমানে যে যেকোনো ভেরিয়েবল $x$-এর জন্য ভার্টেক্স $x$ এবং $\lnot x$ ভিন্ন স্ট্রংলি কানেক্টেড কম্পোনেন্টে আছে।
উপরে এই অ্যালগরিদমের সঠিকতা প্রুফ করা হয়েছে।
তাহলে আমরা একই সাথে সমাধানের অস্তিত্বের আগে বলা শর্তটাও প্রুফ করলাম।

## ইমপ্লিমেন্টেশন:

এখন আমরা সম্পূর্ণ অ্যালগরিদম ইমপ্লিমেন্ট করতে পারি।
প্রথমে আমরা ইমপ্লিকেশনের গ্রাফ তৈরি করি এবং সকল স্ট্রংলি কানেক্টেড কম্পোনেন্ট খুঁজি।
এটা কোসারাজুর অ্যালগরিদম দিয়ে $O(n + m)$ সময়ে করা যায়।
গ্রাফের দ্বিতীয় ট্রাভার্সালে কোসারাজুর অ্যালগরিদম স্ট্রংলি কানেক্টেড কম্পোনেন্টগুলো টপোলজিক্যাল ক্রমে ভিজিট করে, তাই প্রতিটি ভার্টেক্স $v$-এর জন্য $\text{comp}[v]$ গণনা করা সহজ।

এরপর আমরা $\text{comp}[x]$ এবং $\text{comp}[\lnot x]$ তুলনা করে $x$-এর অ্যাসাইনমেন্ট বাছাই করতে পারি।
যদি $\text{comp}[x] = \text{comp}[\lnot x]$ হয় তাহলে আমরা $\text{false}$ রিটার্ন করি এটা বোঝাতে যে ২-স্যাট সমস্যা সিদ্ধ করে এমন কোনো বৈধ অ্যাসাইনমেন্ট নেই।

নিচে আগে থেকে তৈরি করা ইমপ্লিকেশনের গ্রাফ $adj$ এবং ট্রান্সপোজ গ্রাফ $adj^{\intercal}$ (যেখানে প্রতিটা এজের দিক উল্টানো হয়েছে) ব্যবহার করে ২-স্যাট সমস্যার সমাধানের ইমপ্লিমেন্টেশন দেওয়া হলো।
গ্রাফে $2k$ এবং $2k+1$ ইনডেক্সের ভার্টেক্সগুলো ভেরিয়েবল $k$-এর দুটো ভার্টেক্স, যেখানে $2k+1$ নেগেটেড ভেরিয়েবলের সাথে সঙ্গতিপূর্ণ।

```cpp
struct TwoSatSolver {
    int n_vars;
    int n_vertices;
    vector<vector<int>> adj, adj_t;
    vector<bool> used;
    vector<int> order, comp;
    vector<bool> assignment;

    TwoSatSolver(int _n_vars) : n_vars(_n_vars), n_vertices(2 * n_vars), adj(n_vertices), adj_t(n_vertices), used(n_vertices), order(), comp(n_vertices, -1), assignment(n_vars) {
        order.reserve(n_vertices);
    }
    void dfs1(int v) {
        used[v] = true;
        for (int u : adj[v]) {
            if (!used[u])
                dfs1(u);
        }
        order.push_back(v);
    }

    void dfs2(int v, int cl) {
        comp[v] = cl;
        for (int u : adj_t[v]) {
            if (comp[u] == -1)
                dfs2(u, cl);
        }
    }

    bool solve_2SAT() {
        order.clear();
        used.assign(n_vertices, false);
        for (int i = 0; i < n_vertices; ++i) {
            if (!used[i])
                dfs1(i);
        }

        comp.assign(n_vertices, -1);
        for (int i = 0, j = 0; i < n_vertices; ++i) {
            int v = order[n_vertices - i - 1];
            if (comp[v] == -1)
                dfs2(v, j++);
        }

        assignment.assign(n_vars, false);
        for (int i = 0; i < n_vertices; i += 2) {
            if (comp[i] == comp[i + 1])
                return false;
            assignment[i / 2] = comp[i] > comp[i + 1];
        }
        return true;
    }

    void add_disjunction(int a, bool na, int b, bool nb) {
        // na and nb signify whether a and b are to be negated
        a = 2 * a ^ na;
        b = 2 * b ^ nb;
        int neg_a = a ^ 1;
        int neg_b = b ^ 1;
        adj[neg_a].push_back(b);
        adj[neg_b].push_back(a);
        adj_t[b].push_back(neg_a);
        adj_t[a].push_back(neg_b);
    }

    static void example_usage() {
        TwoSatSolver solver(3); // a, b, c
        solver.add_disjunction(0, false, 1, true);  //     a  v  not b
        solver.add_disjunction(0, true, 1, true);   // not a  v  not b
        solver.add_disjunction(1, false, 2, false); //     b  v      c
        solver.add_disjunction(0, false, 0, false); //     a  v      a
        assert(solver.solve_2SAT() == true);
        auto expected = vector<bool>{{true, false, true}};
        assert(solver.assignment == expected);
    }
};
```

## অনুশীলন সমস্যা
 * [Codeforces: The Door Problem](http://codeforces.com/contest/776/problem/D)
 * [Kattis: Illumination](https://open.kattis.com/problems/illumination)
 * [UVA: Rectangles](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3081)
 * [Codeforces : Radio Stations](https://codeforces.com/problemset/problem/1215/F)
 * [CSES : Giant Pizza](https://cses.fi/problemset/task/1684)
 * [Codeforces: +-1](https://codeforces.com/contest/1971/problem/H)
 * [Gym: (C) Colorful Village](https://codeforces.com/gym/104772/problem/C)
 * [POI: Renovation](https://szkopul.edu.pl/problemset/problem/xNjwUvwdHQoQTFBrmyG8vD1O/site/?key=statement)
