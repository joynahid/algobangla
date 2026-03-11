---
title: "স্পার্স টেবিল"
tags: 
weight: 20
---
# স্পার্স টেবিল

স্পার্স টেবিল হলো একটি ডেটা স্ট্রাকচার, যা রেঞ্জ কোয়েরির উত্তর দিতে পারে।
এটি বেশিরভাগ রেঞ্জ কোয়েরি $O(\log n)$-এ উত্তর দিতে পারে, কিন্তু এর প্রকৃত শক্তি হলো রেঞ্জ মিনিমাম কোয়েরি (বা সমতুল্য রেঞ্জ ম্যাক্সিমাম কোয়েরি) উত্তর দেওয়া।
সেই কোয়েরিগুলোর জন্য এটি $O(1)$ সময়ে উত্তর গণনা করতে পারে।

এই ডেটা স্ট্রাকচারের একমাত্র অসুবিধা হলো, এটি শুধু _অপরিবর্তনীয়_ অ্যারেতে ব্যবহার করা যায়।
অর্থাৎ, দুটি কোয়েরির মধ্যে অ্যারে পরিবর্তন করা যাবে না।
যদি অ্যারের কোনো উপাদান পরিবর্তন হয়, সম্পূর্ণ ডেটা স্ট্রাকচার পুনরায় গণনা করতে হবে।

## অন্তর্দৃষ্টি

যেকোনো অ-ঋণাত্মক সংখ্যা দুই-এর ক্রমহ্রাসমান ঘাতের যোগফল হিসেবে অনন্যভাবে উপস্থাপন করা যায়।
এটি মূলত একটি সংখ্যার বাইনারি উপস্থাপনার একটি রূপ।
যেমন $13 = (1101)_2 = 8 + 4 + 1$।
একটি সংখ্যা $x$-এর জন্য সর্বোচ্চ $\lceil \log_2 x \rceil$ পদ থাকতে পারে।

একই যুক্তিতে যেকোনো ব্যবধান দুই-এর ক্রমহ্রাসমান ঘাত দৈর্ঘ্যের ব্যবধানের ইউনিয়ন হিসেবে অনন্যভাবে উপস্থাপন করা যায়।
যেমন $[2, 14] = [2, 9] \cup [10, 13] \cup [14, 14]$, যেখানে সম্পূর্ণ ব্যবধানের দৈর্ঘ্য ১৩, এবং পৃথক ব্যবধানের দৈর্ঘ্য যথাক্রমে ৮, ৪ এবং ১।
এবং এখানেও ইউনিয়নে সর্বোচ্চ $\lceil \log_2(\text{interval length}) \rceil$ ব্যবধান থাকে।

স্পার্স টেবিলের মূল ধারণা হলো দুই-এর ঘাত দৈর্ঘ্যের সব রেঞ্জ কোয়েরির উত্তর আগে থেকে গণনা করে রাখা।
পরে একটি ভিন্ন রেঞ্জ কোয়েরি উত্তর দেওয়া যায় রেঞ্জটিকে দুই-এর ঘাত দৈর্ঘ্যের রেঞ্জে ভাগ করে, আগে থেকে গণনা করা উত্তর দেখে, এবং সেগুলো সংযুক্ত করে সম্পূর্ণ উত্তর পেতে।

## প্রি-কম্পিউটেশন

আমরা আগে থেকে গণনা করা কোয়েরির উত্তর সংরক্ষণ করতে একটি ২-মাত্রিক অ্যারে ব্যবহার করব।
$\text{st}[i][j]$ দৈর্ঘ্য $2^i$-এর রেঞ্জ $[j, j + 2^i - 1]$-এর উত্তর সংরক্ষণ করবে।
২-মাত্রিক অ্যারের আকার হবে $(K + 1) \times \text{MAXN}$, যেখানে $\text{MAXN}$ সবচেয়ে বড় সম্ভাব্য অ্যারে দৈর্ঘ্য।
$\text{K}$-কে $\text{K} \ge \lfloor \log_2 \text{MAXN} \rfloor$ পূরণ করতে হবে, কারণ $2^{\lfloor \log_2 \text{MAXN} \rfloor}$ হলো আমাদের সমর্থন করা দরকার এমন সবচেয়ে বড় দুই-এর ঘাত রেঞ্জ।
যুক্তিসঙ্গত দৈর্ঘ্যের ($\le 10^7$ উপাদান) অ্যারের জন্য, $K = 25$ একটি ভালো মান।

$\text{MAXN}$ মাত্রাটি দ্বিতীয় যেন (ক্যাশে-ফ্রেন্ডলি) পরপর মেমরি অ্যাক্সেস হয়।

```cpp
int st[K + 1][MAXN];
```

যেহেতু দৈর্ঘ্য $2^i$-এর রেঞ্জ $[j, j + 2^i - 1]$ সুন্দরভাবে $[j, j + 2^{i - 1} - 1]$ এবং $[j + 2^{i - 1}, j + 2^i - 1]$ রেঞ্জে ভাগ হয়, দুটোই দৈর্ঘ্য $2^{i - 1}$, আমরা ডায়নামিক প্রোগ্রামিং ব্যবহার করে দক্ষতার সাথে টেবিল তৈরি করতে পারি:

```cpp
std::copy(array.begin(), array.end(), st[0]);

for (int i = 1; i <= K; i++)
    for (int j = 0; j + (1 << i) <= N; j++)
        st[i][j] = f(st[i - 1][j], st[i - 1][j + (1 << (i - 1))]);
```

$f$ ফাংশন কোয়েরির ধরনের উপর নির্ভর করবে।
রেঞ্জ সাম কোয়েরির জন্য এটি যোগফল গণনা করবে, রেঞ্জ মিনিমাম কোয়েরির জন্য সর্বনিম্ন গণনা করবে।

প্রি-কম্পিউটেশনের টাইম কমপ্লেক্সিটি $O(\text{N} \log \text{N})$।

## রেঞ্জ সাম কোয়েরি

এই ধরনের কোয়েরির জন্য, আমরা একটি রেঞ্জের সব মানের যোগফল খুঁজতে চাই।
তাই $f$ ফাংশনের স্বাভাবিক সংজ্ঞা হলো $f(x, y) = x + y$।
আমরা ডেটা স্ট্রাকচারটি এভাবে তৈরি করতে পারি:

```cpp
long long st[K + 1][MAXN];

std::copy(array.begin(), array.end(), st[0]);

for (int i = 1; i <= K; i++)
    for (int j = 0; j + (1 << i) <= N; j++)
        st[i][j] = st[i - 1][j] + st[i - 1][j + (1 << (i - 1))];
```

$[L, R]$ রেঞ্জের সাম কোয়েরি উত্তর দিতে, আমরা সব দুই-এর ঘাতে ইটারেট করি, সবচেয়ে বড় থেকে শুরু করে।
যখনই একটি দুই-এর ঘাত $2^i$ রেঞ্জের দৈর্ঘ্যের ($= R - L + 1$) চেয়ে ছোট বা সমান, আমরা রেঞ্জের $[L, L + 2^i - 1]$ প্রথম অংশ প্রক্রিয়া করি এবং বাকি রেঞ্জ $[L + 2^i, R]$ নিয়ে চলতে থাকি।

```cpp
long long sum = 0;
for (int i = K; i >= 0; i--) {
    if ((1 << i) <= R - L + 1) {
        sum += st[i][L];
        L += 1 << i;
    }
}
```

রেঞ্জ সাম কোয়েরির টাইম কমপ্লেক্সিটি $O(K) = O(\log \text{MAXN})$।

## রেঞ্জ মিনিমাম কোয়েরি (RMQ)

এই কোয়েরিগুলোতেই স্পার্স টেবিল সবচেয়ে ভালো কাজ করে।
রেঞ্জের সর্বনিম্ন গণনা করার সময়, রেঞ্জের কোনো মান একবার বা দুইবার প্রক্রিয়া করলে কোনো পার্থক্য নেই।
তাই রেঞ্জকে একাধিক রেঞ্জে ভাগ করার বদলে, আমরা রেঞ্জটিকে শুধু দুই-এর ঘাত দৈর্ঘ্যের দুটি ওভারল্যাপিং রেঞ্জে ভাগ করতে পারি।
যেমন, $[1, 6]$ রেঞ্জটিকে $[1, 4]$ এবং $[3, 6]$ রেঞ্জে ভাগ করা যায়।
$[1, 6]$-এর রেঞ্জ মিনিমাম স্পষ্টতই $[1, 4]$-এর রেঞ্জ মিনিমাম এবং $[3, 6]$-এর রেঞ্জ মিনিমামের সর্বনিম্ন।
তাই $[L, R]$ রেঞ্জের সর্বনিম্ন গণনা করা যায়:

$$\min(\text{st}[i][L], \text{st}[i][R - 2^i + 1]) \quad \text{ where } i = \log_2(R - L + 1)$$

এর জন্য আমাদের $\log_2(R - L + 1)$ দ্রুত গণনা করতে পারতে হবে।
আপনি সব লগারিদম আগে থেকে গণনা করে রেখে এটি করতে পারেন:

```cpp
int lg[MAXN+1];
lg[1] = 0;
for (int i = 2; i <= MAXN; i++)
    lg[i] = lg[i/2] + 1;
```
বিকল্পভাবে, ধ্রুব স্থান ও সময়ে log তাৎক্ষণিকভাবে গণনা করা যায়:
```c++
// C++20
#include <bit>
int log2_floor(unsigned long i) {
    return std::bit_width(i) - 1;
}

// pre C++20
int log2_floor(unsigned long long i) {
    return i ? __builtin_clzll(1) - __builtin_clzll(i) : -1;
}
```
[এই বেঞ্চমার্ক](https://quick-bench.com/q/Zghbdj_TEkmw4XG2nqOpD3tsJ8U) দেখায় যে `lg` অ্যারে ব্যবহার ক্যাশে মিসের কারণে ধীর।

এরপর আমাদের স্পার্স টেবিল স্ট্রাকচার আগে থেকে গণনা করতে হবে। এবার আমরা $f$-কে $f(x, y) = \min(x, y)$ দিয়ে সংজ্ঞায়িত করি।

```cpp
int st[K + 1][MAXN];

std::copy(array.begin(), array.end(), st[0]);

for (int i = 1; i <= K; i++)
    for (int j = 0; j + (1 << i) <= N; j++)
        st[i][j] = min(st[i - 1][j], st[i - 1][j + (1 << (i - 1))]);
```

এবং $[L, R]$ রেঞ্জের সর্বনিম্ন গণনা করা যায়:

```cpp
int i = lg[R - L + 1];
int minimum = min(st[i][L], st[i][R - (1 << i) + 1]);
```

রেঞ্জ মিনিমাম কোয়েরির টাইম কমপ্লেক্সিটি $O(1)$।

## আরও ধরনের কোয়েরি সমর্থনকারী অনুরূপ ডেটা স্ট্রাকচার

আগের সেকশনে আলোচিত $O(1)$ পদ্ধতির একটি প্রধান দুর্বলতা হলো, এই পদ্ধতি শুধু [ইডেমপোটেন্ট ফাংশন](https://en.wikipedia.org/wiki/Idempotence)-এর কোয়েরি সমর্থন করে।
অর্থাৎ এটি রেঞ্জ মিনিমাম কোয়েরির জন্য দারুণ কাজ করে, কিন্তু এই পদ্ধতি দিয়ে রেঞ্জ সাম কোয়েরি উত্তর দেওয়া সম্ভব নয়।

অনুরূপ ডেটা স্ট্রাকচার আছে যা যেকোনো ধরনের অ্যাসোসিয়েটিভ ফাংশন পরিচালনা করতে পারে এবং $O(1)$-এ রেঞ্জ কোয়েরি উত্তর দিতে পারে।
একটির নাম [ডিসজয়েন্ট স্পার্স টেবিল](https://discuss.codechef.com/questions/117696/tutorial-disjoint-sparse-table)।
আরেকটি হলো [স্কোয়ার্ট ট্রি](sqrt-tree.md)।

## অনুশীলন সমস্যা

* [SPOJ - RMQSQ](http://www.spoj.com/problems/RMQSQ/)
* [SPOJ - THRBL](http://www.spoj.com/problems/THRBL/)
* [Codechef - MSTICK](https://www.codechef.com/problems/MSTICK)
* [Codechef - SEAD](https://www.codechef.com/problems/SEAD)
* [Codeforces - CGCDSSQ](http://codeforces.com/contest/475/problem/D)
* [Codeforces - R2D2 and Droid Army](http://codeforces.com/problemset/problem/514/D)
* [Codeforces - Maximum of Maximums of Minimums](http://codeforces.com/problemset/problem/872/B)
* [SPOJ - Miraculous](http://www.spoj.com/problems/TNVFC1M/)
* [DevSkill - Multiplication Interval (archived)](http://web.archive.org/web/20200922003506/https://devskill.com/CodingProblems/ViewProblem/19)
* [Codeforces - Animals and Puzzles](http://codeforces.com/contest/713/problem/D)
* [Codeforces - Trains and Statistics](http://codeforces.com/contest/675/problem/E)
* [SPOJ - Postering](http://www.spoj.com/problems/POSTERIN/)
* [SPOJ - Negative Score](http://www.spoj.com/problems/RPLN/)
* [SPOJ - A Famous City](http://www.spoj.com/problems/CITY2/)
* [SPOJ - Diferencija](http://www.spoj.com/problems/DIFERENC/)
* [Codeforces - Turn off the TV](http://codeforces.com/contest/863/problem/E)
* [Codeforces - Map](http://codeforces.com/contest/15/problem/D)
* [Codeforces - Awards for Contestants](http://codeforces.com/contest/873/problem/E)
* [Codeforces - Longest Regular Bracket Sequence](http://codeforces.com/contest/5/problem/C)
* [CSES - Static Range Minimum Queries](https://cses.fi/problemset/task/1647)
* [Codeforces - Array Stabilization (GCD version)](http://codeforces.com/problemset/problem/1547/F)
