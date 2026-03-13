---
tags: 
title: MEX (minimal excluded) of a sequence
weight: 40
---
# একটি সিকোয়েন্সের মেক্স (MEX - ন্যূনতম বাদ পড়া)

$N$ আকারের একটি অ্যারে $A$ দেওয়া আছে। তোমাকে এমন ক্ষুদ্রতম অঋণাত্মক উপাদান খুঁজে বের করতে হবে যেটা অ্যারেতে নেই। এই সংখ্যাটিকে সাধারণত **মেক্স** (MEX - ন্যূনতম বাদ পড়া) বলা হয়।

$$
\begin{align}
\text{mex}(\{0, 1, 2, 4, 5\}) &= 3 \\
\text{mex}(\{0, 1, 2, 3, 4\}) &= 5 \\
\text{mex}(\{1, 2, 3, 4, 5\}) &= 0 \\
\end{align}
$$

লক্ষ্য করো, $N$ আকারের একটি অ্যারের মেক্স কখনোই $N$-এর চেয়ে বড় হতে পারে না।

সবচেয়ে সহজ পদ্ধতি হলো অ্যারে $A$-এর সকল উপাদানের একটি সেট তৈরি করা, যাতে আমরা দ্রুত পরীক্ষা করতে পারি কোনো সংখ্যা অ্যারেতে আছে কিনা।
এরপর আমরা $0$ থেকে $N$ পর্যন্ত সকল সংখ্যা পরীক্ষা করতে পারি, যদি বর্তমান সংখ্যাটি সেটে না থাকে, তাহলে সেটা রিটার্ন করব।

## ইমপ্লিমেন্টেশন

নিচের অ্যালগরিদমটি $O(N \log N)$ সময়ে চলে।

```cpp
int mex(vector<int> const& A) {
    set<int> b(A.begin(), A.end());

    int result = 0;
    while (b.count(result))
        ++result;
    return result;
}
```

যদি কোনো অ্যালগরিদমে $O(N)$ সময়ে মেক্স গণনা করা প্রয়োজন হয়, তাহলে সেট-এর পরিবর্তে একটি বুলিয়ান ভেক্টর ব্যবহার করে এটা সম্ভব।
লক্ষ্য করো, অ্যারেটির আকার সম্ভাব্য সর্বোচ্চ অ্যারে আকারের সমান হতে হবে।


```cpp
int mex(vector<int> const& A) {
    static bool used[MAX_N+1] = { 0 };

    // mark the given numbers
    for (int x : A) {
        if (x <= MAX_N)
            used[x] = true;
    }

    // find the mex
    int result = 0;
    while (used[result])
        ++result;

    // clear the array again
    for (int x : A) {
        if (x <= MAX_N)
            used[x] = false;
    }

    return result;
}
```

এই পদ্ধতিটি দ্রুত, কিন্তু শুধুমাত্র তখনই ভালো কাজ করে যখন তোমাকে একবার মেক্স গণনা করতে হয়।
যদি তোমাকে বারবার মেক্স গণনা করতে হয়, যেমন তোমার অ্যারে ক্রমাগত পরিবর্তন হচ্ছে, তাহলে এটা কার্যকর নয়।
এর জন্য আমাদের আরও ভালো কিছু দরকার।

## অ্যারে আপডেটসহ মেক্স

এই সমস্যায় তোমাকে অ্যারের পৃথক সংখ্যা পরিবর্তন করতে হবে এবং প্রতিটি আপডেটের পরে অ্যারের নতুন মেক্স গণনা করতে হবে।

এমন কুয়েরিগুলো দক্ষতার সাথে পরিচালনা করার জন্য একটি উন্নত ডাটা স্ট্রাকচার (data structure) প্রয়োজন।

একটি পদ্ধতি হলো $0$ থেকে $N$ পর্যন্ত প্রতিটি সংখ্যার ফ্রিকোয়েন্সি নেওয়া এবং এর উপর একটি ট্রি-সদৃশ ডাটা স্ট্রাকচার তৈরি করা।
যেমন একটি সেগমেন্ট ট্রি বা একটি ট্রিপ।
প্রতিটি নোড একটি সংখ্যার রেঞ্জ প্রতিনিধিত্ব করে, এবং রেঞ্জের মোট ফ্রিকোয়েন্সির পাশাপাশি তুমি সেই রেঞ্জে ভিন্ন ভিন্ন সংখ্যার পরিমাণও সংরক্ষণ করবে।
এই ডাটা স্ট্রাকচারটি $O(\log N)$ সময়ে আপডেট করা সম্ভব, এবং $O(\log N)$ সময়ে মেক্সও খুঁজে পাওয়া সম্ভব, মেক্সের জন্য বাইনারি সার্চ করে।
যদি $[0, \lfloor N/2 \rfloor)$ রেঞ্জ প্রতিনিধিত্বকারী নোডে $\lfloor N/2 \rfloor$ সংখ্যক ভিন্ন সংখ্যা না থাকে, তাহলে একটি অনুপস্থিত এবং মেক্স $\lfloor N/2 \rfloor$-এর চেয়ে ছোট, এবং তুমি ট্রির বাম শাখায় রিকার্সন করতে পারো। অন্যথায় এটা কমপক্ষে $\lfloor N/2 \rfloor$, এবং তুমি ট্রির ডান শাখায় রিকার্সন করতে পারো।

স্ট্যান্ডার্ড লাইব্রেরি ডাটা স্ট্রাকচার `map` এবং `set` ব্যবহার করেও এটা সম্ভব ([এখানে](https://codeforces.com/blog/entry/81287?#comment-677837) ব্যাখ্যা করা একটি পদ্ধতির উপর ভিত্তি করে)।
একটি `map` দিয়ে আমরা প্রতিটি সংখ্যার ফ্রিকোয়েন্সি মনে রাখব, এবং `set` দিয়ে আমরা অ্যারেতে বর্তমানে অনুপস্থিত সংখ্যাগুলো প্রতিনিধিত্ব করব।
যেহেতু একটি `set` সাজানো থাকে, `*set.begin()` হবে মেক্স।
মোট $O(N \log N)$ প্রিপ্রসেসিং প্রয়োজন, এবং এরপর মেক্স $O(1)$-এ গণনা করা যায় এবং একটি আপডেট $O(\log N)$-এ কমপ্লিট করা যায়।

```cpp
class Mex {
private:
    map<int, int> frequency;
    set<int> missing_numbers;
    vector<int> A;

public:
    Mex(vector<int> const& A) : A(A) {
        for (int i = 0; i <= A.size(); i++)
            missing_numbers.insert(i);

        for (int x : A) {
            ++frequency[x];
            missing_numbers.erase(x);
        }
    }

    int mex() {
        return *missing_numbers.begin();
    }

    void update(int idx, int new_value) {
        if (--frequency[A[idx]] == 0)
            missing_numbers.insert(A[idx]);
        A[idx] = new_value;
        ++frequency[new_value];
        missing_numbers.erase(new_value);
    }
};
```

## অনুশীলন সমস্যা

- [AtCoder: Neq Min](https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_c)
- [Codeforces: Informatics in MAC](https://codeforces.com/contest/1935/problem/B)
- [Codeforces: Replace by MEX](https://codeforces.com/contest/1375/problem/D)
- [Codeforces: Vitya and Strange Lesson](https://codeforces.com/problemset/problem/842/D)
- [Codeforces: MEX Queries](https://codeforces.com/contest/817/problem/F)
