---
title: "ফেনউইক ট্রি"
tags: 
weight: 20
---
# ফেনউইক ট্রি

ধরি $f$ একটি গ্রুপ অপারেশন (একটি সেটের উপর একটি দ্বিমিক সংযুক্ত ফাংশন যার একটি অভেদ উপাদান ও বিপরীত উপাদান আছে) এবং $A$ হলো $N$ দৈর্ঘ্যের একটি পূর্ণসংখ্যা অ্যারে।
$f$ এর ইনফিক্স চিহ্নকে $*$ দ্বারা চিহ্নিত করি; অর্থাৎ, যেকোনো পূর্ণসংখ্যা $x,y$ এর জন্য $f(x,y) = x*y$।
(যেহেতু এটি সংযুক্ত, ইনফিক্স চিহ্ন ব্যবহারে $f$ এর প্রয়োগ ক্রমের জন্য বন্ধনী বাদ দেবো।)

ফেনউইক ট্রি এমন একটি ডেটা স্ট্রাকচার যা:

* প্রদত্ত রেঞ্জ $[l, r]$-এ ফাংশন $f$ এর মান (অর্থাৎ $A_l * A_{l+1} * \dots * A_r$) $O(\log N)$ সময়ে গণনা করে
* $A$ এর একটি উপাদানের মান $O(\log N)$ সময়ে আপডেট করে
* $O(N)$ মেমরি প্রয়োজন ($A$ এর জন্য প্রয়োজনীয় একই পরিমাণ)
* ব্যবহার ও কোড করা সহজ, বিশেষত বহুমাত্রিক অ্যারের ক্ষেত্রে

ফেনউইক ট্রির সবচেয়ে সাধারণ প্রয়োগ হলো _একটি রেঞ্জের যোগফল গণনা_।
উদাহরণস্বরূপ, পূর্ণসংখ্যার সেটের উপর যোগ গ্রুপ অপারেশন হিসেবে ব্যবহার করলে, অর্থাৎ $f(x,y) = x + y$: দ্বিমিক অপারেশন, $*$, এক্ষেত্রে $+$, তাই $A_l * A_{l+1} * \dots * A_r = A_l + A_{l+1} + \dots + A_{r}$।

ফেনউইক ট্রিকে **বাইনারি ইনডেক্সড ট্রি** (BIT)-ও বলা হয়।
এটি প্রথম "A new data structure for cumulative frequency tables" (Peter M. Fenwick, ১৯৯৪) শিরোনামের একটি পত্রে বর্ণিত হয়।

## বর্ণনা

### পরিদর্শন

সরলতার খাতিরে, আমরা ধরে নেবো ফাংশন $f$ পূর্ণসংখ্যার উপর $f(x,y) = x + y$ হিসেবে সংজ্ঞায়িত।

ধরি একটি পূর্ণসংখ্যা অ্যারে দেওয়া আছে, $A[0 \dots N-1]$।
(লক্ষ্য করুন আমরা শূন্য-ভিত্তিক ইনডেক্সিং ব্যবহার করছি।)
একটি ফেনউইক ট্রি শুধু একটি অ্যারে, $T[0 \dots N-1]$, যেখানে প্রতিটি উপাদান $A$ এর কোনো রেঞ্জ $[g(i), i]$-এ উপাদানের যোগফলের সমান:

$$T_i = \sum_{j = g(i)}^{i}{A_j}$$

যেখানে $g$ এমন কোনো ফাংশন যা $0 \le g(i) \le i$ পূরণ করে।
আমরা পরের কয়েকটি অনুচ্ছেদে $g$ সংজ্ঞায়িত করবো।

ডেটা স্ট্রাকচারটিকে ট্রি বলা হয় কারণ একে ট্রি আকারে সুন্দরভাবে উপস্থাপন করা যায়, যদিও আমাদের নোড ও প্রান্ত সহ একটি প্রকৃত ট্রি মডেল করার দরকার নেই।
সব কোয়েরি পরিচালনা করতে শুধু $T$ অ্যারে বজায় রাখতে হবে।

**দ্রষ্টব্য:** এখানে উপস্থাপিত ফেনউইক ট্রি শূন্য-ভিত্তিক ইনডেক্সিং ব্যবহার করে।
অনেকে এক-ভিত্তিক ইনডেক্সিং ব্যবহার করেন।
তাই আপনি ইমপ্লিমেন্টেশন বিভাগে এক-ভিত্তিক ইনডেক্সিং ব্যবহারকারী একটি বিকল্প ইমপ্লিমেন্টেশনও পাবেন।
সময় ও মেমরি কমপ্লেক্সিটিতে উভয় সংস্করণ সমতুল্য।

এখন আমরা উপরে উল্লেখিত দুটি অপারেশনের জন্য কিছু সিউডো-কোড লিখতে পারি।
নিচে, আমরা $A$ এর $[0, r]$ রেঞ্জে উপাদানের যোগফল বের করি এবং কোনো উপাদান $A_i$ আপডেট (বৃদ্ধি) করি:

```python
def sum(int r):
    res = 0
    while (r >= 0):
        res += t[r]
        r = g(r) - 1
    return res

def increase(int i, int delta):
    for all j with g(j) <= i <= j:
        t[j] += delta
```

`sum` ফাংশন নিম্নরূপে কাজ করে:

১. প্রথমে, $[g(r), r]$ রেঞ্জের যোগফল (অর্থাৎ $T[r]$) `result`-এ যোগ করে।
২. তারপর, $[g(g(r)-1), g(r)-1]$ রেঞ্জে "লাফ" দেয় এবং এই রেঞ্জের যোগফল `result`-এ যোগ করে।
৩. এটি চলতে থাকে যতক্ষণ না $[0, g(g( \dots g(r)-1 \dots -1)-1)]$ থেকে $[g(-1), -1]$-এ "লাফ" দেয়; এখানে `sum` ফাংশন লাফানো বন্ধ করে।

`increase` ফাংশন একই সাদৃশ্যে কাজ করে, কিন্তু ক্রমবর্ধমান ইনডেক্সের দিকে "লাফ" দেয়:

১. $[g(j), j]$ আকারের প্রতিটি রেঞ্জের যোগফল যা $g(j) \le i \le j$ শর্ত পূরণ করে `delta` দ্বারা বৃদ্ধি পায়; অর্থাৎ, `t[j] += delta`।
তাই, এটি $T$ এর সব উপাদান আপডেট করে যেগুলো $A_i$ ধারণকারী রেঞ্জের সাথে সংশ্লিষ্ট।

`sum` ও `increase` উভয়ের কমপ্লেক্সিটি ফাংশন $g$ এর উপর নির্ভর করে।
$g$ ফাংশন বেছে নেওয়ার অনেক উপায় আছে যেন সব $i$ এর জন্য $0 \le g(i) \le i$ হয়।
উদাহরণস্বরূপ, $g(i) = i$ ফাংশন কাজ করে, যেখানে $T = A$ হয় (এক্ষেত্রে, যোগফল কোয়েরি ধীর)।
আমরা $g(i) = 0$ ফাংশনও নিতে পারি।
এটি প্রিফিক্স সাম অ্যারের সাথে সংশ্লিষ্ট ($[0, i]$ রেঞ্জের যোগফল ধ্রুবক সময়ে পাওয়া যাবে; তবে, অ্যারে উপাদান আপডেটে $O(n)$ পরিবর্তন দরকার)।
ফেনউইক ট্রির অ্যালগরিদমের চতুর অংশ হলো $g$ ফাংশনের একটি বিশেষ সংজ্ঞা ব্যবহার করা যা উভয় অপারেশন $O(\log N)$ সময়ে পরিচালনা করতে পারে।

### $g(i)$ এর সংজ্ঞা { data-toc-label='$g(i)$ এর সংজ্ঞা' }

$g(i)$ এর গণনা নিম্নলিখিত সরল অপারেশন দিয়ে সংজ্ঞায়িত:
আমরা $i$ এর বাইনারি উপস্থাপনায় সব পশ্চাদ্বর্তী $1$ বিট $0$ বিট দিয়ে প্রতিস্থাপন করি।

অন্য কথায়, $i$ এর বাইনারিতে সবচেয়ে কম তাৎপর্যপূর্ণ অঙ্ক $0$ হলে, $g(i) = i$।
অন্যথায় সবচেয়ে কম তাৎপর্যপূর্ণ অঙ্ক $1$, এবং আমরা এই $1$ ও অন্য সব পশ্চাদ্বর্তী $1$ উল্টে দিই।

উদাহরণস্বরূপ

$$\begin{align}
g(11) = g(1011_2) = 1000_2 &= 8 \\\\
g(12) = g(1100_2) = 1100_2 &= 12 \\\\
g(13) = g(1101_2) = 1100_2 &= 12 \\\\
g(14) = g(1110_2) = 1110_2 &= 14 \\\\
g(15) = g(1111_2) = 0000_2 &= 0 \\\\
\end{align}$$

উপরে বর্ণিত অ-তুচ্ছ অপারেশনের জন্য বিটওয়াইজ অপারেশন ব্যবহার করে একটি সরল ইমপ্লিমেন্টেশন আছে:

$$g(i) = i ~\&~ (i+1),$$

যেখানে $\&$ হলো বিটওয়াইজ AND অপারেটর। নিজেকে বোঝানো কঠিন নয় যে এই সমাধান উপরে বর্ণিত অপারেশনের মতোই কাজ করে।

এখন, সব $j$ খুঁজতে হবে যেন $g(j) \le i \le j$।

দেখা সহজ যে $i$ থেকে শুরু করে এবং শেষ আনসেট বিট উল্টে সব এরকম $j$ পাওয়া যায়।
এই অপারেশনকে $h(j)$ বলবো।
উদাহরণস্বরূপ, $i = 10$ এর জন্য:

$$\begin{align}
10 &= 0001010_2 \\\\
h(10) = 11 &= 0001011_2 \\\\
h(11) = 15 &= 0001111_2 \\\\
h(15) = 31 &= 0011111_2 \\\\
h(31) = 63 &= 0111111_2 \\\\
\vdots &
\end{align}$$

আশ্চর্যজনকভাবে, বিটওয়াইজ অপারেশন ব্যবহার করে $h$ করারও একটি সরল উপায় আছে:

$$h(j) = j ~|~ (j+1),$$

যেখানে $|$ হলো বিটওয়াইজ OR অপারেটর।

নিচের ছবিটি ফেনউইক ট্রির ট্রি হিসেবে একটি সম্ভব্য ব্যাখ্যা দেখায়।
ট্রির নোডগুলো তাদের কভার করা রেঞ্জ দেখায়।

<div style="text-align: center;">
  <img src="/images/data_structures/binary_indexed_tree.png" alt="Binary Indexed Tree">
</div>

## ইমপ্লিমেন্টেশন

### একমাত্রিক অ্যারেতে যোগফল বের করা

এখানে যোগফল কোয়েরি ও একক আপডেটের জন্য ফেনউইক ট্রির একটি ইমপ্লিমেন্টেশন।

সাধারণ ফেনউইক ট্রি শুধু $[0, r]$ ধরনের যোগফল কোয়েরি `sum(int r)` ব্যবহার করে উত্তর দিতে পারে, তবে $[l, r]$ ধরনের অন্যান্য কোয়েরিও দুটি যোগফল $[0, r]$ ও $[0, l-1]$ গণনা করে এবং বিয়োগ করে উত্তর দেওয়া যায়।
এটি `sum(int l, int r)` মেথডে পরিচালিত।

এই ইমপ্লিমেন্টেশন দুটি কনস্ট্রাক্টর সমর্থন করে।
আপনি শূন্য দিয়ে ইনিশিয়ালাইজ করা ফেনউইক ট্রি তৈরি করতে পারেন, অথবা একটি বিদ্যমান অ্যারেকে ফেনউইক আকারে রূপান্তর করতে পারেন।


```cpp
struct FenwickTree {
    vector<int> bit;  // binary indexed tree
    int n;

    FenwickTree(int n) {
        this->n = n;
        bit.assign(n, 0);
    }

    FenwickTree(vector<int> const &a) : FenwickTree(a.size()) {
        for (size_t i = 0; i < a.size(); i++)
            add(i, a[i]);
    }

    int sum(int r) {
        int ret = 0;
        for (; r >= 0; r = (r & (r + 1)) - 1)
            ret += bit[r];
        return ret;
    }

    int sum(int l, int r) {
        return sum(r) - sum(l - 1);
    }

    void add(int idx, int delta) {
        for (; idx < n; idx = idx | (idx + 1))
            bit[idx] += delta;
    }
};
```

### লিনিয়ার কনস্ট্রাকশন

উপরের ইমপ্লিমেন্টেশনে $O(N \log N)$ সময় লাগে।
এটি $O(N)$ সময়ে উন্নত করা সম্ভব।

ধারণাটি হলো, ইনডেক্স $i$ এর সংখ্যা $a[i]$ $bit[i]$-তে সংরক্ষিত রেঞ্জে অবদান রাখবে, এবং ইনডেক্স $i | (i + 1)$ যেসব রেঞ্জে অবদান রাখে তাদের সবগুলোতেও।
তাই ক্রমানুসারে সংখ্যা যোগ করলে, আপনাকে শুধু বর্তমান যোগফল পরবর্তী রেঞ্জে ঠেলে দিতে হবে, যেখান থেকে এটি আবার পরবর্তী রেঞ্জে ঠেলে দেওয়া হবে, এভাবে চলতে থাকবে।

```cpp
FenwickTree(vector<int> const &a) : FenwickTree(a.size()){
    for (int i = 0; i < n; i++) {
        bit[i] += a[i];
        int r = i | (i + 1);
        if (r < n) bit[r] += bit[i];
    }
}
```

### একমাত্রিক অ্যারেতে $[0, r]$ এর সর্বনিম্ন খোঁজা { data-toc-label='একমাত্রিক অ্যারেতে $[0, r]$ এর সর্বনিম্ন খোঁজা' }

এটা স্পষ্ট যে ফেনউইক ট্রি ব্যবহার করে $[l, r]$ রেঞ্জের সর্বনিম্ন খোঁজার কোনো সহজ উপায় নেই, কারণ ফেনউইক ট্রি শুধু $[0, r]$ ধরনের কোয়েরি উত্তর দিতে পারে।
এছাড়াও, প্রতিবার মান `update` হলে, নতুন মান বর্তমান মানের চেয়ে ছোট হতে হবে।
উভয় উল্লেখযোগ্য সীমাবদ্ধতা কারণ $min$ অপারেশন পূর্ণসংখ্যার সেটের সাথে একটি গ্রুপ গঠন করে না, কারণ কোনো বিপরীত উপাদান নেই।

```cpp
struct FenwickTreeMin {
    vector<int> bit;
    int n;
    const int INF = (int)1e9;

    FenwickTreeMin(int n) {
        this->n = n;
        bit.assign(n, INF);
    }

    FenwickTreeMin(vector<int> a) : FenwickTreeMin(a.size()) {
        for (size_t i = 0; i < a.size(); i++)
            update(i, a[i]);
    }

    int getmin(int r) {
        int ret = INF;
        for (; r >= 0; r = (r & (r + 1)) - 1)
            ret = min(ret, bit[r]);
        return ret;
    }

    void update(int idx, int val) {
        for (; idx < n; idx = idx | (idx + 1))
            bit[idx] = min(bit[idx], val);
    }
};
```

দ্রষ্টব্য: যেকোনো সর্বনিম্ন রেঞ্জ কোয়েরি ও যেকোনো আপডেট পরিচালনা করতে পারে এমন ফেনউইক ট্রি ইমপ্লিমেন্ট করা সম্ভব।
[Efficient Range Minimum Queries using Binary Indexed Trees](http://ioinformatics.org/oi/pdf/v9_2015_39_44.pdf) পত্রটি এরকম একটি পদ্ধতি বর্ণনা করে।
তবে সেই পদ্ধতিতে ডেটার উপর একটি দ্বিতীয় বাইনারি ইনডেক্সড ট্রি বজায় রাখতে হয়, কিছুটা ভিন্ন কাঠামোর সাথে, কারণ একটি ট্রি অ্যারের সব উপাদানের মান সংরক্ষণ করতে যথেষ্ট নয়।
যোগফলের সাধারণ ইমপ্লিমেন্টেশনের তুলনায় ইমপ্লিমেন্টেশনও অনেক কঠিন।

### দ্বিমাত্রিক অ্যারেতে যোগফল বের করা

আগে দাবি করা হয়েছে, বহুমাত্রিক অ্যারের জন্য ফেনউইক ট্রি ইমপ্লিমেন্ট করা অত্যন্ত সহজ।

```cpp
struct FenwickTree2D {
    vector<vector<int>> bit;
    int n, m;

    // init(...) { ... }

    int sum(int x, int y) {
        int ret = 0;
        for (int i = x; i >= 0; i = (i & (i + 1)) - 1)
            for (int j = y; j >= 0; j = (j & (j + 1)) - 1)
                ret += bit[i][j];
        return ret;
    }

    void add(int x, int y, int delta) {
        for (int i = x; i < n; i = i | (i + 1))
            for (int j = y; j < m; j = j | (j + 1))
                bit[i][j] += delta;
    }
};
```

### এক-ভিত্তিক ইনডেক্সিং পদ্ধতি

এই পদ্ধতির জন্য আমরা $T[]$ ও $g()$ এর প্রয়োজনীয়তা ও সংজ্ঞা কিছুটা পরিবর্তন করি।
আমরা চাই $T[i]$ $[g(i)+1; i]$ রেঞ্জের যোগফল সংরক্ষণ করুক।
এটি ইমপ্লিমেন্টেশন কিছুটা পরিবর্তন করে, এবং $g(i)$ এর জন্য একইরকম সুন্দর সংজ্ঞা দেয়:

```python
def sum(int r):
    res = 0
    while (r > 0):
        res += t[r]
        r = g(r)
    return res

def increase(int i, int delta):
    for all j with g(j) < i <= j:
        t[j] += delta
```

$g(i)$ এর গণনা সংজ্ঞায়িত:
$i$ এর বাইনারি উপস্থাপনায় শেষ সেট $1$ বিট টগল করা।

$$\begin{align}
g(7) = g(111_2) = 110_2 &= 6 \\\\
g(6) = g(110_2) = 100_2 &= 4 \\\\
g(4) = g(100_2) = 000_2 &= 0 \\\\
\end{align}$$

শেষ সেট বিট $i ~\&~ (-i)$ দিয়ে বের করা যায়, তাই অপারেশনটি এভাবে প্রকাশ করা যায়:

$$g(i) = i - (i ~\&~ (-i)).$$

এবং দেখা কঠিন নয় যে, $A[j]$ আপডেট করতে চাইলে $i,~ h(i),~ h(h(i)),~ \dots$ ক্রমের সব $T[j]$ মান পরিবর্তন করতে হবে, যেখানে $h(i)$ সংজ্ঞায়িত:

$$h(i) = i + (i ~\&~ (-i)).$$

দেখতে পাচ্ছেন, এই পদ্ধতির প্রধান সুবিধা হলো বাইনারি অপারেশনগুলো পরস্পরকে খুব সুন্দরভাবে পরিপূরক করে।

নিচের ইমপ্লিমেন্টেশন অন্য ইমপ্লিমেন্টেশনগুলোর মতোই ব্যবহার করা যায়, তবে অভ্যন্তরীণভাবে এক-ভিত্তিক ইনডেক্সিং ব্যবহার করে।

```cpp
struct FenwickTreeOneBasedIndexing {
    vector<int> bit;  // binary indexed tree
    int n;

    FenwickTreeOneBasedIndexing(int n) {
        this->n = n + 1;
        bit.assign(n + 1, 0);
    }

    FenwickTreeOneBasedIndexing(vector<int> a)
        : FenwickTreeOneBasedIndexing(a.size()) {
        for (size_t i = 0; i < a.size(); i++)
            add(i, a[i]);
    }

    int sum(int idx) {
        int ret = 0;
        for (++idx; idx > 0; idx -= idx & -idx)
            ret += bit[idx];
        return ret;
    }

    int sum(int l, int r) {
        return sum(r) - sum(l - 1);
    }

    void add(int idx, int delta) {
        for (++idx; idx < n; idx += idx & -idx)
            bit[idx] += delta;
    }
};
```

## রেঞ্জ অপারেশন

একটি ফেনউইক ট্রি নিম্নলিখিত রেঞ্জ অপারেশন সমর্থন করতে পারে:

১. পয়েন্ট আপডেট ও রেঞ্জ কোয়েরি
২. রেঞ্জ আপডেট ও পয়েন্ট কোয়েরি
৩. রেঞ্জ আপডেট ও রেঞ্জ কোয়েরি

### ১. পয়েন্ট আপডেট ও রেঞ্জ কোয়েরি

এটি উপরে ব্যাখ্যা করা সাধারণ ফেনউইক ট্রি।

### ২. রেঞ্জ আপডেট ও পয়েন্ট কোয়েরি

সরল কৌশল ব্যবহার করে আমরা বিপরীত অপারেশনও করতে পারি: রেঞ্জ বৃদ্ধি ও একক মান কোয়েরি।

ধরি ফেনউইক ট্রি শূন্য দিয়ে ইনিশিয়ালাইজ করা।
ধরি আমরা $[l, r]$ ব্যবধানকে $x$ দিয়ে বৃদ্ধি করতে চাই।
আমরা ফেনউইক ট্রিতে দুটি পয়েন্ট আপডেট অপারেশন করি: `add(l, x)` ও `add(r+1, -x)`।

$A[i]$ এর মান পেতে চাইলে, সাধারণ রেঞ্জ সাম মেথড ব্যবহার করে প্রিফিক্স সাম নিলেই হবে।
এটি কেন সত্য তা দেখতে, আমরা শুধু আগের বৃদ্ধি অপারেশনে মনোযোগ দিতে পারি।
যদি $i < l$, তাহলে দুটি আপডেট অপারেশন কোয়েরিতে কোনো প্রভাব ফেলে না এবং যোগফল $0$ পাই।
যদি $i \in [l, r]$, তাহলে প্রথম আপডেট অপারেশনের কারণে উত্তর $x$ পাই।
এবং যদি $i > r$, তাহলে দ্বিতীয় আপডেট অপারেশন প্রথমটির প্রভাব বাতিল করবে।

নিচের ইমপ্লিমেন্টেশন এক-ভিত্তিক ইনডেক্সিং ব্যবহার করে।

```cpp
void add(int idx, int val) {
    for (++idx; idx < n; idx += idx & -idx)
        bit[idx] += val;
}

void range_add(int l, int r, int val) {
    add(l, val);
    add(r + 1, -val);
}

int point_query(int idx) {
    int ret = 0;
    for (++idx; idx > 0; idx -= idx & -idx)
        ret += bit[idx];
    return ret;
}
```

দ্রষ্টব্য: অবশ্যই `range_add(i, i, val)` দিয়ে একক বিন্দু $A[i]$ বৃদ্ধি করাও সম্ভব।

### ৩. রেঞ্জ আপডেট ও রেঞ্জ কোয়েরি

রেঞ্জ আপডেট ও রেঞ্জ কোয়েরি উভয় সমর্থন করতে আমরা দুটি BIT ব্যবহার করবো, $B_1[]$ ও $B_2[]$, শূন্য দিয়ে ইনিশিয়ালাইজ করা।

ধরি আমরা $[l, r]$ ব্যবধানকে $x$ মান দিয়ে বৃদ্ধি করতে চাই।
আগের পদ্ধতির মতোই, আমরা $B_1$ এ দুটি পয়েন্ট আপডেট করি: `add(B1, l, x)` ও `add(B1, r+1, -x)`।
এবং $B_2$-ও আপডেট করি। বিবরণ পরে ব্যাখ্যা করা হবে।

```python
def range_add(l, r, x):
    add(B1, l, x)
    add(B1, r+1, -x)
    add(B2, l, x*(l-1))
    add(B2, r+1, -x*r))
```
রেঞ্জ আপডেট $(l, r, x)$ এর পর রেঞ্জ সাম কোয়েরি নিম্নলিখিত মান দেওয়া উচিত:

$$
sum[0, i]=
\begin{cases}
0 & i < l \\\\
x \cdot (i-(l-1)) & l \le i \le r \\\\
x \cdot (r-l+1) & i > r \\\\
\end{cases}
$$

রেঞ্জ সামকে দুটি পদের পার্থক্য হিসেবে লেখা যায়, যেখানে প্রথম পদের জন্য $B_1$ ও দ্বিতীয় পদের জন্য $B_2$ ব্যবহার করি।
কোয়েরির পার্থক্য $[0, i]$ এর উপর প্রিফিক্স সাম দেবে।

$$\begin{align}
sum[0, i] &= sum(B_1, i) \cdot i - sum(B_2, i) \\\\
&= \begin{cases}
0 \cdot i - 0 & i < l\\\\
x \cdot i - x \cdot (l-1) & l \le i \le r \\\\
0 \cdot i - (x \cdot (l-1) - x \cdot r) & i > r \\\\
\end{cases}
\end{align}
$$

শেষ রাশিটি ঠিক প্রয়োজনীয় পদগুলোর সমান।
সুতরাং $B_1[i]\times i$ গুণ করার সময় অতিরিক্ত পদ ছেঁটে ফেলতে আমরা $B_2$ ব্যবহার করতে পারি।

$l-1$ ও $r$ এর জন্য প্রিফিক্স সাম গণনা করে এবং তাদের পার্থক্য নিয়ে যেকোনো রেঞ্জ সাম পাওয়া যায়।

```python
def add(b, idx, x):
    while idx <= N:
        b[idx] += x
        idx += idx & -idx

def range_add(l,r,x):
    add(B1, l, x)
    add(B1, r+1, -x)
    add(B2, l, x*(l-1))
    add(B2, r+1, -x*r)

def sum(b, idx):
    total = 0
    while idx > 0:
        total += b[idx]
        idx -= idx & -idx
    return total

def prefix_sum(idx):
    return sum(B1, idx)*idx -  sum(B2, idx)

def range_sum(l, r):
    return prefix_sum(r) - prefix_sum(l-1)
```

## অনুশীলন সমস্যা

* [UVA 12086 - Potentiometers](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3238)
* [LOJ 1112 - Curious Robin Hood](http://www.lightoj.com/volume_showproblem.php?problem=1112)
* [LOJ 1266 - Points in Rectangle](http://www.lightoj.com/volume_showproblem.php?problem=1266 "2D Fenwick Tree")
* [Codechef - SPREAD](http://www.codechef.com/problems/SPREAD)
* [SPOJ - CTRICK](http://www.spoj.com/problems/CTRICK/)
* [SPOJ - MATSUM](http://www.spoj.com/problems/MATSUM/)
* [SPOJ - DQUERY](http://www.spoj.com/problems/DQUERY/)
* [SPOJ - NKTEAM](http://www.spoj.com/problems/NKTEAM/)
* [SPOJ - YODANESS](http://www.spoj.com/problems/YODANESS/)
* [SRM 310 - FloatingMedian](https://community.topcoder.com/stat?c=problem_statement&pm=6551&rd=9990)
* [SPOJ - Ada and Behives](http://www.spoj.com/problems/ADABEHIVE/)
* [Hackerearth - Counting in Byteland](https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/counting-in-byteland/)
* [DevSkill - Shan and String (archived)](http://web.archive.org/web/20210322010617/https://devskill.com/CodingProblems/ViewProblem/300)
* [Codeforces - Little Artem and Time Machine](http://codeforces.com/contest/669/problem/E)
* [Codeforces - Hanoi Factory](http://codeforces.com/contest/777/problem/E)
* [SPOJ - Tulip and Numbers](http://www.spoj.com/problems/TULIPNUM/)
* [SPOJ - SUMSUM](http://www.spoj.com/problems/SUMSUM/)
* [SPOJ - Sabir and Gifts](http://www.spoj.com/problems/SGIFT/)
* [SPOJ - The Permutation Game Again](http://www.spoj.com/problems/TPGA/)
* [SPOJ - Zig when you Zag](http://www.spoj.com/problems/ZIGZAG2/)
* [SPOJ - Cryon](http://www.spoj.com/problems/CRAYON/)
* [SPOJ - Weird Points](http://www.spoj.com/problems/DCEPC705/)
* [SPOJ - Its a Murder](http://www.spoj.com/problems/DCEPC206/)
* [SPOJ - Bored of Suffixes and Prefixes](http://www.spoj.com/problems/KOPC12G/)
* [SPOJ - Mega Inversions](http://www.spoj.com/problems/TRIPINV/)
* [Codeforces - Subsequences](http://codeforces.com/contest/597/problem/C)
* [Codeforces - Ball](http://codeforces.com/contest/12/problem/D)
* [GYM - The Kamphaeng Phet's Chedis](http://codeforces.com/gym/101047/problem/J)
* [Codeforces - Garlands](http://codeforces.com/contest/707/problem/E)
* [Codeforces - Inversions after Shuffle](http://codeforces.com/contest/749/problem/E)
* [GYM - Cairo Market](http://codeforces.com/problemset/gymProblem/101055/D)
* [Codeforces - Goodbye Souvenir](http://codeforces.com/contest/849/problem/E)
* [SPOJ - Ada and Species](http://www.spoj.com/problems/ADACABAA/)
* [Codeforces - Thor](https://codeforces.com/problemset/problem/704/A)
* [CSES - Forest Queries II](https://cses.fi/problemset/task/1739/)
* [Latin American Regionals 2017 - Fundraising](http://matcomgrader.com/problem/9346/fundraising/)

## অন্যান্য উৎস

* [Fenwick tree on Wikipedia](http://en.wikipedia.org/wiki/Fenwick_tree)
* [Binary indexed trees tutorial on TopCoder](https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/)
* [Range updates and queries ](https://programmingcontests.quora.com/Tutorial-Range-Updates-in-Fenwick-Tree)
