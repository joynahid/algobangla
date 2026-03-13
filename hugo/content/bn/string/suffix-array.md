---
title: "সাফিক্স অ্যারে"
tags: 
weight: 50
---
# সাফিক্স অ্যারে

## সংজ্ঞা

ধরি $s$ দৈর্ঘ্য $n$ এর একটি স্ট্রিং। $s$ এর $i$-তম সাফিক্স হল সাবস্ট্রিং $s[i \ldots n - 1]$।

একটি **সাফিক্স অ্যারে** পূর্ণসংখ্যা রয়েছে যা দেওয়া স্ট্রিং-এর সমস্ত সাফিক্সের **শুরুর সূচক** প্রতিনিধিত্ব করে, উপরোক্ত সাফিক্সগুলি সাজানোর পরে।

উদাহরণস্বরূপ স্ট্রিং $s = abaab$ দেখো।
সমস্ত সাফিক্স এভাবে

$$\begin{array}{ll}
0. & abaab \\
1. & baab \\
2. & aab \\
3. & ab \\
4. & b
\end{array}$$

এই স্ট্রিংগুলি সাজানোর পরে:

$$\begin{array}{ll}
2. & aab \\
3. & ab \\
0. & abaab \\
4. & b \\
1. & baab
\end{array}$$

অতএব $s$ এর জন্য সাফিক্স অ্যারে হবে $(2,~ 3,~ 0,~ 4,~ 1)$।

একটি ডাটা স্ট্রাকচার (data structure) হিসেবে এটা ডেটা সংকোচন, বায়োইনফরম্যাটিক্স এবং সাধারণভাবে স্ট্রিং এবং স্ট্রিং ম্যাচিং সমস্যা সম্পর্কিত যেকোনো ক্ষেত্রে ব্যাপকভাবে ব্যবহৃত হয়।

## নির্মাণ

### $O(n^2 \log n)$ পদ্ধতি {data-toc-label="O(n^2 log n) approach"}

এটা সবচেয়ে নিষ্কলুষ পদ্ধতি।
সমস্ত সাফিক্স নাও এবং কুইকসর্ট বা মার্জসর্ট ব্যবহার করে সেগুলো সাজাও এবং একই সাথে তাদের মূল ইনডেক্স ধরে রাখো।
সাজানোটি $O(n \log n)$ তুলনা ব্যবহার করে, এবং যেহেতু দুটি স্ট্রিং তুলনা করতে অতিরিক্ত $O(n)$ সময় লাগবে, আমরা চূড়ান্ত কমপ্লেক্সিটি $O(n^2 \log n)$ পাই।

### $O(n \log n)$ পদ্ধতি {data-toc-label="O(n log n) approach"}

কঠোরভাবে বলতে গেলে নিম্নোক্ত অ্যালগরিদম সাফিক্স সাজাবে না, বরং একটি স্ট্রিংয়ের সাইক্লিক পরিবর্তন সাজাবে।
তবে আমরা এটা থেকে সাফিক্স সাজানোর জন্য একটি অ্যালগরিদম সহজেই উদ্ভাবন করতে পারি:
স্ট্রিংয়ের শেষে একটি স্বেচ্ছাচারী অক্ষর সংযুক্ত করা যথেষ্ট যা স্ট্রিংয়ের যেকোনো অক্ষরের চেয়ে ছোট।
সাধারণত \$ চিহ্ন ব্যবহার করা হয়।
তারপর সাজানো সাইক্লিক পরিবর্তনের ক্রম সাজানো সাফিক্সের ক্রমের সমতুল্য, যেমন এখানে স্ট্রিং $dabbb$ সহ প্রদর্শিত।

$$\begin{array}{lll}
1. & abbb\$d & abbb \\
4. & b\$dabb & b \\
3. & bb\$dab & bb \\
2. & bbb\$da & bbb \\
0. & dabbb\$ & dabbb
\end{array}$$

যেহেতু আমরা সাইক্লিক পরিবর্তন সাজাতে যাচ্ছি, আমরা **সাইক্লিক সাবস্ট্রিং** কনসিডার করব।
আমরা $s[i \dots j]$ চিহ্ন ব্যবহার করব $s$ এর সাবস্ট্রিংয়ের জন্য এমনকি $i > j$ হলেও।
এই ক্ষেত্রে আমরা আসলে স্ট্রিং $s[i \dots n-1] + s[0 \dots j]$ অর্থ করি।
অতিরিক্তভাবে আমরা $s$ এর দৈর্ঘ্যের মডুলো সমস্ত সূচক নেব, এবং সহজতার জন্য মডুলো অপারেশন বাদ দেব।

আমরা যে অ্যালগরিদম আলোচনা করি তা $\lceil \log n \rceil + 1$ ইটারেশন সম্পাদন করবে।
$k$-তম ইটারেশনতে ($k = 0 \dots \lceil \log n \rceil$) আমরা $s$ এর দৈর্ঘ্য $2^k$ এর $n$ সাইক্লিক সাবস্ট্রিং সাজাই।
$\lceil \log n \rceil$-তম ইটারেশনর পরে দৈর্ঘ্য $2^{\lceil \log n \rceil} \ge n$ এর সাবস্ট্রিংগুলি সাজানো হবে, তাই এটা সাইক্লিক পরিবর্তন একসাথে সাজানোর সমতুল্য।

অ্যালগরিদমের প্রতিটি ইটারেশনতে, পারমুটেশন $p[0 \dots n-1]$ ছাড়াও, যেখানে $p[i]$ হল সাজানো ক্রমে $i$-তম সাবস্ট্রিং ($i$ থেকে শুরু করে এবং দৈর্ঘ্য $2^k$) এর সূচক, আমরা একটি অ্যারে $c[0 \dots n-1]$ ও বজায় রাখব, যেখানে $c[i]$ **সমতুল্য শ্রেণী** এর সাথে সামঞ্জস্যপূর্ণ যাতে সাবস্ট্রিং অন্তর্গত।
কারণ কিছু সাবস্ট্রিং সমান হবে, এবং অ্যালগরিদম তাদের সমানভাবে পরিচালনা করতে প্রয়োজন।
সুবিধার জন্য শ্রেণীগুলি শূন্য থেকে শুরু করা সংখ্যা দ্বারা লেবেল করা হবে।
অতিরিক্তভাবে সংখ্যা $c[i]$ এমনভাবে ডিটারমিন করা হবে যাতে তারা ক্রম সম্পর্কিত তথ্য সংরক্ষণ করে:
যদি একটি সাবস্ট্রিং অন্যটির চেয়ে ছোট হয়, তবে এটিরও একটি ছোট শ্রেণী লেবেল থাকা উচিত।
সমতুল্য শ্রেণীর সংখ্যা একটি পরিবর্তনশীল $\text{classes}$ তে সংরক্ষণ করা হবে।

চলো একটি উদাহরণ দেখি।
স্ট্রিং $s = aaba$ কনসিডার করো।
প্রতিটি ইটারেশনর জন্য সাইক্লিক সাবস্ট্রিং এবং সংশ্লিষ্ট অ্যারে $p[]$ এবং $c[]$ দেওয়া হয়:

$$\begin{array}{cccc}
0: & (a,~ a,~ b,~ a) & p = (0,~ 1,~ 3,~ 2) & c = (0,~ 0,~ 1,~ 0)\\
1: & (aa,~ ab,~ ba,~ aa) & p = (0,~ 3,~ 1,~ 2) & c = (0,~ 1,~ 2,~ 0)\\
2: & (aaba,~ abaa,~ baaa,~ aaab) & p = (3,~ 0,~ 1,~ 2) & c = (1,~ 2,~ 3,~ 0)\\
\end{array}$$

এটা উল্লেখযোগ্য যে $p[]$ এর মানগুলি আলাদা হতে পারে।
উদাহরণস্বরূপ $0$-তম ইটারেশনতে অ্যারেটি $p = (3,~ 1,~ 0,~ 2)$ বা $p = (3,~ 0,~ 1,~ 2)$ ও হতে পারত।
এই সমস্ত বিকল্প সাবস্ট্রিংগুলি একটি সাজানো ক্রমে পরিবর্তন করে।
তাই সবই বৈধ।
একই সাথে অ্যারে $c[]$ স্থির, কোনো দ্ব্যর্থতা থাকতে পারে না।

এখন চলো অ্যালগরিদমের ইমপ্লিমেন্টেশনে ফোকাস করি।
আমরা একটি ফাংশন লেখব যা স্ট্রিং $s$ নেয় এবং সাজানো সাইক্লিক পরিবর্তনের পারমুটেশন রিটার্ন করে।

```cpp
vector<int> sort_cyclic_shifts(string const& s) {
    int n = s.size();
    const int alphabet = 256;
```

At the beginning (in the **$0$-th iteration**) we must sort the cyclic substrings of length $1$, that is we have to sort all characters of the string and divide them into equivalence classes (same symbols get assigned to the same class).
This can be done trivially, for example, by using **counting sort**.
For each character we count how many times it appears in the string, and then use this information to create the array $p[]$.
After that we go through the array $p[]$ and construct $c[]$ by comparing adjacent characters.

```cpp
    vector<int> p(n), c(n), cnt(max(alphabet, n), 0);
    for (int i = 0; i < n; i++)
        cnt[s[i]]++;
    for (int i = 1; i < alphabet; i++)
        cnt[i] += cnt[i-1];
    for (int i = 0; i < n; i++)
        p[--cnt[s[i]]] = i;
    c[p[0]] = 0;
    int classes = 1;
    for (int i = 1; i < n; i++) {
        if (s[p[i]] != s[p[i-1]])
            classes++;
        c[p[i]] = classes - 1;
    }
```

Now we have to talk about the iteration step.
Let's assume we have already performed the $k-1$-th step and computed the values of the arrays $p[]$ and $c[]$ for it.
We want to compute the values for the $k$-th step in $O(n)$ time.
Since we perform this step $O(\log n)$ times, the complete algorithm will have a time complexity of $O(n \log n)$.

To do this, note that the cyclic substrings of length $2^k$ consists of two substrings of length $2^{k-1}$ which we can compare with each other in $O(1)$ using the information from the previous phase - the values of the equivalence classes $c[]$.
Thus, for two substrings of length $2^k$ starting at position $i$ and $j$, all necessary information to compare them is contained in the pairs $(c[i],~ c[i + 2^{k-1}])$ and $(c[j],~ c[j + 2^{k-1}])$.

$$\dots
\overbrace{
\underbrace{s_i \dots s_{i+2^{k-1}-1}}_{\text{length} = 2^{k-1},~ \text{class} = c[i]}
\quad
\underbrace{s_{i+2^{k-1}} \dots s_{i+2^k-1}}_{\text{length} = 2^{k-1},~ \text{class} = c[i + 2^{k-1}]}
}^{\text{length} = 2^k}
\dots
\overbrace{
\underbrace{s_j \dots s_{j+2^{k-1}-1}}_{\text{length} = 2^{k-1},~ \text{class} = c[j]}
\quad
\underbrace{s_{j+2^{k-1}} \dots s_{j+2^k-1}}_{\text{length} = 2^{k-1},~ \text{class} = c[j + 2^{k-1}]}
}^{\text{length} = 2^k}
\dots
$$

This gives us a very simple solution:
**sort** the substrings of length $2^k$ **by these pairs of numbers**.
This will give us the required order $p[]$.
However a normal sort runs in $O(n \log n)$ time, with which we are not satisfied.
This will only give us an algorithm for constructing a suffix array in $O(n \log^2 n)$ times.

How do we quickly perform such a sorting of the pairs?
Since the elements of the pairs do not exceed $n$, we can use counting sort again.
However sorting pairs with counting sort is not the most efficient.
To achieve a better hidden constant in the complexity, we will use another trick.

We use here the technique on which **radix sort** is based: to sort the pairs we first sort them by the second element, and then by the first element (with a stable sort, i.e. sorting without breaking the relative order of equal elements).
However the second elements were already sorted in the previous iteration.
Thus, in order to sort the pairs by the second elements, we just need to subtract $2^{k-1}$ from the indices in $p[]$ (e.g. if the smallest substring of length $2^{k-1}$ starts at position $i$, then the substring of length $2^k$ with the smallest second half starts at $i - 2^{k-1}$).

So only by simple subtractions we can sort the second elements of the pairs in $p[]$.
Now we need to perform a stable sort by the first elements.
As already mentioned, this can be accomplished with counting sort.

The only thing left is to compute the equivalence classes $c[]$, but as before this can be done by simply iterating over the sorted permutation $p[]$ and comparing neighboring pairs.

Here is the remaining implementation.
We use temporary arrays $pn[]$ and $cn[]$ to store the permutation by the second elements and the new equivalent class indices.

```cpp
    vector<int> pn(n), cn(n);
    for (int h = 0; (1 << h) < n; ++h) {
        for (int i = 0; i < n; i++) {
            pn[i] = p[i] - (1 << h);
            if (pn[i] < 0)
                pn[i] += n;
        }
        fill(cnt.begin(), cnt.begin() + classes, 0);
        for (int i = 0; i < n; i++)
            cnt[c[pn[i]]]++;
        for (int i = 1; i < classes; i++)
            cnt[i] += cnt[i-1];
        for (int i = n-1; i >= 0; i--)
            p[--cnt[c[pn[i]]]] = pn[i];
        cn[p[0]] = 0;
        classes = 1;
        for (int i = 1; i < n; i++) {
            pair<int, int> cur = {c[p[i]], c[(p[i] + (1 << h)) % n]};
            pair<int, int> prev = {c[p[i-1]], c[(p[i-1] + (1 << h)) % n]};
            if (cur != prev)
                ++classes;
            cn[p[i]] = classes - 1;
        }
        c.swap(cn);
    }
    return p;
}
```
অ্যালগরিদম $O(n \log n)$ সময় এবং $O(n)$ মেমোরি প্রয়োজন। সহজতার জন্য আমরা সম্পূর্ণ ASCII পরিসীমা বর্ণমালা হিসাবে ব্যবহার করেছি।

যদি জানা যায় যে স্ট্রিং শুধুমাত্র অক্ষরের একটি উপসেট ধারণ করে, যেমন শুধুমাত্র ছোট অক্ষর, তবে ইমপ্লিমেন্টেশন অপ্টিমাইজ করা যায়, তবে অপ্টিমাইজেশন ফ্যাক্টর সম্ভবত নগণ্য হবে, কারণ বর্ণমালার আকার শুধুমাত্র প্রথম ইটারেশনতে গুরুত্বপূর্ণ। প্রতিটি অন্য ইটারেশন সমতুল্য শ্রেণীর সংখ্যার উপর নির্ভর করে, যা দ্রুত $O(n)$ এ পৌঁছাতে পারে এমনকি যদি শুরুতে এটা আকার 2 এর বর্ণমালা উপর একটি স্ট্রিং ছিল।

এছাড়াও লক্ষ্য করো যে এই অ্যালগরিদম শুধুমাত্র সাইক্লিক পরিবর্তন সাজায়।
এই বিভাগের শুরুতে উল্লেখ করা হয়েছে যে আমরা সাফিক্সের সাজানো ক্রম উৎপন্ন করতে পারি স্ট্রিংয়ের অন্যান্য সমস্ত অক্ষরের চেয়ে ছোট একটি অক্ষর যোগ করে, এবং এই রেজাল্ট স্ট্রিং সাজিয়ে সাইক্লিক পরিবর্তনের মাধ্যমে, যেমন $s + \$$ এর সাইক্লিক পরিবর্তন সাজিয়ে।
এটা স্পষ্টতই $s$ এর সাফিক্স অ্যারে দেবে, তবে $|s|$ দিয়ে প্রিপেন্ড করা।

```cpp
vector<int> suffix_array_construction(string s) {
    s += "$";
    vector<int> sorted_shifts = sort_cyclic_shifts(s);
    sorted_shifts.erase(sorted_shifts.begin());
    return sorted_shifts;
}
```

## অ্যাপ্লিকেশন

### সবচেয়ে ছোট সাইক্লিক স্থানান্তর খুঁজে পাওয়া

উপরের অ্যালগরিদম সমস্ত সাইক্লিক স্থানান্তর সাজায় (স্ট্রিং-এ একটি অক্ষর যোগ না করে), এবং অতএব $p[0]$ সবচেয়ে ছোট সাইক্লিক স্থানান্তরের অবস্থান দেয়।

### একটি স্ট্রিং-এ একটি সাবস্ট্রিং খুঁজে পাওয়া

কাজটি হল কোনো পাঠ্য $t$ এর মধ্যে একটি স্ট্রিং $s$ খুঁজে বের করা অনলাইনে - আমরা পাঠ্য $t$ আগে থেকে জানি, কিন্তু স্ট্রিং $s$ নয়।
আমরা পাঠ্য $t$ এর জন্য সাফিক্স অ্যারে তৈরি করতে পারি $O(|t| \log |t|)$ সময়ে।
এখন আমরা নিচের উপায়ে সাবস্ট্রিং $s$ খুঁজে পেতে পারি।
$s$ এর উপস্থিতি $t$ থেকে কোনো সাফিক্সের প্রিফিক্স হতে হবে।
যেহেতু আমরা সমস্ত সাফিক্স সাজিয়েছি আমরা $p$ তে $s$ এর জন্য একটি বাইনারি সার্চ সম্পাদন করতে পারি।
বাইনারি সার্চের মধ্যে বর্তমান সাফিক্স এবং সাবস্ট্রিং $s$ তুলনা করা $O(|s|)$ সময়ে করা যায়, তাই সাবস্ট্রিং খুঁজে পাওয়ার কমপ্লেক্সিটি $O(|s| \log |t|)$।
এছাড়াও লক্ষ্য করো যে যদি সাবস্ট্রিং $t$ তে একাধিকবার ঘটে, তাহলে সমস্ত উপস্থিতি $p$ তে একসাথে থাকবে।
অতএব উপস্থিতির সংখ্যা একটি দ্বিতীয় বাইনারি সার্চ দিয়ে খুঁজে পাওয়া যায়, এবং সমস্ত উপস্থিতি সহজেই মুদ্রণ করা যায়।

### একটি স্ট্রিংয়ের দুটি সাবস্ট্রিং তুলনা করা

আমরা একটা দেওয়া স্ট্রিং $s$ এর একই দৈর্ঘ্যের দুটি সাবস্ট্রিং $O(1)$ সময়ে তুলনা করতে সক্ষম হতে চাই, অর্থাৎ প্রথম সাবস্ট্রিং দ্বিতীয়টির চেয়ে ছোট কিনা তা যাচাই করা।

এর জন্য আমরা সাফিক্স অ্যারে $O(|s| \log |s|)$ সময়ে নির্মাণ করি এবং সমতুল্য শ্রেণী $c[]$ এর সমস্ত মধ্যবর্তী ফলাফল সংরক্ষণ করি।

এই তথ্য ব্যবহার করে আমরা যেকোনো দুটি সাবস্ট্রিং যার দৈর্ঘ্য দুইয়ের শক্তির সমান O(1) তে তুলনা করতে পারি:
এটির জন্য উভয় সাবস্ট্রিংয়ের সমতুল্য শ্রেণী তুলনা করা যথেষ্ট।
এখন আমরা এই পদ্ধতি স্বেচ্ছাচারী দৈর্ঘ্যের সাবস্ট্রিংয়ে সাধারণীকরণ করতে চাই।

দৈর্ঘ্য $l$ এর দুটি সাবস্ট্রিং তুলনা করি শুরুর সূচক $i$ এবং $j$ সহ।
আমরা এই দৈর্ঘ্যের একটি সাবস্ট্রিংয়ের মধ্যে রাখা একটি ব্লকের বৃহত্তম দৈর্ঘ্য খুঁজি: সবচেয়ে বড় $k$ যেমন $2^k \le l$।
তারপর দুটি সাবস্ট্রিং তুলনা করা দৈর্ঘ্য $2^k$ এর দুটি ওভারল্যাপিং ব্লক তুলনা করে প্রতিস্থাপন করা যায়:
প্রথমে তোমাকে $i$ এবং $j$ থেকে শুরু হওয়া দুটি ব্লক তুলনা করতে হবে, এবং যদি এগুলি সমান হয় তবে অবস্থান $i + l - 1$ এবং $j + l - 1$ এ শেষ হওয়া দুটি ব্লক তুলনা করো:

$$\dots
\overbrace{\underbrace{s_i \dots s_{i+l-2^k} \dots s_{i+2^k-1}}_{2^k} \dots s_{i+l-1}}^{\text{first}}
\dots
\overbrace{\underbrace{s_j \dots s_{j+l-2^k} \dots s_{j+2^k-1}}_{2^k} \dots s_{j+l-1}}^{\text{second}}
\dots$$

$$\dots
\overbrace{s_i \dots \underbrace{s_{i+l-2^k} \dots s_{i+2^k-1} \dots s_{i+l-1}}_{2^k}}^{\text{first}}
\dots
\overbrace{s_j \dots \underbrace{s_{j+l-2^k} \dots s_{j+2^k-1} \dots s_{j+l-1}}_{2^k}}^{\text{second}}
\dots$$

এখানে তুলনার ইমপ্লিমেন্টেশন রয়েছে।
মনে রাখো যে অনুমান করা হয় যে ফাংশন ইতিমধ্যে গণনা করা $k$ দিয়ে বলা হয়।
$k$ কে $\lfloor \log l \rfloor$ দিয়ে গণনা করা যায়, তবে প্রতিটি $l$ এর জন্য সমস্ত $k$ মানগুলি পূর্বডিটারমিন করা আরও দক্ষ।
উদাহরণস্বরূপ [সার্স টেবিল](../data_structures/sparse-table.md) সম্পর্কে আর্টিকেল দেখো, যা একটি অনুরূপ ধারণা ব্যবহার করে এবং সমস্ত $\log$ মানগুলি গণনা করে।

```cpp
int compare(int i, int j, int l, int k) {
    pair<int, int> a = {c[k][i], c[k][(i+l-(1 << k))%n]};
    pair<int, int> b = {c[k][j], c[k][(j+l-(1 << k))%n]};
    return a == b ? 0 : a < b ? -1 : 1;
}
```

### অতিরিক্ত মেমোরি সহ দুটি সাবস্ট্রিংয়ের দীর্ঘতম সাধারণ প্রিফিক্স

একটা দেওয়া স্ট্রিং $s$ এর জন্য আমরা অবস্থান $i$ এবং $j$ সহ দুটি স্বেচ্ছাচারী সাফিক্সের দীর্ঘতম সাধারণ প্রিফিক্স (**LCP**) গণনা করতে চাই।

এখানে বর্ণিত পদ্ধতি $O(|s| \log |s|)$ অতিরিক্ত মেমোরি ব্যবহার করে।
একটি সম্পূর্ণ ভিন্ন পদ্ধতি যা শুধুমাত্র রৈখিক পরিমাণ মেমোরি ব্যবহার করবে তা পরবর্তী বিভাগে বর্ণিত।

We construct the suffix array in $O(|s| \log |s|)$ time, and remember the intermediate results of the arrays $c[]$ from each iteration.

Let's compute the LCP for two suffixes starting at $i$ and $j$.
We can compare any two substrings with a length equal to a power of two in $O(1)$.
To do this, we compare the strings by power of twos (from highest to lowest power) and if the substrings of this length are the same, then we add the equal length to the answer and continue checking for the LCP to the right of the equal part, i.e. $i$ and $j$ get added by the current power of two.

```cpp
int lcp(int i, int j) {
    int ans = 0;
    for (int k = log_n; k >= 0; k--) {
        if (c[k][i % n] == c[k][j % n]) {
            ans += 1 << k;
            i += 1 << k;
            j += 1 << k;
        }
    }
    return ans;
}
```

Here `log_n` denotes a constant that is equal to the logarithm of $n$ in base $2$ rounded down.

### অতিরিক্ত মেমরি ছাড়াই দুটি সাবস্ট্রিং-এর দীর্ঘতম সাধারণ প্রিফিক্স

আমাদের কাছে আগের বিভাগের মতো একই কাজ রয়েছে।
আমরা একটি স্ট্রিং $s$ এর দুটি সাফিক্সের জন্য দীর্ঘতম সাধারণ প্রিফিক্স (**LCP**) গণনা করেছি।

আগের পদ্ধতির বিপরীতে এটা শুধুমাত্র $O(|s|)$ মেমরি ব্যবহার করবে।
প্রিপ্রসেসিং-এর ফলাফল একটি অ্যারে হবে (যা নিজেই স্ট্রিং সম্পর্কে তথ্যের একটি গুরুত্বপূর্ণ উৎস, এবং তাই অন্যান্য কাজ সমাধানের জন্যও ব্যবহৃত হয়)।
LCP কোয়েরিগুলি এই অ্যারেতে RMQ কোয়েরি (রেঞ্জ ন্যূনতম কোয়েরি) সম্পাদন করে উত্তর দেওয়া যায়, তাই বিভিন্ন ইমপ্লিমেন্টেশনের জন্য লগারিদমিক এবং এমনকি ধ্রুবক কোয়েরি সময় অর্জন করা সম্ভব। 

The basis for this algorithm is the following idea:
we will compute the longest common prefix for each **pair of adjacent suffixes in the sorted order**.
In other words we construct an array $\text{lcp}[0 \dots n-2]$, where $\text{lcp}[i]$ is equal to the length of the longest common prefix of the suffixes starting at $p[i]$ and $p[i+1]$.
This array will give us an answer for any two adjacent suffixes of the string.
Then the answer for arbitrary two suffixes, not necessarily neighboring ones, can be obtained from this array.
In fact, let the request be to compute the LCP of the suffixes $p[i]$ and $p[j]$.
Then the answer to this query will be $\min(lcp[i],~ lcp[i+1],~ \dots,~ lcp[j-1])$.

Thus if we have such an array $\text{lcp}$, then the problem is reduced to the [RMQ](../sequences/rmq.md), which has many wide number of different solutions with different complexities.

So the main task is to **build** this array $\text{lcp}$.
We will use **Kasai's algorithm**, which can compute this array in $O(n)$ time.

Let's look at two adjacent suffixes in the sorted order (order of the suffix array).
Let their starting positions be $i$ and $j$ and their $\text{lcp}$ equal to $k > 0$.
If we remove the first letter of both suffixes - i.e. we take the suffixes $i+1$ and $j+1$ - then it should be obvious that the $\text{lcp}$ of these two is $k - 1$.
However we cannot use this value and write it in the $\text{lcp}$ array, because these two suffixes might not be next to each other in the sorted order.
The suffix $i+1$ will of course be smaller than the suffix $j+1$, but there might be some suffixes between them.
However, since we know that the LCP between two suffixes is the minimum value of all transitions, we also know that the LCP between any two pairs in that interval has to be at least $k-1$, especially also between $i+1$ and the next suffix.
And possibly it can be bigger.

Now we already can implement the algorithm.
We will iterate over the suffixes in order of their length. This way we can reuse the last value $k$, since going from suffix $i$ to the suffix $i+1$ is exactly the same as removing the first letter.
We will need an additional array $\text{rank}$, which will give us the position of a suffix in the sorted list of suffixes.

```cpp
vector<int> lcp_construction(string const& s, vector<int> const& p) {
    int n = s.size();
    vector<int> rank(n, 0);
    for (int i = 0; i < n; i++)
        rank[p[i]] = i;

    int k = 0;
    vector<int> lcp(n-1, 0);
    for (int i = 0; i < n; i++) {
        if (rank[i] == n - 1) {
            k = 0;
            continue;
        }
        int j = p[rank[i] + 1];
        while (i + k < n && j + k < n && s[i+k] == s[j+k])
            k++;
        lcp[rank[i]] = k;
        if (k)
            k--;
    }
    return lcp;
}
```

It is easy to see, that we decrease $k$ at most $O(n)$ times (each iteration at most once, except for $\text{rank}[i] == n-1$, where we directly reset it to $0$), and the LCP between two strings is at most $n-1$, we will also increase $k$ only $O(n)$ times.
Therefore the algorithm runs in $O(n)$ time.

### বিভিন্ন সাবস্ট্রিং-এর সংখ্যা

আমরা সাফিক্স অ্যারে এবং LCP অ্যারে গণনা করে স্ট্রিং $s$ প্রিপ্রসেস করি।
এই তথ্য ব্যবহার করে আমরা স্ট্রিং-এ বিভিন্ন সাবস্ট্রিং-এর সংখ্যা গণনা করতে পারি।

এটা করতে, আমরা ভাবব কোন **নতুন** সাবস্ট্রিং অবস্থান $p[0]$ এ শুরু হয়, তারপর $p[1]$ এ, ইত্যাদি।
আসলে আমরা সাফিক্সগুলি সাজানো ক্রমে নিই এবং দেখি কোন প্রিফিক্সগুলি নতুন সাবস্ট্রিং দেয়।
এইভাবে আমরা দুর্ঘটনাক্রমে কোনটা উপেক্ষা করব না।

যেহেতু সাফিক্সগুলি সাজানো আছে, এটা স্পষ্ট যে বর্তমান সাফিক্স $p[i]$ এর সমস্ত প্রিফিক্সের জন্য নতুন সাবস্ট্রিং দেবে, প্রথম $\text{lcp}[i-1]$ প্রিফিক্সের কাছাকাছি যে সাফিক্স $p[i-1]$ সঙ্গে মিলে।
অতএব, এর সমস্ত প্রিফিক্স প্রথম $\text{lcp}[i-1]$ একটি ব্যতিক্রমী।
বর্তমান সাফিক্সের দৈর্ঘ্য $n - p[i]$ হওয়ায়, $n - p[i] - \text{lcp}[i-1]$ নতুন প্রিফিক্স $p[i]$ তে শুরু হয়।
সমস্ত সাফিক্সের উপর যোগফল, আমরা চূড়ান্ত উত্তর পাই:

$$\sum_{i=0}^{n-1} (n - p[i]) - \sum_{i=0}^{n-2} \text{lcp}[i] = \frac{n^2 + n}{2} - \sum_{i=0}^{n-2} \text{lcp}[i]$$

## অনুশীলন সমস্যা

* [Uva 760 - DNA Sequencing](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=701)
* [Uva 1223 - Editor](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3664)
* [Codechef - Tandem](https://www.codechef.com/problems/TANDEM)
* [Codechef - Substrings and Repetitions](https://www.codechef.com/problems/ANUSAR)
* [Codechef - Entangled Strings](https://www.codechef.com/problems/TANGLED)
* [Codeforces - Martian Strings](http://codeforces.com/problemset/problem/149/E)
* [Codeforces - Little Elephant and Strings](http://codeforces.com/problemset/problem/204/E)
* [SPOJ - Ada and Terramorphing](http://www.spoj.com/problems/ADAPHOTO/)
* [SPOJ - Ada and Substring](http://www.spoj.com/problems/ADASTRNG/)
* [UVA - 1227 - The longest constant gene](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3668)
* [SPOJ - Longest Common Substring](http://www.spoj.com/problems/LCS/en/)
* [UVA 11512 - GATTACA](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2507)
* [LA 7502 - Suffixes and Palindromes](https://vjudge.net/problem/UVALive-7502)
* [GYM - Por Costel and the Censorship Committee](http://codeforces.com/gym/100923/problem/D)
* [UVA 1254 - Top 10](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3695)
* [UVA 12191 - File Recover](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3343)
* [UVA 12206 - Stammering Aliens](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3358)
* [Codechef - Jarvis and LCP](https://www.codechef.com/problems/INSQ16F)
* [LA 3943 - Liking's Letter](https://vjudge.net/problem/UVALive-3943)
* [UVA 11107 - Life Forms](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2048)
* [UVA 12974 - Exquisite Strings](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4853)
* [UVA 10526 - Intellectual Property](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1467)
* [UVA 12338 - Anti-Rhyme Pairs](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3760)
* [UVA 12191 - File Recover](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3343)
* [SPOJ - Suffix Array](http://www.spoj.com/problems/SARRAY/)
* [LA 4513 - Stammering Aliens](https://vjudge.net/problem/UVALive-4513)
* [SPOJ - LCS2](http://www.spoj.com/problems/LCS2/)
* [Codeforces - Fake News (hard)](http://codeforces.com/contest/802/problem/I)
* [SPOJ - Longest Commong Substring](http://www.spoj.com/problems/LONGCS/)
* [SPOJ - Lexicographical Substring Search](http://www.spoj.com/problems/SUBLEX/)
* [Codeforces - Forbidden Indices](http://codeforces.com/contest/873/problem/F)
* [Codeforces - Tricky and Clever Password](http://codeforces.com/contest/30/problem/E)
* [LA 6856 - Circle of digits](https://vjudge.net/problem/UVALive-6856)
