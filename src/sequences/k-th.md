---
title: $O(N)$-এ $K$-তম ক্রম পরিসংখ্যান
tags:
  - Translated
e_maxx_link: kth_order_statistics
---
# $O(N)$-এ $K$-তম ক্রম পরিসংখ্যান

$N$ আকারের একটি অ্যারে $A$ এবং একটি সংখ্যা $K$ দেওয়া আছে। সমস্যা হলো অ্যারেতে $K$-তম বৃহত্তম সংখ্যা, অর্থাৎ $K$-তম ক্রম পরিসংখ্যান খুঁজে বের করা।

মূল ধারণা — কুইক সর্ট অ্যালগরিদমের ধারণা ব্যবহার করা। আসলে, অ্যালগরিদমটি সরল, এটি প্রমাণ করা বেশি কঠিন যে এটি গড়ে $O(N)$-এ চলে, কুইক সর্টের বিপরীতে।

## ইমপ্লিমেন্টেশন (নন-রিকার্সিভ)

```cpp
template <class T>
T order_statistics (std::vector<T> a, unsigned n, unsigned k)
{
    using std::swap;
    for (unsigned l=1, r=n; ; )
    {
        if (r <= l+1)
        {
            // the current part size is either 1 or 2, so it is easy to find the answer
            if (r == l+1 && a[r] < a[l])
                swap (a[l], a[r]);
            return a[k];
        }

        // ordering a[l], a[l+1], a[r]
        unsigned mid = (l + r) >> 1;
        swap (a[mid], a[l+1]);
        if (a[l] > a[r])
            swap (a[l], a[r]);
        if (a[l+1] > a[r])
            swap (a[l+1], a[r]);
        if (a[l] > a[l+1])
            swap (a[l], a[l+1]);

        // performing division
        // barrier is a[l + 1], i.e. median among a[l], a[l + 1], a[r]
        unsigned
            i = l+1,
            j = r;
        const T
            cur = a[l+1];
        for (;;)
        {
            while (a[++i] < cur) ;
            while (a[--j] > cur) ;
            if (i > j)
                break;
            swap (a[i], a[j]);
        }

        // inserting the barrier
        a[l+1] = a[j];
        a[j] = cur;

        // we continue to work in that part, which must contain the required element
        if (j >= k)
            r = j-1;
        if (j <= k)
            l = i;
    }
}
```

## টীকা
* উপরের র‍্যান্ডমাইজড অ্যালগরিদমটিকে [quickselect](https://en.wikipedia.org/wiki/Quickselect) বলা হয়। এটি সঠিকভাবে চালানোর জন্য কল করার আগে $A$-তে র‍্যান্ডম শাফেল করা উচিত অথবা ব্যারিয়ার হিসেবে একটি র‍্যান্ডম উপাদান ব্যবহার করা উচিত। ডিটারমিনিস্টিক অ্যালগরিদমও আছে যা নির্দিষ্ট সমস্যাটি রৈখিক সময়ে সমাধান করে, যেমন [median of medians](https://en.wikipedia.org/wiki/Median_of_medians)।
* [std::nth_element](https://en.cppreference.com/w/cpp/algorithm/nth_element) C++-এ এটি সমাধান করে কিন্তু gcc-এর ইমপ্লিমেন্টেশন সবচেয়ে খারাপ ক্ষেত্রে $O(n \log n )$ সময়ে চলে।
* $K$টি ক্ষুদ্রতম উপাদান খুঁজে বের করা রৈখিক ওভারহেডসহ $K$-তম উপাদান খুঁজে বের করায় রিডিউস করা যায়, কারণ এগুলো ঠিক সেই উপাদান যা $K$-তম-এর চেয়ে ছোট।

## অনুশীলন সমস্যা
- [Leetcode: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)
- [CODECHEF: Median](https://www.codechef.com/problems/CD1IT1)
