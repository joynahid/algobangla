---
title: "ডিসক্রিট রুট"
tags: 
weight: 80
---
# ডিসক্রিট রুট

ডিসক্রিট রুট খুঁজে বের করার সমস্যাটি নিম্নরূপে সংজ্ঞায়িত। একটি মৌলিক সংখ্যা $n$ এবং দুটি পূর্ণসংখ্যা $a$ ও $k$ দেওয়া আছে, সকল $x$ খুঁজুন যেন:

$x^k \equiv a \pmod n$

## অ্যালগরিদম

আমরা এই সমস্যাটি [ডিসক্রিট লগারিদম সমস্যায়](discrete-log.md) রিডিউস করে সমাধান করব।

আসুন $n$ মডুলোতে [প্রিমিটিভ রুটের](primitive-root.md) ধারণা প্রয়োগ করি। ধরি $g$ হলো $n$ মডুলোতে একটি প্রিমিটিভ রুট। লক্ষ্য করুন যে $n$ মৌলিক হওয়ায়, এটি অবশ্যই বিদ্যমান, এবং $O(Ans \cdot \log \phi (n) \cdot \log n) = O(Ans \cdot \log^2 n)$-এ খুঁজে পাওয়া সম্ভব, সাথে $\phi (n)$ ফ্যাক্টরাইজেশনের সময়।

$a = 0$ কেসটি আমরা সহজেই বাতিল করতে পারি। এই ক্ষেত্রে, স্পষ্টতই শুধুমাত্র একটি উত্তর আছে: $x = 0$।

যেহেতু আমরা জানি $n$ মৌলিক এবং ১ থেকে $n-1$ পর্যন্ত যেকোনো সংখ্যা প্রিমিটিভ রুটের ঘাত হিসেবে উপস্থাপন করা যায়, আমরা ডিসক্রিট রুট সমস্যাটি নিম্নরূপে উপস্থাপন করতে পারি:

$(g^y)^k \equiv a \pmod n$

যেখানে

$x \equiv g^y \pmod n$

এটি, আবার, নিম্নরূপে পুনরায় লেখা যায়

$(g^k)^y \equiv a \pmod n$

এখন আমাদের একটি অজানা $y$ আছে, যা একটি ডিসক্রিট লগারিদম সমস্যা। সমাধানটি শ্যাংকসের বেবি-স্টেপ জায়ান্ট-স্টেপ অ্যালগরিদম ব্যবহার করে $O(\sqrt {n} \log n)$-এ পাওয়া যায় (অথবা আমরা যাচাই করতে পারি যে কোনো সমাধান নেই)।

একটি সমাধান $y_0$ পাওয়ার পর, ডিসক্রিট রুট সমস্যার সমাধানগুলোর একটি হবে $x_0 = g^{y_0} \pmod n$।

## একটি জানা সমাধান থেকে সকল সমাধান খুঁজে বের করা

প্রদত্ত সমস্যাটি পুরোপুরি সমাধান করতে, আমাদের একটি জানা সমাধান $x_0 = g^{y_0} \pmod n$ থেকে সকল সমাধান খুঁজে বের করতে হবে।

আসুন স্মরণ করি যে একটি প্রিমিটিভ রুটের সর্বদা $\phi (n)$ অর্ডার থাকে, অর্থাৎ $g$-এর সর্বনিম্ন ঘাত যা ১ দেয় তা হলো $\phi (n)$। তাই, আমরা সূচকে $\phi (n)$ পদ যোগ করলেও একই মান পাই:

$x^k \equiv g^{ y_0 \cdot k + l \cdot \phi (n)} \equiv a \pmod n \forall l \in Z$

অতএব, সকল সমাধান নিম্নরূপ:

$x = g^{y_0 + \frac {l \cdot \phi (n)}{k}} \pmod n \forall l \in Z$.

যেখানে $l$ এমনভাবে বেছে নেওয়া হয় যাতে ভগ্নাংশটি পূর্ণসংখ্যা হয়। এটি সত্য হতে হলে, লব $\phi (n)$ এবং $k$-এর ল.সা.গু দ্বারা বিভাজ্য হতে হবে। মনে রাখুন দুটি সংখ্যার ল.সা.গু $lcm(a, b) = \frac{a \cdot b}{gcd(a, b)}$; আমরা পাই

$x = g^{y_0 + i \frac {\phi (n)}{gcd(k, \phi (n))}} \pmod n \forall i \in Z$.

ডিসক্রিট রুট সমস্যার সকল সমাধানের জন্য এটি চূড়ান্ত সূত্র।

## ইমপ্লিমেন্টেশন

এখানে একটি সম্পূর্ণ ইমপ্লিমেন্টেশন দেওয়া হলো, প্রিমিটিভ রুট, ডিসক্রিট লগ খোঁজা এবং সকল সমাধান খোঁজা ও প্রিন্ট করার প্রসিডিউরসহ।

```cpp
int gcd(int a, int b) {
	return a ? gcd(b % a, a) : b;
}

int powmod(int a, int b, int p) {
	int res = 1;
	while (b > 0) {
		if (b & 1) {
			res = res * a % p;
		}
		a = a * a % p;
		b >>= 1;
	}
	return res;
}

// Finds the primitive root modulo p
int generator(int p) {
	vector<int> fact;
	int phi = p-1, n = phi;
	for (int i = 2; i * i <= n; ++i) {
		if (n % i == 0) {
			fact.push_back(i);
			while (n % i == 0)
				n /= i;
		}
	}
	if (n > 1)
		fact.push_back(n);

	for (int res = 2; res <= p; ++res) {
		bool ok = true;
		for (int factor : fact) {
			if (powmod(res, phi / factor, p) == 1) {
				ok = false;
				break;
			}
		}
		if (ok) return res;
	}
	return -1;
}

// This program finds all numbers x such that x^k = a (mod n)
int main() {
	int n, k, a;
	scanf("%d %d %d", &n, &k, &a);
	if (a == 0) {
		puts("1\n0");
		return 0;
	}

	int g = generator(n);

	// Baby-step giant-step discrete logarithm algorithm
	int sq = (int) sqrt (n + .0) + 1;
	vector<pair<int, int>> dec(sq);
	for (int i = 1; i <= sq; ++i)
		dec[i-1] = {powmod(g, i * sq * k % (n - 1), n), i};
	sort(dec.begin(), dec.end());
	int any_ans = -1;
	for (int i = 0; i < sq; ++i) {
		int my = powmod(g, i * k % (n - 1), n) * a % n;
		auto it = lower_bound(dec.begin(), dec.end(), make_pair(my, 0));
		if (it != dec.end() && it->first == my) {
			any_ans = it->second * sq - i;
			break;
		}
	}
	if (any_ans == -1) {
		puts("0");
		return 0;
	}

	// Print all possible answers
	int delta = (n-1) / gcd(k, n-1);
	vector<int> ans;
	for (int cur = any_ans % delta; cur < n-1; cur += delta)
		ans.push_back(powmod(g, cur, n));
	sort(ans.begin(), ans.end());
	printf("%d\n", ans.size());
	for (int answer : ans)
		printf("%d ", answer);
}
```

## অনুশীলন সমস্যা

* [Codeforces - Lunar New Year and a Recursive Sequence](https://codeforces.com/contest/1106/problem/F)
