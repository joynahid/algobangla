---
title: ক্রাউট পদ্ধতিতে নির্ণায়ক নির্ণয়
tags: 
weight: 30
---
# $O(N^3)$-এ ক্রাউট পদ্ধতিতে নির্ণায়ক নির্ণয়

এই নিবন্ধে, আমরা বর্ণনা করব কিভাবে ক্রাউট পদ্ধতি ব্যবহার করে ম্যাট্রিক্সের নির্ণায়ক নির্ণয় করা যায়, যা $O(N^3)$-এ কাজ করে।

ক্রাউট অ্যালগরিদম ম্যাট্রিক্স $A$-কে $A = L U$ আকারে ডিকম্পোজিশন করে, যেখানে $L$ হলো নিম্ন ত্রিভুজাকার এবং $U$ হলো ঊর্ধ্ব ত্রিভুজাকার ম্যাট্রিক্স। সাধারণতা না হারিয়ে, আমরা ধরে নিতে পারি যে $L$-এর সমস্ত কর্ণ উপাদান ১-এর সমান। একবার আমরা এই ম্যাট্রিক্সগুলো জানলে, $A$-এর নির্ণায়ক নির্ণয় করা সহজ: এটি ম্যাট্রিক্স $U$-এর মূল কর্ণের সমস্ত উপাদানের গুণফলের সমান।

একটি উপপাদ্য রয়েছে যা বলে যে যেকোনো ইনভার্টিবল ম্যাট্রিক্সের একটি LU-ডিকম্পোজিশন আছে, এবং এটি অনন্য, যদি এবং কেবল যদি এর সমস্ত প্রিন্সিপাল মাইনর অশূন্য হয়। আমরা কেবল সেই ডিকম্পোজিশন বিবেচনা করি যেখানে ম্যাট্রিক্স $L$-এর কর্ণ এক দিয়ে গঠিত।

ধরি $A$ হলো ম্যাট্রিক্স এবং $N$ হলো এর আকার। আমরা নিচের ধাপগুলো ব্যবহার করে ম্যাট্রিক্স $L$ এবং $U$-এর উপাদানগুলো বের করব:

 ১. $i = 1, 2, ..., N$-এর জন্য $L_{i i} = 1$ ধরি।
 ২. প্রতিটি $j = 1, 2, ..., N$-এর জন্য নিচের কাজগুলো করি:
      - $i = 1, 2, ..., j$-এর জন্য মান নির্ণয় করি

        \[U_{ij} = A_{ij} - \sum_{k=1}^{i-1} L_{ik} \cdot U_{kj}\]

      - এরপর, $i = j+1, j+2, ..., N$-এর জন্য মান নির্ণয় করি

        \[L_{ij} = \frac{1}{U_{jj}} \left(A_{ij} - \sum_{k=1}^{j-1} L_{ik} \cdot U_{kj} \right).\]

## ইমপ্লিমেন্টেশন

```java
static BigInteger det (BigDecimal a [][], int n) {
	try {

	for (int i=0; i<n; i++) {
		boolean nonzero = false;
		for (int j=0; j<n; j++)
			if (a[i][j].compareTo (new BigDecimal (BigInteger.ZERO)) > 0)
				nonzero = true;
		if (!nonzero)
			return BigInteger.ZERO;
	}

	BigDecimal scaling [] = new BigDecimal [n];
	for (int i=0; i<n; i++) {
		BigDecimal big = new BigDecimal (BigInteger.ZERO);
		for (int j=0; j<n; j++)
			if (a[i][j].abs().compareTo (big) > 0)
				big = a[i][j].abs();
		scaling[i] = (new BigDecimal (BigInteger.ONE)) .divide
			(big, 100, BigDecimal.ROUND_HALF_EVEN);
	}

	int sign = 1;

	for (int j=0; j<n; j++) {
		for (int i=0; i<j; i++) {
			BigDecimal sum = a[i][j];
			for (int k=0; k<i; k++)
				sum = sum.subtract (a[i][k].multiply (a[k][j]));
			a[i][j] = sum;
		}

		BigDecimal big = new BigDecimal (BigInteger.ZERO);
		int imax = -1;
		for (int i=j; i<n; i++) {
			BigDecimal sum = a[i][j];
			for (int k=0; k<j; k++)
				sum = sum.subtract (a[i][k].multiply (a[k][j]));
			a[i][j] = sum;
			BigDecimal cur = sum.abs();
			cur = cur.multiply (scaling[i]);
			if (cur.compareTo (big) >= 0) {
				big = cur;
				imax = i;
			}
		}

		if (j != imax) {
			for (int k=0; k<n; k++) {
				BigDecimal t = a[j][k];
				a[j][k] = a[imax][k];
				a[imax][k] = t;
			}

			BigDecimal t = scaling[imax];
			scaling[imax] = scaling[j];
			scaling[j] = t;

			sign = -sign;
		}

		if (j != n-1)
			for (int i=j+1; i<n; i++)
				a[i][j] = a[i][j].divide
					(a[j][j], 100, BigDecimal.ROUND_HALF_EVEN);

	}

	BigDecimal result = new BigDecimal (1);
	if (sign == -1)
		result = result.negate();
	for (int i=0; i<n; i++)
		result = result.multiply (a[i][i]);

	return result.divide
		(BigDecimal.valueOf(1), 0, BigDecimal.ROUND_HALF_EVEN).toBigInteger();
	}
	catch (Exception e) {
		return BigInteger.ZERO;
	}
}
```
