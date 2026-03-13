---
title: "ডিভাইড অ্যান্ড কনকার ডিপি"
tags: 
weight: 10
---
# ডিভাইড অ্যান্ড কনকার ডিপি

ডিভাইড অ্যান্ড কনকার হলো একটি ডায়নামিক প্রোগ্রামিং অপটিমাইজেশন।

### পূর্বশর্ত
কিছু ডায়নামিক প্রোগ্রামিং সমস্যায় এই ধরনের রিকারেন্স থাকে:

$$
dp(i, j) = \min_{0 \leq k \leq j} \\{ dp(i - 1, k - 1) + C(k, j) \\}
$$

যেখানে $C(k, j)$ একটি কস্ট ফাংশন এবং $dp(i, j) = 0$ যখন $j \lt 0$।

ধরো $0 \leq i \lt m$ এবং $0 \leq j \lt n$, এবং $C$ মূল্যায়ন করতে $O(1)$ সময় লাগে। তাহলে উপরের রিকারেন্সের সরাসরি মূল্যায়ন $O(m n^2)$। $m \times n$ টা স্টেট আছে, এবং প্রতিটি স্টেটের জন্য $n$টা ট্রানজিশন।

ধরো $opt(i, j)$ হলো সেই $k$-এর মান যেটা উপরের রাশি সর্বনিম্ন করে। ধরে নিচ্ছি কস্ট ফাংশন চতুর্ভুজ অসমতা (quadrangle inequality) পূরণ করে, তাহলে আমরা দেখাতে পারি যে সব $i, j$-এর জন্য $opt(i, j) \leq opt(i, j + 1)$। এটা _মনোটনিসিটি শর্ত_ নামে পরিচিত।
তখন, আমরা ডিভাইড অ্যান্ড কনকার ডিপি প্রয়োগ করতে পারি। একটা নির্দিষ্ট $i$-এর জন্য অপটিমাল "স্প্লিটিং পয়েন্ট" $j$ বাড়ার সাথে বাড়ে।

এটা আমাদের সব স্টেট আরও দক্ষতার সাথে সমাধান করতে দেয়। ধরো আমরা কোনো নির্দিষ্ট $i$ এবং $j$-এর জন্য $opt(i, j)$ বের করি। তাহলে যেকোনো $j' < j$-এর জন্য আমরা জানি যে $opt(i, j') \leq opt(i, j)$।
তারমানে $opt(i, j')$ বের করার সময়, আমাদের ততগুলো স্প্লিটিং পয়েন্ট কনসিডার করতে হবে না!

রানটাইম সর্বনিম্ন করতে, আমরা ডিভাইড অ্যান্ড কনকারের পেছনের ধারণা প্রয়োগ করি। প্রথমে, $opt(i, n / 2)$ বের করি। তারপর, $opt(i, n / 4)$ বের করি, জেনে যে এটা $opt(i, n / 2)$-এর চেয়ে কম বা সমান এবং $opt(i, 3 n / 4)$ জেনে যে এটা $opt(i, n / 2)$-এর চেয়ে বেশি বা সমান। রিকার্সিভভাবে $opt$-এর নিম্ন ও ঊর্ধ্ব সীমা ট্র্যাক করে, আমরা $O(m n \log n)$ রানটাইমে পৌঁছাই।
ইমপ্লিমেন্টেশনের বিস্তারিতের জন্য নিচের কোড দেখো।

ডিভাইড অ্যান্ড কনকারের কমপ্লেক্সিটি (complexity) প্রুফ করতে, প্রথমে লক্ষ্য করো রিকার্সনে $O(\log{n})$ লেভেল আছে। আমরা দাবি করি প্রতিটা লেভেলে $O(n)$ ধাপ হচ্ছে। $k$-তম লেভেলে $\text{opt}$ ইন্টারভালগুলোর (কোডে $optl$ এবং $optr$ দ্বারা চিহ্নিত) মোট দৈর্ঘ্য $S_k$ হোক, এবং লক্ষ্য করো লেভেল $k$-তে দৈর্ঘ্য $x$-এর একটা ইন্টারভাল স্প্লিট হলে, তাহলে ইন্টারভাল(গুলো)র মোট দৈর্ঘ্য সর্বোচ্চ $x + 1$। এছাড়া, লেভেল $k$-তে সর্বোচ্চ $2^k$ স্প্লিট হয়, তাই $S_{k + 1} \leq S_k + 2^k$। $S_0 = n$ দিয়ে ইন্ডাকশন (induction) প্রয়োগ করলে প্রতিটা লেভেল $k$-এর জন্য পাই,

$$
S_k < n + 2^k \in O(n).
$$

তাই, প্রতিটি ডিভাইড অ্যান্ড কনকারের কমপ্লেক্সিটি $O(n\log{n})$, এবং সম্পূর্ণ ডিপি গণনার কমপ্লেক্সিটি $O(mn\log{n})$।

## জেনেরিক ইমপ্লিমেন্টেশন

যদিও ইমপ্লিমেন্টেশন সমস্যা অনুযায়ী ভিন্ন হয়, এখানে একটা মোটামুটি জেনেরিক টেমপ্লেট দেওয়া হলো।
`compute` ফাংশনটা `dp_cur`-এর একটা সারি $i$ বের করে, আগের সারি $i-1$ `dp_before` দেওয়া থাকলে।
এটাকে `compute(0, n-1, 0, n-1)` দিয়ে কল করতে হবে। `solve` ফাংশনটা `m` সারি বের করে এবং ফলাফল রিটার্ন করে।

```cpp
int m, n;
vector<long long> dp_before, dp_cur;

long long C(int i, int j);

// compute dp_cur[l], ... dp_cur[r] (inclusive)
void compute(int l, int r, int optl, int optr) {
    if (l > r)
        return;

    int mid = (l + r) >> 1;
    pair<long long, int> best = {LLONG_MAX, -1};

    for (int k = optl; k <= min(mid, optr); k++) {
        best = min(best, {(k ? dp_before[k - 1] : 0) + C(k, mid), k});
    }

    dp_cur[mid] = best.first;
    int opt = best.second;

    compute(l, mid - 1, optl, opt);
    compute(mid + 1, r, opt, optr);
}

long long solve() {
    dp_before.assign(n,0);
    dp_cur.assign(n,0);

    for (int i = 0; i < n; i++)
        dp_before[i] = C(0, i);

    for (int i = 1; i < m; i++) {
        compute(0, n - 1, 0, n - 1);
        dp_before = dp_cur;
    }

    return dp_before[n - 1];
}
```

### লক্ষণীয় বিষয়

ডিভাইড অ্যান্ড কনকার ডিপি সমস্যার সবচেয়ে বড় কঠিনতা হলো $opt$-এর মনোটনিসিটি প্রুফ করা। একটা বিশেষ কেস যেখানে এটা সত্য, সেটা হলো যখন কস্ট ফাংশন চতুর্ভুজ অসমতা পূরণ করে, মানে সব $a \leq b \leq c \leq d$-এর জন্য $C(a, c) + C(b, d) \leq C(a, d) + C(b, c)$।
অনেক ডিভাইড অ্যান্ড কনকার ডিপি সমস্যা কনভেক্স হাল ট্রিক দিয়েও সমাধান করা যায় বা উল্টোটাও। দুটোই জানা এবং বোঝা দরকারি!

## অনুশীলন সমস্যা
- [AtCoder - Yakiniku Restaurants](https://atcoder.jp/contests/arc067/tasks/arc067_d)
- [CodeForces - Ciel and Gondolas](https://codeforces.com/contest/321/problem/E) (I/O-তে সতর্ক থেকো!)
- [CodeForces - Levels And Regions](https://codeforces.com/problemset/problem/673/E)
- [CodeForces - Partition Game](https://codeforces.com/contest/1527/problem/E)
- [CodeForces - The Bakery](https://codeforces.com/problemset/problem/834/D)
- [CodeForces - Yet Another Minimization Problem](https://codeforces.com/contest/868/problem/F)
- [Codechef - CHEFAOR](https://www.codechef.com/problems/CHEFAOR)
- [CodeForces - GUARDS](https://codeforces.com/gym/103536/problem/A) (এই আর্টিকেলের ঠিক এই সমস্যা।)
- [Hackerrank - Guardians of the Lunatics](https://www.hackerrank.com/contests/ioi-2014-practice-contest-2/challenges/guardians-lunatics-ioi14)
- [Hackerrank - Mining](https://www.hackerrank.com/contests/world-codesprint-5/challenges/mining)
- [Kattis - Money (ACM ICPC World Finals 2017)](https://open.kattis.com/problems/money)
- [SPOJ - ADAMOLD](https://www.spoj.com/problems/ADAMOLD/)
- [SPOJ - LARMY](https://www.spoj.com/problems/LARMY/)
- [SPOJ - NKLEAVES](https://www.spoj.com/problems/NKLEAVES/)
- [Timus - Bicolored Horses](https://acm.timus.ru/problem.aspx?space=1&num=1167)
- [USACO - Circular Barn](https://usaco.org/index.php?page=viewproblem2&cpid=626)
- [UVA - Arranging Heaps](https://onlinejudge.org/external/125/12524.pdf)
- [UVA - Naming Babies](https://onlinejudge.org/external/125/12594.pdf)



## রেফারেন্স
- [Quora Answer by Michael Levin](https://www.quora.com/What-is-divide-and-conquer-optimization-in-dynamic-programming)
- [Video Tutorial by "Sothe" the Algorithm Wolf](https://www.youtube.com/watch?v=wLXEWuDWnzI)
