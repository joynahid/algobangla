---
title: "ফেনউইক ট্রি"
tags: 
weight: 20
---
# ফেনউইক ট্রি

ফেনউইক ট্রি (Fenwick Tree) বা বাইনারি ইনডেক্সড ট্রি (BIT) হলো এমন একটা ডাটা স্ট্রাকচার যেটা দিয়ে তুমি একটা অ্যারের উপর দুই ধরনের কাজ খুব দ্রুত করতে পারবে:

* কোনো রেঞ্জ $[l, r]$-এ উপাদানগুলোর যোগফল (বা অন্য কোনো অপারেশন যেমন $A_l * A_{l+1} * \dots * A_r$) $O(\log N)$ সময়ে বের করা
* অ্যারের যেকোনো একটা উপাদানের মান $O(\log N)$ সময়ে আপডেট করা
* মেমরি লাগে মাত্র $O(N)$ — মানে অ্যারের সমান
* কোড করাও অনেক সহজ, এমনকি 2D অ্যারের জন্যও

সবচেয়ে কমন ব্যবহার হলো _রেঞ্জ সাম কুয়েরি_।
ধরো তুমি যোগ অপারেশন নিয়ে কাজ করছ, মানে $f(x,y) = x + y$। তাহলে $A_l * A_{l+1} * \dots * A_r = A_l + A_{l+1} + \dots + A_{r}$।

এটা প্রথম দেখানো হয়েছিল "A new data structure for cumulative frequency tables" (Peter M. Fenwick, 1994) পেপারে।

## বর্ণনা

### ভূমিকা

সহজ করার জন্য ধরি আমরা যোগ অপারেশন নিয়ে কাজ করছি, মানে $f(x,y) = x + y$।

ধরো তোমাকে একটা পূর্ণসংখ্যা অ্যারে দেয়া হলো, $A[0 \dots N-1]$।
(লক্ষ্য কর আমরা 0 থেকে ইনডেক্সিং শুরু করছি।)
ফেনউইক ট্রি আসলে আরেকটা অ্যারে, $T[0 \dots N-1]$, যেখানে প্রতিটা উপাদান $A$ এর কোনো রেঞ্জ $[g(i), i]$-এ উপাদানগুলোর যোগফল রাখে:

$$T_i = \sum_{j = g(i)}^{i}{A_j}$$

এখানে $g$ এমন একটা ফাংশন যেটা $0 \le g(i) \le i$ শর্ত মানে।
$g$ কীভাবে কাজ করে সেটা একটু পরেই দেখাচ্ছি।

এই ডাটা স্ট্রাকচারকে ট্রি বলে কারণ এটাকে ট্রি আকারে দেখানো যায়, তবে আসল ট্রি এর মত নোড আর এজ দিয়ে বানানোর দরকার নেই।
সব কুয়েরি হ্যান্ডেল করতে শুধু $T$ অ্যারেটাই যথেষ্ট।

**লক্ষ্য কর:** এখানে আমরা 0-based ইনডেক্সিং ব্যবহার করছি।
অনেকে 1-based ইনডেক্সিং পছন্দ করে।
তাই ইমপ্লিমেন্টেশন সেকশনে তুমি 1-based ইনডেক্সিং এর একটা বিকল্প ইমপ্লিমেন্টেশনও পাবে।
দুইটার টাইম আর মেমরি কমপ্লেক্সিটি একই।

এবার উপরের দুইটা অপারেশনের জন্য সিউডো-কোড দেখি।
নিচে $A$ এর $[0, r]$ রেঞ্জের যোগফল বের করা আর কোনো উপাদান $A_i$ আপডেট করার কোড দেয়া হলো:

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

`sum` ফাংশন এভাবে কাজ করে:

1. প্রথমে $[g(r), r]$ রেঞ্জের যোগফল (মানে $T[r]$) `result`-এ যোগ করে।
2. তারপর $[g(g(r)-1), g(r)-1]$ রেঞ্জে "জাম্প" করে আর সেই রেঞ্জের যোগফলও `result`-এ যোগ করে।
3. এভাবে চলতে থাকে যতক্ষণ না $[0, g(g( \dots g(r)-1 \dots -1)-1)]$ থেকে $[g(-1), -1]$-এ পৌঁছায়। তখন `sum` ফাংশন থেমে যায়।

`increase` ফাংশনও একইভাবে কাজ করে, তবে বড় ইনডেক্সের দিকে জাম্প করে:

1. $[g(j), j]$ আকারের প্রতিটা রেঞ্জ যেখানে $g(j) \le i \le j$, সেটার যোগফল `delta` দিয়ে বাড়ে। মানে `t[j] += delta`।
তারমানে $T$ এর যে যে উপাদান $A_i$ এর রেঞ্জে পড়ে, সেগুলো সব আপডেট হয়।

`sum` আর `increase` দুইটারই কমপ্লেক্সিটি নির্ভর করে $g$ ফাংশনের উপর।
$g$ বেছে নেয়ার অনেক উপায় আছে যেখানে সব $i$ এর জন্য $0 \le g(i) \le i$ হয়।
যেমন $g(i) = i$ নিলে $T = A$ হয়ে যায় — এক্ষেত্রে যোগফল কুয়েরি স্লো হবে।
আবার $g(i) = 0$ নিলে এটা প্রিফিক্স সাম অ্যারে হয়ে যায় — $[0, i]$ রেঞ্জের যোগফল $O(1)$-এ পাবে, কিন্তু আপডেটে $O(n)$ লাগবে।
ফেনউইক ট্রির চালাকিটা হলো $g$ এমনভাবে ডিফাইন করা যেন দুইটা অপারেশনই $O(\log N)$-এ হয়।

### $g(i)$ এর সংজ্ঞা { data-toc-label='$g(i)$ এর সংজ্ঞা' }

$g(i)$ বের করাটা খুব সিম্পল:
$i$ এর বাইনারি রিপ্রেজেন্টেশনে শেষের দিকের সব $1$ বিটকে $0$ বানিয়ে দাও।

সোজা কথায়, $i$ এর বাইনারিতে সবচেয়ে ডানের বিট যদি $0$ হয়, তাহলে $g(i) = i$।
আর যদি $1$ হয়, তাহলে সেই $1$ সহ ডানদিকের সব consecutive $1$ গুলো ফ্লিপ করে $0$ বানাও।

উদাহরণ দেখো

$$\begin{align}
g(11) = g(1011_2) = 1000_2 &= 8 \\\\
g(12) = g(1100_2) = 1100_2 &= 12 \\\\
g(13) = g(1101_2) = 1100_2 &= 12 \\\\
g(14) = g(1110_2) = 1110_2 &= 14 \\\\
g(15) = g(1111_2) = 0000_2 &= 0 \\\\
\end{align}$$

এই কাজটা বিটওয়াইজ অপারেশন দিয়ে খুব সহজে করা যায়:

$$g(i) = i ~\&~ (i+1),$$

এখানে $\&$ হলো বিটওয়াইজ AND অপারেটর। একটু ভেবে দেখলে বুঝবে এটা উপরের অপারেশনটাই করে।

এবার সব $j$ বের করতে হবে যেখানে $g(j) \le i \le j$।

$i$ থেকে শুরু করে প্রতিবার শেষের আনসেট বিট ফ্লিপ করলেই এরকম সব $j$ পাওয়া যায়।
এই অপারেশনটাকে $h(j)$ বলি।
যেমন $i = 10$ এর জন্য:

$$\begin{align}
10 &= 0001010_2 \\\\
h(10) = 11 &= 0001011_2 \\\\
h(11) = 15 &= 0001111_2 \\\\
h(15) = 31 &= 0011111_2 \\\\
h(31) = 63 &= 0111111_2 \\\\
\vdots &
\end{align}$$

মজার ব্যাপার হলো, $h$-ও বিটওয়াইজ অপারেশন দিয়ে বের করা যায়:

$$h(j) = j ~|~ (j+1),$$

এখানে $|$ হলো বিটওয়াইজ OR অপারেটর।

নিচের ছবিতে ফেনউইক ট্রিকে একটা ট্রি আকারে দেখানো হয়েছে।
প্রতিটা নোড তার কভার করা রেঞ্জ দেখাচ্ছে।

<div style="text-align: center;">
  <img src="/images/data_structures/binary_indexed_tree.png" alt="Binary Indexed Tree">
</div>

## ইমপ্লিমেন্টেশন

### 1D অ্যারেতে যোগফল বের করা

এখানে যোগফল কুয়েরি আর পয়েন্ট আপডেটের জন্য ফেনউইক ট্রির ইমপ্লিমেন্টেশন দেয়া হলো।

সাধারণ ফেনউইক ট্রি শুধু $[0, r]$ টাইপের কুয়েরি `sum(int r)` দিয়ে উত্তর দিতে পারে। কিন্তু $[l, r]$ রেঞ্জের উত্তর চাইলে $[0, r]$ আর $[0, l-1]$ — এই দুইটা সাম বের করে বিয়োগ করলেই হয়।
এটাই `sum(int l, int r)` মেথডে করা হচ্ছে।

এই ইমপ্লিমেন্টেশনে দুইটা কনস্ট্রাক্টর আছে।
তুমি চাইলে সব 0 দিয়ে ইনিশিয়ালাইজ করতে পারো, অথবা একটা অ্যারে থেকে সরাসরি ফেনউইক ট্রি বানাতে পারো।


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

উপরের ইমপ্লিমেন্টেশনে কনস্ট্রাকশনে $O(N \log N)$ সময় লাগে।
এটা $O(N)$-এ করা সম্ভব।

আইডিয়াটা হলো, ইনডেক্স $i$ এর ভ্যালু $a[i]$ শুধু $bit[i]$-তে রাখা রেঞ্জেই contribute করে না, ইনডেক্স $i | (i + 1)$ এর রেঞ্জেও contribute করে।
তাই একটার পর একটা যোগ করলে, তোমাকে শুধু বর্তমান সাম পরের রেঞ্জে পাস করতে হবে। সেখান থেকে আবার পরের রেঞ্জে যাবে — এভাবে চলতে থাকবে।

```cpp
FenwickTree(vector<int> const &a) : FenwickTree(a.size()){
    for (int i = 0; i < n; i++) {
        bit[i] += a[i];
        int r = i | (i + 1);
        if (r < n) bit[r] += bit[i];
    }
}
```

### 1D অ্যারেতে $[0, r]$ এর মিনিমাম বের করা { data-toc-label='একমাত্রিক অ্যারেতে $[0, r]$ এর সর্বনিম্ন খোঁজা' }

ফেনউইক ট্রি দিয়ে $[l, r]$ রেঞ্জের মিনিমাম বের করার কোনো সহজ উপায় নেই — শুধু $[0, r]$ টাইপের কুয়েরি করা যায়।
এছাড়া প্রতিবার আপডেটে নতুন মান আগের মানের চেয়ে ছোট হতে হবে।
এই দুইটা সীমাবদ্ধতার কারণ হলো $min$ অপারেশন পূর্ণসংখ্যার উপর গ্রুপ তৈরি করে না, কারণ inverse element নেই।

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

মনে রাখো: যেকোনো RMQ আর যেকোনো আপডেট সাপোর্ট করে এমন ফেনউইক ট্রি বানানো সম্ভব।
[Efficient Range Minimum Queries using Binary Indexed Trees](http://ioinformatics.org/oi/pdf/v9_2015_39_44.pdf) পেপারে এরকম একটা পদ্ধতি দেখানো হয়েছে।
তবে সেখানে ডাটার উপর আরেকটা BIT রাখতে হয়, যেটার স্ট্রাকচার একটু আলাদা। কারণ একটা ট্রি দিয়ে অ্যারের সব ভ্যালু রাখা যায় না।
সাধারণ সাম ইমপ্লিমেন্টেশনের তুলনায় এটা বানানোও অনেক কঠিন।

### 2D অ্যারেতে যোগফল বের করা

আগেই বলেছিলাম, মাল্টিডাইমেনশনাল অ্যারের জন্য ফেনউইক ট্রি ইমপ্লিমেন্ট করা অনেক সহজ।

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

### 1-based ইনডেক্সিং পদ্ধতি

এই পদ্ধতিতে $T[]$ আর $g()$ এর ডেফিনিশন একটু পাল্টে যায়।
এখানে $T[i]$ রাখবে $[g(i)+1; i]$ রেঞ্জের যোগফল।
এতে ইমপ্লিমেন্টেশন একটু বদলায়, আর $g(i)$ এর ডেফিনিশনও সুন্দর থাকে:

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

$g(i)$ বের করতে হলে:
$i$ এর বাইনারি রিপ্রেজেন্টেশনে সবচেয়ে ডানের সেট বিট ($1$) টগল করো।

$$\begin{align}
g(7) = g(111_2) = 110_2 &= 6 \\\\
g(6) = g(110_2) = 100_2 &= 4 \\\\
g(4) = g(100_2) = 000_2 &= 0 \\\\
\end{align}$$

সবচেয়ে ডানের সেট বিট বের হয় $i ~\&~ (-i)$ দিয়ে, তাই:

$$g(i) = i - (i ~\&~ (-i)).$$

আর $A[j]$ আপডেট করতে চাইলে $i,~ h(i),~ h(h(i)),~ \dots$ সিকোয়েন্সের সব $T[j]$ আপডেট করতে হবে, যেখানে:

$$h(i) = i + (i ~\&~ (-i)).$$

দেখো, এই পদ্ধতির সবচেয়ে বড় সুবিধা হলো বিটওয়াইজ অপারেশনগুলো একে অপরকে চমৎকারভাবে complement করে।

নিচের ইমপ্লিমেন্টেশন বাইরে থেকে আগের গুলোর মতোই ব্যবহার করা যায়, তবে ভেতরে 1-based ইনডেক্সিং চলে।

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

ফেনউইক ট্রি দিয়ে এই ধরনের রেঞ্জ অপারেশন করা যায়:

১. পয়েন্ট আপডেট ও রেঞ্জ কুয়েরি
২. রেঞ্জ আপডেট ও পয়েন্ট কুয়েরি
৩. রেঞ্জ আপডেট ও রেঞ্জ কুয়েরি

### ১. পয়েন্ট আপডেট ও রেঞ্জ কুয়েরি

এটাই উপরে দেখানো সাধারণ ফেনউইক ট্রি।

### ২. রেঞ্জ আপডেট ও পয়েন্ট কুয়েরি

একটা সিম্পল ট্রিক দিয়ে উল্টো কাজটাও করা যায় — রেঞ্জে ভ্যালু বাড়ানো আর একটা পয়েন্টের ভ্যালু জানা।

ধরো ফেনউইক ট্রি সব 0 দিয়ে ইনিশিয়ালাইজ করা।
এখন তুমি $[l, r]$ রেঞ্জে $x$ যোগ করতে চাও।
দুইটা পয়েন্ট আপডেট করলেই হবে: `add(l, x)` আর `add(r+1, -x)`।

$A[i]$ এর মান জানতে চাইলে শুধু প্রিফিক্স সাম বের করো।
কেন কাজ করে? একটু ভেবে দেখো।
যদি $i < l$ হয়, তাহলে দুইটা আপডেটই কুয়েরিতে ধরবে না, সাম $0$ পাবে।
যদি $i \in [l, r]$ হয়, তাহলে শুধু প্রথম আপডেট ধরবে, উত্তর $x$ পাবে।
আর যদি $i > r$ হয়, তাহলে দ্বিতীয় আপডেট প্রথমটাকে ক্যান্সেল করে দেবে।

নিচের ইমপ্লিমেন্টেশন 1-based ইনডেক্সিং ব্যবহার করে।

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

মনে রাখো: `range_add(i, i, val)` দিয়ে একটা পয়েন্ট $A[i]$-ও আপডেট করা যায়।

### ৩. রেঞ্জ আপডেট ও রেঞ্জ কুয়েরি

রেঞ্জ আপডেট আর রেঞ্জ কুয়েরি দুইটাই সাপোর্ট করতে আমরা দুইটা BIT ব্যবহার করবো — $B_1[]$ আর $B_2[]$, দুইটাই 0 দিয়ে ইনিশিয়ালাইজ করা।

ধরো $[l, r]$ রেঞ্জে $x$ যোগ করতে চাও।
আগের মতোই $B_1$ এ দুইটা পয়েন্ট আপডেট করো: `add(B1, l, x)` আর `add(B1, r+1, -x)`।
$B_2$-ও আপডেট করতে হবে — কেন লাগে সেটা একটু পরেই দেখাচ্ছি।

```python
def range_add(l, r, x):
    add(B1, l, x)
    add(B1, r+1, -x)
    add(B2, l, x*(l-1))
    add(B2, r+1, -x*r))
```
রেঞ্জ আপডেট $(l, r, x)$ এর পর রেঞ্জ সাম কুয়েরির উত্তর হওয়া উচিত:

$$
sum[0, i]=
\begin{cases}
0 & i < l \\\\
x \cdot (i-(l-1)) & l \le i \le r \\\\
x \cdot (r-l+1) & i > r \\\\
\end{cases}
$$

রেঞ্জ সামকে দুইটা টার্মের পার্থক্য হিসেবে লেখা যায় — প্রথমটার জন্য $B_1$ আর দ্বিতীয়টার জন্য $B_2$ ব্যবহার করি।
এই পার্থক্য $[0, i]$ এর প্রিফিক্স সাম দেয়।

$$\begin{align}
sum[0, i] &= sum(B_1, i) \cdot i - sum(B_2, i) \\\\
&= \begin{cases}
0 \cdot i - 0 & i < l\\\\
x \cdot i - x \cdot (l-1) & l \le i \le r \\\\
0 \cdot i - (x \cdot (l-1) - x \cdot r) & i > r \\\\
\end{cases}
\end{align}
$$

শেষ এক্সপ্রেশনটা ঠিক আমাদের দরকারি ভ্যালু দেয়।
তারমানে $B_1[i]\times i$ গুণ করার সময় যে extra টার্ম আসে, সেটা কাটার জন্যই $B_2$ ব্যবহার করছি।

$l-1$ আর $r$ এর প্রিফিক্স সাম বের করে বিয়োগ করলেই যেকোনো রেঞ্জ সাম পাওয়া যায়।

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
