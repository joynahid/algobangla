---
tags:
  - Translated
e_maxx_link: rabin_karp
---

# স্ট্রিং ম্যাচিং-এর জন্য রবিন-কার্প অ্যালগরিদম

এই অ্যালগরিদমটি হ্যাশিং-এর ধারণার উপর ভিত্তি করে তৈরি, তাই আপনি যদি স্ট্রিং হ্যাশিং-এর সাথে পরিচিত না হন, তাহলে [স্ট্রিং হ্যাশিং](string-hashing.md) নিবন্ধটি দেখুন।

এই অ্যালগরিদমটি ১৯৮৭ সালে রবিন এবং কার্প প্রণয়ন করেন।

সমস্যা: দুটি স্ট্রিং দেওয়া আছে - একটি প্যাটার্ন $s$ এবং একটি টেক্সট $t$, প্যাটার্নটি টেক্সটে আছে কিনা তা নির্ণয় করুন এবং থাকলে $O(|s| + |t|)$ সময়ে এর সকল অবস্থান গণনা করুন।

অ্যালগরিদম: প্যাটার্ন $s$-এর হ্যাশ গণনা করুন।
টেক্সট $t$-এর সকল প্রিফিক্সের হ্যাশ মান গণনা করুন।
এখন, আমরা গণনাকৃত হ্যাশ ব্যবহার করে $|s|$ দৈর্ঘ্যের একটি সাবস্ট্রিংকে $s$-এর সাথে ধ্রুব সময়ে তুলনা করতে পারি।
সুতরাং, $|s|$ দৈর্ঘ্যের প্রতিটি সাবস্ট্রিংকে প্যাটার্নের সাথে তুলনা করুন। এতে মোট $O(|t|)$ সময় লাগবে।
অতএব অ্যালগরিদমের চূড়ান্ত কমপ্লেক্সিটি হলো $O(|t| + |s|)$: প্যাটার্নের হ্যাশ গণনার জন্য $O(|s|)$ এবং $|s|$ দৈর্ঘ্যের প্রতিটি সাবস্ট্রিংকে প্যাটার্নের সাথে তুলনার জন্য $O(|t|)$ প্রয়োজন।

## ইমপ্লিমেন্টেশন
```{.cpp file=rabin_karp}
vector<int> rabin_karp(string const& s, string const& t) {
    const int p = 31;
    const int m = 1e9 + 9;
    int S = s.size(), T = t.size();

    vector<long long> p_pow(max(S, T));
    p_pow[0] = 1;
    for (int i = 1; i < (int)p_pow.size(); i++)
        p_pow[i] = (p_pow[i-1] * p) % m;

    vector<long long> h(T + 1, 0);
    for (int i = 0; i < T; i++)
        h[i+1] = (h[i] + (t[i] - 'a' + 1) * p_pow[i]) % m;
    long long h_s = 0;
    for (int i = 0; i < S; i++)
        h_s = (h_s + (s[i] - 'a' + 1) * p_pow[i]) % m;

    vector<int> occurrences;
    for (int i = 0; i + S - 1 < T; i++) {
        long long cur_h = (h[i+S] + m - h[i]) % m;
        if (cur_h == h_s * p_pow[i] % m)
            occurrences.push_back(i);
    }
    return occurrences;
}
```

## অনুশীলন সমস্যা

* [SPOJ - Pattern Find](http://www.spoj.com/problems/NAJPF/)
* [Codeforces - Good Substrings](http://codeforces.com/problemset/problem/271/D)
* [Codeforces - Palindromic characteristics](https://codeforces.com/problemset/problem/835/D)
* [Leetcode - Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)
