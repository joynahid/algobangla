---
title: "অয়লারের টোশেন্ট ফাংশন"
tags: 
weight: 10
---
# অয়লারের টোশেন্ট ফাংশন

অয়লারের টোশেন্ট ফাংশন, যা **ফি-ফাংশন** $\phi (n)$ নামেও পরিচিত, ১ থেকে $n$ পর্যন্ত (১ ও $n$ সহ) $n$-এর সাথে সহমৌলিক এমন পূর্ণসংখ্যার সংখ্যা গণনা করে। দুটি সংখ্যা সহমৌলিক যদি তাদের গসাগু $1$ হয় ($1$-কে যেকোনো সংখ্যার সাথে সহমৌলিক ধরা হয়)।

প্রথম কয়েকটি ধনাত্মক পূর্ণসংখ্যার জন্য $\phi(n)$-এর মান এখানে দেওয়া হলো:

$$\begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
n & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20 & 21 \\\\ \hline
\phi(n) & 1 & 1 & 2 & 2 & 4 & 2 & 6 & 4 & 6 & 4 & 10 & 4 & 12 & 6 & 8 & 8 & 16 & 6 & 18 & 8 & 12 \\\\ \hline
\end{array}$$

## বৈশিষ্ট্যসমূহ

অয়লারের টোশেন্ট ফাংশনের নিম্নলিখিত বৈশিষ্ট্যগুলো যেকোনো সংখ্যার জন্য এটি গণনা করতে যথেষ্ট:

  - যদি $p$ একটি মৌলিক সংখ্যা হয়, তাহলে সকল $1 \le q < p$-এর জন্য $\gcd(p, q) = 1$। তাই:

$$\phi (p) = p - 1.$$

  - যদি $p$ একটি মৌলিক সংখ্যা হয় এবং $k \ge 1$ হয়, তাহলে ১ থেকে $p^k$-এর মধ্যে ঠিক $p^k / p$টি সংখ্যা $p$ দ্বারা বিভাজ্য।
    যা থেকে পাই:

$$\phi(p^k) = p^k - p^{k-1}.$$

  - যদি $a$ ও $b$ পরস্পর সহমৌলিক হয়, তাহলে:

    \[\phi(a b) = \phi(a) \cdot \phi(b).\]

    এই সম্পর্কটি তুচ্ছভাবে দেখা যায় না। এটি [চাইনিজ রিমেইন্ডার থিওরেম](chinese-remainder-theorem.md) থেকে অনুসৃত হয়। চাইনিজ রিমেইন্ডার থিওরেম নিশ্চিত করে যে, প্রতিটি $0 \le x < a$ এবং প্রতিটি $0 \le y < b$-এর জন্য, একটি অনন্য $0 \le z < a b$ বিদ্যমান যেখানে $z \equiv x \pmod{a}$ এবং $z \equiv y \pmod{b}$। দেখানো কঠিন নয় যে $z$, $a b$-এর সাথে সহমৌলিক যদি এবং কেবল যদি $x$, $a$-এর সাথে সহমৌলিক হয় এবং $y$, $b$-এর সাথে সহমৌলিক হয়। তাই $a b$-এর সাথে সহমৌলিক পূর্ণসংখ্যার সংখ্যা $a$ ও $b$-এর পরিমাণের গুণফলের সমান।

  - সাধারণভাবে, সহমৌলিক নয় এমন $a$ ও $b$-এর জন্য, সমীকরণ

    \[\phi(ab) = \phi(a) \cdot \phi(b) \cdot \dfrac{d}{\phi(d)}\]

    যেখানে $d = \gcd(a, b)$, এটি ধরে।

সুতরাং, প্রথম তিনটি বৈশিষ্ট্য ব্যবহার করে, আমরা $n$-এর উৎপাদক বিশ্লেষণ ($n$-কে তার মৌলিক গুণনীয়কের গুণফলে বিভাজন) এর মাধ্যমে $\phi(n)$ গণনা করতে পারি।
যদি $n = {p_1}^{a_1} \cdot {p_2}^{a_2} \cdots {p_k}^{a_k}$ হয়, যেখানে $p_i$ হলো $n$-এর মৌলিক গুণনীয়ক,

$$\begin{align}
\phi (n) &= \phi ({p_1}^{a_1}) \cdot \phi ({p_2}^{a_2}) \cdots  \phi ({p_k}^{a_k}) \\\\
&= \left({p_1}^{a_1} - {p_1}^{a_1 - 1}\right) \cdot \left({p_2}^{a_2} - {p_2}^{a_2 - 1}\right) \cdots \left({p_k}^{a_k} - {p_k}^{a_k - 1}\right) \\\\
&= p_1^{a_1} \cdot \left(1 - \frac{1}{p_1}\right) \cdot p_2^{a_2} \cdot \left(1 - \frac{1}{p_2}\right) \cdots p_k^{a_k} \cdot \left(1 - \frac{1}{p_k}\right) \\\\
&= n \cdot \left(1 - \frac{1}{p_1}\right) \cdot \left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_k}\right)
\end{align}$$

## ইমপ্লিমেন্টেশন

$O(\sqrt{n})$-এ উৎপাদক বিশ্লেষণ ব্যবহার করে একটি ইমপ্লিমেন্টেশন:

```cpp
int phi(int n) {
    int result = n;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0)
                n /= i;
            result -= result / i;
        }
    }
    if (n > 1)
        result -= result / n;
    return result;
}
```

## $1$ থেকে $n$ পর্যন্ত অয়লারের টোশেন্ট ফাংশন $O(n \log\log{n})$-এ { #etf_1_to_n data-toc-label="Euler totient function from 1 to n in <script type=\"math/tex\">O(n log log n)</script>" }

$1$ থেকে $n$-এর মধ্যে সকল সংখ্যার টোশেন্ট প্রয়োজন হলে, সকল $n$টি সংখ্যার উৎপাদক বিশ্লেষণ করা দক্ষ নয়।
আমরা [এরাটোস্থেনিসের সিভ](sieve-of-eratosthenes.md)-এর মতো একই ধারণা ব্যবহার করতে পারি।
এটি এখনও উপরে দেখানো বৈশিষ্ট্যের উপর ভিত্তি করে, তবে প্রতিটি সংখ্যার জন্য প্রতিটি মৌলিক গুণনীয়কের জন্য অস্থায়ী ফলাফল আপডেট করার বদলে, আমরা সকল মৌলিক সংখ্যা খুঁজে বের করি এবং প্রতিটির জন্য সেই মৌলিক সংখ্যা দ্বারা বিভাজ্য সকল সংখ্যার অস্থায়ী ফলাফল আপডেট করি।

যেহেতু এই পদ্ধতিটি এরাটোস্থেনিসের সিভের সাথে মূলত অভিন্ন, কমপ্লেক্সিটিও একই হবে: $O(n \log \log n)$

```cpp
void phi_1_to_n(int n) {
    vector<int> phi(n + 1);
    for (int i = 0; i <= n; i++)
        phi[i] = i;

    for (int i = 2; i <= n; i++) {
        if (phi[i] == i) {
            for (int j = i; j <= n; j += i)
                phi[j] -= phi[j] / i;
        }
    }
}
```

### [সেগমেন্টেড সিভ](sieve-of-eratosthenes.md#segmented-sieve) ব্যবহার করে $L$ থেকে $R$ পর্যন্ত টোশেন্ট নির্ণয় { data-toc-label="Finding the totient from L to R using the segmented sieve" }

$L$ থেকে $R$-এর মধ্যে সকল সংখ্যার টোশেন্ট প্রয়োজন হলে, আমরা [সেগমেন্টেড সিভ](sieve-of-eratosthenes.md#segmented-sieve) পদ্ধতি ব্যবহার করতে পারি।

অ্যালগরিদমটি প্রথমে $\sqrt{R}$ পর্যন্ত সকল মৌলিক সংখ্যা একটি [লিনিয়ার সিভ](prime-sieve-linear.md) ব্যবহার করে $O(\sqrt{R})$ সময় ও স্থানে প্রিকম্পিউট করে। $[L, R]$ রেঞ্জের প্রতিটি সংখ্যার জন্য, এটি এই মৌলিক সংখ্যাগুলোর উপর ইটারেট করে উৎপাদক বিশ্লেষণ-ভিত্তিক $\phi$ সূত্র প্রয়োগ করে। আমরা প্রতিটি সংখ্যার অবিশ্লেষিত অংশ ট্র্যাক করতে একটি রিমেইন্ডার অ্যারে রাখি। সকল ছোট মৌলিক প্রক্রিয়া করার পরও যদি একটি রিমেইন্ডার ১-এর বেশি থাকে, তাহলে এটি $\sqrt{R}$-এর চেয়ে বড় একটি মৌলিক গুণনীয়ক নির্দেশ করে, যা চূড়ান্ত পাসে হ্যান্ডেল করা হয়। রেঞ্জ গণনার সামগ্রিক কমপ্লেক্সিটি $O((R - L + 1) \log \log R) + \sqrt{R}$।


```cpp
const long long MAX_RANGE = 1e6 + 6;
vector<long long> primes;
long long phi[MAX_RANGE], rem[MAX_RANGE];

vector<int> linear_sieve(int n) {
    vector<bool> composite(n + 1, 0);
    vector<int> prime;

    // 0 and 1 are not composite (nor prime)
    composite[0] = composite[1] = 1;

    for(int i = 2; i <= n; i++) {
        if(!composite[i]) prime.push_back(i);
        for(int j = 0; j < prime.size() && i * prime[j] <= n; j++) {
            composite[i * prime[j]] = true;
            if(i % prime[j] == 0) break;
        }
    }
    return prime;
}

// To get the value of phi(x) for L <= x <= R, use phi[x - L].
void segmented_phi(long long L, long long R) {
    for(long long i = L; i <= R; i++) {
        rem[i - L] = i;
        phi[i - L] = i;
    }

    for(long long i : primes) {
        for(long long j = max(i * i, (L + i - 1) / i * i); j <= R; j += i) {
            phi[j - L] -= phi[j - L] / i;
            while(rem[j - L] % i == 0) rem[j - L] /= i;
        }
    }

    for(long long i = 0; i < R - L + 1; i++) {
        if(rem[i] > 1) phi[i] -= phi[i] / rem[i];
    }
}
```

## ভাজকের যোগফল বৈশিষ্ট্য { #divsum}

এই আকর্ষণীয় বৈশিষ্ট্যটি গাউস প্রতিষ্ঠা করেছিলেন:

$$ \sum_{d|n} \phi{(d)} = n$$

এখানে যোগফল $n$-এর সকল ধনাত্মক ভাজক $d$-এর উপর।

উদাহরণস্বরূপ ১০-এর ভাজকগুলো হলো ১, ২, ৫ ও ১০।
তাই $\phi{(1)} + \phi{(2)} + \phi{(5)} + \phi{(10)} = 1 + 1 + 4 + 4 = 10$।

### ভাজকের যোগফল বৈশিষ্ট্য ব্যবহার করে ১ থেকে $n$ পর্যন্ত টোশেন্ট নির্ণয় { data-toc-label="Finding the totient from 1 to n using the divisor sum property" }

ভাজকের যোগফল বৈশিষ্ট্য আমাদের ১ থেকে $n$-এর মধ্যে সকল সংখ্যার টোশেন্ট গণনা করতেও দেয়।
এই ইমপ্লিমেন্টেশনটি এরাটোস্থেনিসের সিভ-ভিত্তিক আগের ইমপ্লিমেন্টেশনের চেয়ে একটু সরল, তবে সামান্য খারাপ কমপ্লেক্সিটি: $O(n \log n)$

```cpp
void phi_1_to_n(int n) {
    vector<int> phi(n + 1);
    phi[0] = 0;
    phi[1] = 1;
    for (int i = 2; i <= n; i++)
        phi[i] = i - 1;

    for (int i = 2; i <= n; i++)
        for (int j = 2 * i; j <= n; j += i)
              phi[j] -= phi[i];
}
```

## অয়লারের উপপাদ্যে প্রয়োগ { #application }

অয়লারের টোশেন্ট ফাংশনের সবচেয়ে বিখ্যাত ও গুরুত্বপূর্ণ বৈশিষ্ট্য **অয়লারের উপপাদ্যে** প্রকাশিত:

$$a^{\phi(m)} \equiv 1 \pmod m \quad \text{if } a \text{ and } m \text{ are relatively prime.}$$

বিশেষ ক্ষেত্রে যখন $m$ মৌলিক, অয়লারের উপপাদ্য **ফার্মার ক্ষুদ্র উপপাদ্যে** পরিণত হয়:

$$a^{m - 1} \equiv 1 \pmod m$$

অয়লারের উপপাদ্য ও অয়লারের টোশেন্ট ফাংশন ব্যবহারিক প্রয়োগে বেশ ঘন ঘন দেখা যায়, উদাহরণস্বরূপ উভয়ই [মডুলার গুণনীয় বিপরীত](module-inverse.md) গণনায় ব্যবহৃত হয়।

তাৎক্ষণিক ফলাফল হিসেবে আমরা এই সমতুল্যতাও পাই:

$$a^n \equiv a^{n \bmod \phi(m)} \pmod m$$

এটি অত্যন্ত বড় $n$-এর জন্য $x^n \bmod m$ গণনা করতে দেয়, বিশেষত যদি $n$ অন্য কোনো গণনার ফলাফল হয়, কারণ এটি একটি মডুলোর অধীনে $n$ গণনা করতে দেয়।

### গ্রুপ থিওরি
$\phi(n)$ হলো [মডুলো n গুণনীয় গ্রুপ](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n) $(\mathbb Z / n\mathbb Z)^\times$-এর [অর্ডার](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n), অর্থাৎ ইউনিটের গ্রুপ (গুণনীয় বিপরীত বিশিষ্ট উপাদানসমূহ)। গুণনীয় বিপরীত বিশিষ্ট উপাদানগুলো ঠিক সেগুলোই যারা $n$-এর সাথে সহমৌলিক।

একটি উপাদান $a$-এর মডুলো $n$-এ [গুণনীয় অর্ডার](https://en.wikipedia.org/wiki/Multiplicative_order), যা $\operatorname{ord}_n(a)$ দ্বারা চিহ্নিত, হলো সবচেয়ে ছোট $k>0$ যেন $a^k \equiv 1 \pmod m$। $\operatorname{ord}_n(a)$ হলো $a$ দ্বারা উৎপন্ন সাবগ্রুপের আকার, তাই ল্যাগ্রাঞ্জের উপপাদ্য অনুসারে, যেকোনো $a$-এর গুণনীয় অর্ডার $\phi(n)$-কে ভাগ করবে। যদি $a$-এর গুণনীয় অর্ডার $\phi(n)$ হয়, সর্বোচ্চ সম্ভাব্য, তাহলে $a$ একটি [আদিম মূল](primitive-root.md) এবং সংজ্ঞা অনুসারে গ্রুপটি চক্রীয়।

## সাধারণীকরণ

শেষ সমতুল্যতার একটি কম পরিচিত সংস্করণ আছে, যা সহমৌলিক নয় এমন $x$ ও $m$-এর জন্যও দক্ষতার সাথে $x^n \bmod m$ গণনা করতে দেয়।
ইচ্ছামতো $x, m$ এবং $n \geq \log_2 m$-এর জন্য:

$$x^{n}\equiv x^{\phi(m)+[n \bmod \phi(m)]} \mod m$$

প্রমাণ:

মনে করি $p_1, \dots, p_t$ হলো $x$ ও $m$-এর সাধারণ মৌলিক ভাজক, এবং $k_i$ হলো $m$-এ তাদের সূচক।
এগুলো দিয়ে সংজ্ঞায়িত করি $a = p_1^{k_1} \dots p_t^{k_t}$, যা $\frac{m}{a}$-কে $x$-এর সাথে সহমৌলিক করে।
এবং মনে করি $k$ হলো সবচেয়ে ছোট সংখ্যা যেন $a$, $x^k$-কে ভাগ করে।
$n \ge k$ ধরে, আমরা লিখতে পারি:

$$\begin{align}x^n \bmod m &= \frac{x^k}{a}ax^{n-k}\bmod m \\
&= \frac{x^k}{a}\left(ax^{n-k}\bmod m\right) \bmod m \\
&= \frac{x^k}{a}\left(ax^{n-k}\bmod a \frac{m}{a}\right) \bmod m \\
&=\frac{x^k}{a} a \left(x^{n-k} \bmod \frac{m}{a}\right)\bmod m \\
&= x^k\left(x^{n-k} \bmod \frac{m}{a}\right)\bmod m
\end{align}$$

তৃতীয় ও চতুর্থ লাইনের মধ্যে সমতুল্যতা এই সত্য থেকে অনুসৃত যে $ab \bmod ac = a(b \bmod c)$।
প্রকৃতপক্ষে যদি $b = cd + r$ যেখানে $r < c$, তাহলে $ab = acd + ar$ যেখানে $ar < ac$।

যেহেতু $x$ ও $\frac{m}{a}$ সহমৌলিক, আমরা অয়লারের উপপাদ্য প্রয়োগ করে দক্ষ সূত্র পাই (যেহেতু $k$ অত্যন্ত ছোট; প্রকৃতপক্ষে $k \le \log_2 m$):

$$x^n \bmod m = x^k\left(x^{n-k \bmod \phi(\frac{m}{a})} \bmod \frac{m}{a}\right)\bmod m.$$

এই সূত্রটি প্রয়োগ করা কঠিন, তবে আমরা এটি $x^n \bmod m$-এর আচরণ বিশ্লেষণে ব্যবহার করতে পারি। দেখা যায় ঘাতের ক্রম $(x^1 \bmod m, x^2 \bmod m, x^3 \bmod m, \dots)$ প্রথম $k$টি (বা কম) উপাদানের পর $\phi\left(\frac{m}{a}\right)$ দৈর্ঘ্যের একটি চক্রে প্রবেশ করে।
$\phi\left(\frac{m}{a}\right)$, $\phi(m)$-কে ভাগ করে (কারণ $a$ ও $\frac{m}{a}$ সহমৌলিক বলে $\phi(a) \cdot \phi\left(\frac{m}{a}\right) = \phi(m)$), তাই আমরা বলতে পারি যে পর্যায়ের দৈর্ঘ্য $\phi(m)$।
এবং যেহেতু $\phi(m) \ge \log_2 m \ge k$, আমরা কাঙ্ক্ষিত, অনেক সরল, সূত্রটি উপসংহার করতে পারি:

$$ x^n \equiv x^{\phi(m)} x^{(n - \phi(m)) \bmod \phi(m)} \bmod m \equiv x^{\phi(m)+[n \bmod \phi(m)]} \mod m.$$

## অনুশীলন সমস্যা

* [SPOJ #4141 "Euler Totient Function" [Difficulty: CakeWalk]](http://www.spoj.com/problems/ETF/)
* [UVA #10179 "Irreducible Basic Fractions" [Difficulty: Easy]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1120)
* [UVA #10299 "Relatives" [Difficulty: Easy]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1240)
* [UVA #11327 "Enumerating Rational Numbers" [Difficulty: Medium]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2302)
* [TIMUS #1673 "Admission to Exam" [Difficulty: High]](http://acm.timus.ru/problem.aspx?space=1&num=1673)
* [UVA 10990 - Another New Function](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1931)
* [Codechef - Golu and Sweetness](https://www.codechef.com/problems/COZIE)
* [SPOJ - LCM Sum](http://www.spoj.com/problems/LCMSUM/)
* [GYM - Simple Calculations  (F)](http://codeforces.com/gym/100975)
* [UVA 13132 - Laser Mirrors](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=5043)
* [SPOJ - GCDEX](http://www.spoj.com/problems/GCDEX/)
* [UVA 12995 - Farey Sequence](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4878)
* [SPOJ - Totient in Permutation (easy)](http://www.spoj.com/problems/TIP1/)
* [LOJ - Mathematically Hard](http://lightoj.com/volume_showproblem.php?problem=1007)
* [SPOJ - Totient Extreme](http://www.spoj.com/problems/DCEPCA03/)
* [SPOJ - Playing with GCD](http://www.spoj.com/problems/NAJPWG/)
* [SPOJ - G Force](http://www.spoj.com/problems/DCEPC12G/)
* [SPOJ - Smallest Inverse Euler Totient Function](http://www.spoj.com/problems/INVPHI/)
* [Codeforces - Power Tower](http://codeforces.com/problemset/problem/906/D)
* [Kattis - Exponial](https://open.kattis.com/problems/exponial)
* [LeetCode - 372. Super Pow](https://leetcode.com/problems/super-pow/)
* [Codeforces - The Holmes Children](http://codeforces.com/problemset/problem/776/E)
* [Codeforces - Small GCD](https://codeforces.com/contest/1900/problem/D)
