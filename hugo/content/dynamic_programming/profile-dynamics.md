---
title: "ব্রোকেন প্রোফাইলে ডায়নামিক প্রোগ্রামিং। \"পার্কেট\" সমস্যা"
tags: 
weight: 10
---
# ব্রোকেন প্রোফাইলে ডায়নামিক প্রোগ্রামিং। "পার্কেট" সমস্যা

ব্রোকেন প্রোফাইলে ডিপি ব্যবহার করে সমাধান করা সাধারণ সমস্যাগুলোর মধ্যে রয়েছে:

- একটি এলাকা (যেমন দাবার বোর্ড/গ্রিড) কিছু চিত্র (যেমন ডমিনো) দিয়ে সম্পূর্ণভাবে পূরণ করার উপায়ের সংখ্যা বের করা
- ন্যূনতম সংখ্যক চিত্র দিয়ে একটি এলাকা পূরণ করার উপায় বের করা
- ন্যূনতম সংখ্যক পূরণ না হওয়া স্থান (বা গ্রিডের ক্ষেত্রে ঘর) সহ আংশিক পূরণ বের করা
- ন্যূনতম সংখ্যক চিত্র দিয়ে আংশিক পূরণ বের করা, যাতে আর কোনো চিত্র যোগ করা না যায়

## "পার্কেট" সমস্যা

**সমস্যার বিবরণ।** $N \times M$ আকারের একটি গ্রিড দেওয়া আছে। $2 \times 1$ আকারের চিত্র দিয়ে গ্রিডটি পূরণ করার উপায়ের সংখ্যা বের করুন (কোনো ঘর খালি থাকবে না, এবং চিত্রগুলো একে অপরের উপর ওভারল্যাপ করবে না)।

ধরি ডিপি স্টেট হলো: $dp[i, mask]$, যেখানে $i = 1, \ldots N$ এবং $mask = 0, \ldots 2^M - 1$।

$i$ বর্তমান গ্রিডের সারির সংখ্যা উপস্থাপন করে, এবং $mask$ হলো বর্তমান গ্রিডের শেষ সারির অবস্থা। যদি $mask$-এর $j$-তম বিট $0$ হয় তাহলে সংশ্লিষ্ট ঘরটি পূরণ করা হয়েছে, অন্যথায় এটি পূরণ হয়নি।

স্পষ্টতই, সমস্যার উত্তর হবে $dp[N, 0]$।

আমরা প্রতিটি $i = 1, \cdots N$ এবং প্রতিটি $mask = 0, \ldots 2^M - 1$ এর উপর ইটারেট করে ডিপি স্টেট তৈরি করব, এবং প্রতিটি $mask$-এর জন্য আমরা শুধুমাত্র সামনের দিকে ট্রানজিশন করব, অর্থাৎ বর্তমান গ্রিডে চিত্র _যোগ_ করব।

### ইমপ্লিমেন্টেশন

```cpp
int n, m;
vector < vector<long long> > dp;


void calc (int x = 0, int y = 0, int mask = 0, int next_mask = 0)
{
	if (x == n)
		return;
	if (y >= m)
		dp[x+1][next_mask] += dp[x][mask];
	else
	{
		int my_mask = 1 << y;
		if (mask & my_mask)
			calc (x, y+1, mask, next_mask);
		else
		{
			calc (x, y+1, mask, next_mask | my_mask);
			if (y+1 < m && ! (mask & my_mask) && ! (mask & (my_mask << 1)))
				calc (x, y+2, mask, next_mask);
		}
	}
}


int main()
{
	cin >> n >> m;

	dp.resize (n+1, vector<long long> (1<<m));
	dp[0][0] = 1;
	for (int x=0; x<n; ++x)
		for (int mask=0; mask<(1<<m); ++mask)
			calc (x, 0, mask, 0);

	cout << dp[n][0];

}
```

## অনুশীলন সমস্যা

- [UVA 10359 - Tiling](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1300)
- [UVA 10918 - Tri Tiling](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1859)
- [SPOJ GNY07H (Four Tiling)](https://www.spoj.com/problems/GNY07H/)
- [SPOJ M5TILE (Five Tiling)](https://www.spoj.com/problems/M5TILE/)
- [SPOJ MNTILE (MxN Tiling)](https://www.spoj.com/problems/MNTILE/)
- [SPOJ DOJ1](https://www.spoj.com/problems/DOJ1/)
- [SPOJ DOJ2](https://www.spoj.com/problems/DOJ2/)
- [SPOJ BTCODE_J](https://www.spoj.com/problems/BTCODE_J/)
- [SPOJ PBOARD](https://www.spoj.com/problems/PBOARD/)
- [ACM HDU 4285 - Circuits](http://acm.hdu.edu.cn/showproblem.php?pid=4285)
- [LiveArchive 4608 - Mosaic](https://vjudge.net/problem/UVALive-4608)
- [Timus 1519 - Formula 1](https://acm.timus.ru/problem.aspx?space=1&num=1519)
- [Codeforces Parquet](https://codeforces.com/problemset/problem/26/C)

## রেফারেন্স

- [Blog by EvilBunny](https://web.archive.org/web/20180712171735/https://blog.evilbuggy.com/2018/05/broken-profile-dynamic-programming.html)
- [TopCoder Recipe by "syg96"](https://apps.topcoder.com/forums/?module=Thread&start=0&threadID=697369)
- [Blogpost by sk765](http://sk765.blogspot.com/2012/02/dynamic-programming-with-profile.html)
