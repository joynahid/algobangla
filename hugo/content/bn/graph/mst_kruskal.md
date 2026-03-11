---
title: "মিনিমাম স্প্যানিং ট্রি - ক্রুস্কালের অ্যালগরিদম"
tags: 
weight: 20
---
# মিনিমাম স্প্যানিং ট্রি - ক্রুস্কালের অ্যালগরিদম

একটি ওয়েটেড আনডিরেক্টেড গ্রাফ দেওয়া আছে।
আমরা এই গ্রাফের এমন একটি সাবট্রি খুঁজতে চাই যেটি সকল ভার্টেক্সকে সংযুক্ত করে (অর্থাৎ এটি একটি স্প্যানিং ট্রি) এবং সকল সম্ভাব্য স্প্যানিং ট্রির মধ্যে এর ওয়েট সর্বনিম্ন (অর্থাৎ সকল এজের ওয়েটের যোগফল ন্যূনতম)।
এই স্প্যানিং ট্রিকে মিনিমাম স্প্যানিং ট্রি বলা হয়।

বাম ছবিতে আপনি একটি ওয়েটেড আনডিরেক্টেড গ্রাফ দেখতে পাচ্ছেন, এবং ডান ছবিতে সংশ্লিষ্ট মিনিমাম স্প্যানিং ট্রি দেখতে পাচ্ছেন।

![Random graph](/images/graph/MST_before.png) ![MST of this graph](/images/graph/MST_after.png)

এই নিবন্ধে মিনিমাম স্প্যানিং ট্রি সম্পর্কিত কিছু গুরুত্বপূর্ণ তথ্য আলোচনা করা হবে, এবং তারপর মিনিমাম স্প্যানিং ট্রি খুঁজে বের করার জন্য ক্রুস্কালের অ্যালগরিদমের সবচেয়ে সরল ইমপ্লিমেন্টেশন দেওয়া হবে।

## মিনিমাম স্প্যানিং ট্রির বৈশিষ্ট্য

* একটি গ্রাফের মিনিমাম স্প্যানিং ট্রি অনন্য হয়, যদি সকল এজের ওয়েট ভিন্ন হয়। অন্যথায়, একাধিক মিনিমাম স্প্যানিং ট্রি থাকতে পারে।
  (নির্দিষ্ট অ্যালগরিদমগুলো সাধারণত সম্ভাব্য মিনিমাম স্প্যানিং ট্রিগুলোর মধ্যে একটি আউটপুট দেয়)।
* মিনিমাম স্প্যানিং ট্রি হলো সেই ট্রিও যেটিতে এজের ওয়েটের গুণফল ন্যূনতম।
  (সকল এজের ওয়েটকে তাদের লগারিদম দিয়ে প্রতিস্থাপন করে এটি সহজেই প্রমাণ করা যায়)
* একটি গ্রাফের মিনিমাম স্প্যানিং ট্রিতে, একটি এজের সর্বোচ্চ ওয়েট সেই গ্রাফের সকল সম্ভাব্য স্প্যানিং ট্রি থেকে ন্যূনতম সম্ভাব্য।
  (এটি ক্রুস্কালের অ্যালগরিদমের বৈধতা থেকে অনুসরণ করে)।
* একটি গ্রাফের ম্যাক্সিমাম স্প্যানিং ট্রি (এজের ওয়েটের যোগফল সর্বোচ্চ এমন স্প্যানিং ট্রি) মিনিমাম স্প্যানিং ট্রির অনুরূপভাবে পাওয়া যায়, সকল এজের ওয়েটের চিহ্ন বিপরীত করে এবং তারপর যেকোনো মিনিমাম স্প্যানিং ট্রি অ্যালগরিদম প্রয়োগ করে।

## ক্রুস্কালের অ্যালগরিদম

এই অ্যালগরিদমটি জোসেফ বার্নার্ড ক্রুস্কাল, জুনিয়র ১৯৫৬ সালে বর্ণনা করেন।

ক্রুস্কালের অ্যালগরিদম প্রথমে মূল গ্রাফের সকল নোডকে পরস্পর থেকে বিচ্ছিন্ন রাখে, একক নোড ট্রির একটি ফরেস্ট তৈরি করে, এবং তারপর ধীরে ধীরে এই ট্রিগুলো মার্জ করে, প্রতিটি ইটারেশনে মূল গ্রাফের কোনো এজ দিয়ে সকল ট্রির মধ্যে যেকোনো দুটিকে একত্রিত করে। অ্যালগরিদম কার্যকর করার আগে, সকল এজ ওয়েট অনুসারে সর্ট করা হয় (অ-হ্রাসমান ক্রমে)। তারপর ইউনিফিকেশনের প্রক্রিয়া শুরু হয়: প্রথম থেকে শেষ পর্যন্ত সকল এজ (সর্টেড ক্রমে) নেওয়া হয়, এবং যদি বর্তমানে নেওয়া এজের প্রান্তগুলো ভিন্ন সাবট্রিতে থাকে, তাহলে সেই সাবট্রিগুলো একত্রিত করা হয় এবং এজটি উত্তরে যোগ করা হয়। সকল এজ ইটারেট করার পর, সকল ভার্টেক্স একই সাব-ট্রিতে থাকবে এবং আমরা উত্তর পাব।

## সবচেয়ে সরল ইমপ্লিমেন্টেশন

নিচের কোডটি উপরে বর্ণিত অ্যালগরিদমটি সরাসরি ইমপ্লিমেন্ট করে, এবং এর টাইম কমপ্লেক্সিটি $O(M \log M + N^2)$।
এজ সর্ট করতে $O(M \log N)$ ($O(M \log M)$-এর সমান) অপারেশন প্রয়োজন।
একটি ভার্টেক্স কোন সাবট্রিতে আছে সেই তথ্য `tree_id[]` অ্যারের সাহায্যে রাখা হয় - প্রতিটি ভার্টেক্স `v`-এর জন্য, `tree_id[v]` সেই ট্রির নম্বর সংরক্ষণ করে যেটিতে `v` আছে।
প্রতিটি এজের জন্য, এটি ভিন্ন ট্রির প্রান্তে আছে কিনা তা $O(1)$-এ নির্ণয় করা যায়।
সবশেষে, দুটি ট্রির ইউনিয়ন `tree_id[]` অ্যারের মধ্য দিয়ে একটি সাধারণ পাস করে $O(N)$-এ সম্পন্ন হয়।
মোট মার্জ অপারেশনের সংখ্যা $N-1$ হওয়ায়, আমরা $O(M \log N + N^2)$ অ্যাসিম্পটোটিক আচরণ পাই।

```cpp
struct Edge {
    int u, v, weight;
    bool operator<(Edge const& other) {
        return weight < other.weight;
    }
};

int n;
vector<Edge> edges;

int cost = 0;
vector<int> tree_id(n);
vector<Edge> result;
for (int i = 0; i < n; i++)
    tree_id[i] = i;

sort(edges.begin(), edges.end());

for (Edge e : edges) {
    if (tree_id[e.u] != tree_id[e.v]) {
        cost += e.weight;
        result.push_back(e);

        int old_id = tree_id[e.u], new_id = tree_id[e.v];
        for (int i = 0; i < n; i++) {
            if (tree_id[i] == old_id)
                tree_id[i] = new_id;
        }
    }
}
```

## সঠিকতার প্রমাণ

কেন ক্রুস্কালের অ্যালগরিদম আমাদের সঠিক ফলাফল দেয়?

যদি মূল গ্রাফটি সংযুক্ত হয়, তাহলে ফলাফল গ্রাফটিও সংযুক্ত হবে।
কারণ অন্যথায় দুটি কম্পোনেন্ট থাকত যেগুলো অন্তত একটি এজ দিয়ে সংযুক্ত করা যেত। কিন্তু এটি অসম্ভব, কারণ ক্রুস্কাল সেই এজগুলোর একটি নির্বাচন করত, যেহেতু কম্পোনেন্টগুলোর আইডি ভিন্ন।
এছাড়াও ফলাফল গ্রাফে কোনো সাইকেল নেই, কারণ আমরা অ্যালগরিদমে স্পষ্টভাবে এটি নিষেধ করি।
অতএব অ্যালগরিদমটি একটি স্প্যানিং ট্রি তৈরি করে।

তাহলে কেন এই অ্যালগরিদম আমাদের একটি মিনিমাম স্প্যানিং ট্রি দেয়?

আমরা ইন্ডাকশন ব্যবহার করে প্রমাণ করতে পারি যে "যদি $F$ হলো অ্যালগরিদমের যেকোনো পর্যায়ে নির্বাচিত এজের সেট, তাহলে একটি এমএসটি আছে যেটি $F$-এর সকল এজ ধারণ করে"।

প্রস্তাবনাটি শুরুতে স্পষ্টতই সত্য, খালি সেট যেকোনো এমএসটি-র সাবসেট।

এখন ধরা যাক $F$ হলো অ্যালগরিদমের যেকোনো পর্যায়ে কোনো এজ সেট, $T$ হলো $F$ ধারণকারী একটি এমএসটি এবং $e$ হলো নতুন এজ যেটি আমরা ক্রুস্কাল ব্যবহার করে যোগ করতে চাই।

যদি $e$ একটি সাইকেল তৈরি করে, তাহলে আমরা এটি যোগ করি না, এবং তাই এই ধাপের পরেও প্রস্তাবনাটি সত্য।

যদি $T$ ইতিমধ্যে $e$ ধারণ করে, তাহলেও এই ধাপের পরে প্রস্তাবনাটি সত্য।

যদি $T$ এজ $e$ ধারণ না করে, তাহলে $T + e$ একটি সাইকেল $C$ ধারণ করবে।
এই সাইকেলে অন্তত একটি এজ $f$ থাকবে, যেটি $F$-তে নেই।
$T - f + e$ এজ সেটটিও একটি স্প্যানিং ট্রি হবে।
লক্ষ্য করুন যে $f$-এর ওয়েট $e$-এর ওয়েটের চেয়ে ছোট হতে পারে না, কারণ তাহলে ক্রুস্কাল আগেই $f$ নির্বাচন করত।
এর ওয়েট বড়ও হতে পারে না, কারণ তাহলে $T - f + e$-এর মোট ওয়েট $T$-এর মোট ওয়েটের চেয়ে ছোট হত, যা অসম্ভব কারণ $T$ ইতিমধ্যে একটি এমএসটি।
এর মানে হলো $e$-এর ওয়েট $f$-এর ওয়েটের সমান হতে হবে।
অতএব $T - f + e$-ও একটি এমএসটি, এবং এটি $F + e$-এর সকল এজ ধারণ করে।
সুতরাং এখানেও ধাপের পরে প্রস্তাবনাটি পূরণ হয়।

এটি প্রস্তাবনাটি প্রমাণ করে।
যার অর্থ হলো সকল এজ ইটারেট করার পর ফলাফল এজ সেট সংযুক্ত হবে, এবং একটি এমএসটি-তে ধারণকৃত হবে, যার মানে এটি ইতিমধ্যেই একটি এমএসটি।

## উন্নত ইমপ্লিমেন্টেশন

আমরা [**ডিসজয়েন্ট সেট ইউনিয়ন** (ডিএসইউ)](../data_structures/disjoint_set_union.md) ডেটা স্ট্রাকচার ব্যবহার করে ক্রুস্কালের অ্যালগরিদমের একটি দ্রুততর ইমপ্লিমেন্টেশন লিখতে পারি যার টাইম কমপ্লেক্সিটি প্রায় $O(M \log N)$। [এই নিবন্ধে](mst_kruskal_with_dsu.md) এই পদ্ধতিটি বিস্তারিত বর্ণনা করা হয়েছে।

## অনুশীলন সমস্যা

* [SPOJ - Koicost](http://www.spoj.com/problems/KOICOST/)
* [SPOJ - MaryBMW](http://www.spoj.com/problems/MARYBMW/)
* [Codechef - Fullmetal Alchemist](https://www.codechef.com/ICL2016/problems/ICL16A)
* [Codeforces - Edges in MST](http://codeforces.com/contest/160/problem/D)
* [UVA 12176 - Bring Your Own Horse](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3328)
* [UVA 10600 - ACM Contest and Blackout](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1541)
* [UVA 10724 - Road Construction](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1665)
* [Hackerrank - Roads in HackerLand](https://www.hackerrank.com/contests/june-world-codesprint/challenges/johnland/problem)
* [UVA 11710 - Expensive subway](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2757)
* [Codechef - Chefland and Electricity](https://www.codechef.com/problems/CHEFELEC)
* [UVA 10307 - Killing Aliens in Borg Maze](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1248)
* [Codeforces - Flea](http://codeforces.com/problemset/problem/32/C)
* [Codeforces - Igon in Museum](http://codeforces.com/problemset/problem/598/D)
* [Codeforces - Hongcow Builds a Nation](http://codeforces.com/problemset/problem/744/A)
* [UVA - 908 - Re-connecting Computer Sites](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=849)
* [UVA 1208 - Oreon](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3649)
* [UVA 1235 - Anti Brute Force Lock](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3676)
* [UVA 10034 - Freckles](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=975)
* [UVA 11228 - Transportation system](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2169)
* [UVA 11631 - Dark roads](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2678)
* [UVA 11733 - Airports](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2833)
* [UVA 11747 - Heavy Cycle Edges](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2847)
* [SPOJ - Blinet](http://www.spoj.com/problems/BLINNET/)
* [SPOJ - Help the Old King](http://www.spoj.com/problems/IITKWPCG/)
* [Codeforces - Hierarchy](http://codeforces.com/contest/17/problem/B)
* [SPOJ - Modems](https://www.spoj.com/problems/EC_MODE/)
* [CSES - Road Reparation](https://cses.fi/problemset/task/1675)
* [CSES - Road Construction](https://cses.fi/problemset/task/1676)
