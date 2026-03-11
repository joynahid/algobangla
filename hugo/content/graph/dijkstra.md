---
title: "ডায়াক্সট্রা অ্যালগরিদম"
tags: 
weight: 10
---
# ডায়াক্সট্রা অ্যালগরিদম

আপনাকে $n$ টি ভার্টেক্স এবং $m$ টি এজবিশিষ্ট একটি ডিরেক্টেড বা আনডিরেক্টেড ওয়েটেড গ্রাফ দেওয়া আছে। সব এজের ওয়েট নন-নেগেটিভ। আপনাকে একটি সোর্স ভার্টেক্স $s$-ও দেওয়া আছে। এই আর্টিকেলে সোর্স ভার্টেক্স $s$ থেকে অন্য সব ভার্টেক্সে শর্টেস্ট পাথের দৈর্ঘ্য বের করা এবং শর্টেস্ট পাথগুলো নিজেই আউটপুট করা নিয়ে আলোচনা করা হয়েছে।

এই সমস্যাটিকে **সিঙ্গেল-সোর্স শর্টেস্ট পাথ** সমস্যাও বলা হয়।

## অ্যালগরিদম

এটি ডাচ কম্পিউটার বিজ্ঞানী Edsger W. Dijkstra কর্তৃক ১৯৫৯ সালে বর্ণিত একটি অ্যালগরিদম।

ধরি, একটি অ্যারে $d[]$ তৈরি করা হলো যেখানে প্রতিটি ভার্টেক্স $v$-এর জন্য $s$ থেকে $v$-তে বর্তমান শর্টেস্ট পাথের দৈর্ঘ্য $d[v]$-তে সংরক্ষিত থাকবে।
প্রাথমিকভাবে $d[s] = 0$, এবং অন্য সব ভার্টেক্সের জন্য এই দৈর্ঘ্য অসীম (infinity)।
ইমপ্লিমেন্টেশনে অসীমের পরিবর্তে যথেষ্ট বড় একটি সংখ্যা বেছে নেওয়া হয় (যা যেকোনো সম্ভাব্য পাথের দৈর্ঘ্যের চেয়ে বড় হওয়া নিশ্চিত)।

$$d[v] = \infty,~ v \ne s$$

এছাড়াও, একটি বুলিয়ান অ্যারে $u[]$ রাখা হয় যেখানে প্রতিটি ভার্টেক্স $v$-এর জন্য সংরক্ষিত থাকে যে এটি মার্কড কি না। প্রাথমিকভাবে সব ভার্টেক্স আনমার্কড:

$$u[v] = {\rm false}$$

ডায়াক্সট্রা অ্যালগরিদম $n$ টি ইটারেশনে চলে। প্রতিটি ইটারেশনে একটি ভার্টেক্স $v$ বেছে নেওয়া হয় যেটি আনমার্কড এবং যার $d[v]$-এর মান সবচেয়ে কম:

স্পষ্টতই, প্রথম ইটারেশনে সোর্স ভার্টেক্স $s$ নির্বাচিত হবে।

নির্বাচিত ভার্টেক্স $v$ কে মার্কড করা হয়। এরপর, ভার্টেক্স $v$ থেকে **রিলাক্সেশন** সম্পন্ন করা হয়: $(v,\text{to})$ আকারের সব এজ বিবেচনা করা হয়, এবং প্রতিটি ভার্টেক্স $\text{to}$-এর জন্য অ্যালগরিদম $d[\text{to}]$-এর মান উন্নত করার চেষ্টা করে। বর্তমান এজের দৈর্ঘ্য যদি $len$ হয়, তাহলে রিলাক্সেশনের কোড হলো:

$$d[\text{to}] = \min (d[\text{to}], d[v] + len)$$

এই ধরনের সব এজ বিবেচনা করার পর বর্তমান ইটারেশন শেষ হয়। অবশেষে, $n$ টি ইটারেশনের পর সব ভার্টেক্স মার্কড হয়ে যাবে এবং অ্যালগরিদম সমাপ্ত হবে। আমরা দাবি করি যে প্রাপ্ত $d[v]$ মানগুলো $s$ থেকে সব ভার্টেক্স $v$-তে শর্টেস্ট পাথের দৈর্ঘ্য।

লক্ষ্য করুন, সোর্স ভার্টেক্স $s$ থেকে কিছু ভার্টেক্স যদি অ্যাক্সেসযোগ্য না হয়, তাহলে সেগুলোর $d[v]$ মান অসীমই থাকবে। স্পষ্টতই, অ্যালগরিদমের শেষ কয়েকটি ইটারেশন ওই ভার্টেক্সগুলো নির্বাচন করবে, কিন্তু তাদের জন্য কোনো কাজের কাজ হবে না। তাই, নির্বাচিত ভার্টেক্সের দূরত্ব অসীম হলেই অ্যালগরিদম থামিয়ে দেওয়া যেতে পারে।

### শর্টেস্ট পাথ পুনরুদ্ধার

সাধারণত শুধু শর্টেস্ট পাথের দৈর্ঘ্যই নয়, বরং শর্টেস্ট পাথগুলো নিজেও জানা দরকার হয়। দেখা যাক কীভাবে $s$ থেকে যেকোনো ভার্টেক্সে শর্টেস্ট পাথ পুনরুদ্ধার করার জন্য পর্যাপ্ত তথ্য সংরক্ষণ করা যায়। আমরা একটি প্রিডিসেসর অ্যারে $p[]$ রাখব যেখানে প্রতিটি ভার্টেক্স $v \ne s$-এর জন্য, $p[v]$ হলো $s$ থেকে $v$-তে শর্টেস্ট পাথের শেষ থেকে দ্বিতীয় ভার্টেক্স। এখানে আমরা এই তথ্যটি ব্যবহার করি যে, কোনো ভার্টেক্স $v$-তে শর্টেস্ট পাথ নিয়ে $v$ সরিয়ে দিলে আমরা $p[v]$-তে শেষ হওয়া একটি পাথ পাই, এবং এই পাথটি $p[v]$ ভার্টেক্সের জন্য শর্টেস্ট পাথ। এই প্রিডিসেসর অ্যারে ব্যবহার করে যেকোনো ভার্টেক্সে শর্টেস্ট পাথ পুনরুদ্ধার করা যায়: $v$ থেকে শুরু করে বারবার বর্তমান ভার্টেক্সের প্রিডিসেসর নিতে থাকুন যতক্ষণ না সোর্স ভার্টেক্স $s$-এ পৌঁছান, এতে বিপরীত ক্রমে তালিকাভুক্ত ভার্টেক্সসহ প্রয়োজনীয় শর্টেস্ট পাথ পাওয়া যাবে। সুতরাং, ভার্টেক্স $v$-তে শর্টেস্ট পাথ $P$ হলো:

$$P = (s, \ldots, p[p[p[v]]], p[p[v]], p[v], v)$$

এই প্রিডিসেসর অ্যারে তৈরি করা খুবই সহজ: প্রতিটি সফল রিলাক্সেশনের সময়, অর্থাৎ যখন কোনো নির্বাচিত ভার্টেক্স $v$-এর জন্য কোনো ভার্টেক্স $\text{to}$-এর দূরত্বে উন্নতি হয়, তখন $\text{to}$-এর প্রিডিসেসর ভার্টেক্স $v$ দিয়ে আপডেট করি:

$$p[\text{to}] = v$$

## প্রমাণ

ডায়াক্সট্রা অ্যালগরিদমের সঠিকতা যে মূল দাবির উপর ভিত্তি করে তা হলো:

**যেকোনো ভার্টেক্স $v$ মার্কড হওয়ার পর, তার বর্তমান দূরত্ব $d[v]$ শর্টেস্ট, এবং এটি আর পরিবর্তন হবে না।**

প্রমাণটি ইন্ডাকশনের মাধ্যমে করা হয়। প্রথম ইটারেশনের জন্য এই বিবৃতি স্পষ্ট: একমাত্র মার্কড ভার্টেক্স হলো $s$, এবং এর দূরত্ব $d[s] = 0$ যা প্রকৃতপক্ষে $s$-এর শর্টেস্ট পাথের দৈর্ঘ্য। এখন ধরি, এই বিবৃতি পূর্ববর্তী সব ইটারেশনের জন্য সত্য, অর্থাৎ ইতোমধ্যে মার্কড সব ভার্টেক্সের জন্য; প্রমাণ করা যাক যে বর্তমান ইটারেশন সম্পন্ন হলেও এটি লঙ্ঘিত হয় না। ধরি $v$ হলো বর্তমান ইটারেশনে নির্বাচিত ভার্টেক্স, অর্থাৎ $v$ হলো সেই ভার্টেক্স যাকে অ্যালগরিদম মার্ক করবে। এখন আমাদের প্রমাণ করতে হবে যে $d[v]$ প্রকৃতপক্ষে এর শর্টেস্ট পাথের দৈর্ঘ্য $l[v]$-এর সমান।

ভার্টেক্স $v$-তে শর্টেস্ট পাথ $P$ বিবেচনা করুন। এই পাথকে দুটি অংশে ভাগ করা যায়: $P_1$ যা শুধুমাত্র মার্কড নোড নিয়ে গঠিত (অন্তত সোর্স ভার্টেক্স $s$ হলো $P_1$-এর অংশ), এবং বাকি পাথ $P_2$ (এতে একটি মার্কড ভার্টেক্স থাকতে পারে, তবে এটি সবসময় একটি আনমার্কড ভার্টেক্স দিয়ে শুরু হয়)। ধরি $P_2$ পাথের প্রথম ভার্টেক্স $p$ এবং $P_1$ পাথের শেষ ভার্টেক্স $q$।

প্রথমে আমরা ভার্টেক্স $p$-এর জন্য আমাদের বিবৃতি প্রমাণ করি, অর্থাৎ প্রমাণ করা যাক যে $d[p] = l[p]$।
এটি প্রায় স্পষ্ট: পূর্ববর্তী কোনো এক ইটারেশনে আমরা ভার্টেক্স $q$ নির্বাচন করেছিলাম এবং তা থেকে রিলাক্সেশন করেছিলাম।
যেহেতু (ভার্টেক্স $p$-এর নির্বাচনের কারণে) $p$-এর শর্টেস্ট পাথ হলো $q$-এর শর্টেস্ট পাথ যোগ এজ $(p,q)$, তাই $q$ থেকে রিলাক্সেশন $d[p]$-এর মান শর্টেস্ট পাথের দৈর্ঘ্য $l[p]$-তে সেট করেছে।

যেহেতু এজের ওয়েটগুলো নন-নেগেটিভ, শর্টেস্ট পাথের দৈর্ঘ্য $l[p]$ (যা আমরা এইমাত্র প্রমাণ করলাম $d[p]$-এর সমান) ভার্টেক্স $v$-তে শর্টেস্ট পাথের দৈর্ঘ্য $l[v]$-এর চেয়ে বেশি নয়। যেহেতু $l[v] \le d[v]$ (কারণ ডায়াক্সট্রা অ্যালগরিদম সম্ভাব্য সর্বনিম্নের চেয়ে ছোট পথ খুঁজে পেতে পারে না), আমরা পাই:

$$d[p] = l[p] \le l[v] \le d[v]$$

অন্যদিকে, যেহেতু $p$ এবং $v$ উভয়ই আনমার্কড, এবং বর্তমান ইটারেশনে $p$ নয় বরং ভার্টেক্স $v$ নির্বাচিত হয়েছে, আমরা আরেকটি অসমতা পাই:

$$d[p] \ge d[v]$$

এই দুটি অসমতা থেকে আমরা সিদ্ধান্তে আসি যে $d[p] = d[v]$, এবং তারপর পূর্বে প্রাপ্ত সমীকরণগুলো থেকে পাই:

$$d[v] = l[v]$$

প্রমাণ সম্পন্ন।

## ইমপ্লিমেন্টেশন

ডায়াক্সট্রা অ্যালগরিদম $n$ টি ইটারেশন সম্পন্ন করে। প্রতিটি ইটারেশনে এটি সবচেয়ে কম $d[v]$ মানবিশিষ্ট একটি আনমার্কড ভার্টেক্স $v$ নির্বাচন করে, একে মার্ক করে এবং সব এজ $(v, \text{to})$ পরীক্ষা করে $d[\text{to}]$-এর মান উন্নত করার চেষ্টা করে।

অ্যালগরিদমের রানিং টাইম নিম্নলিখিত অংশ নিয়ে গঠিত:

* $O(n)$ টি আনমার্কড ভার্টেক্সের মধ্যে সবচেয়ে ছোট $d[v]$ মানের ভার্টেক্স খোঁজার জন্য $n$ বার সার্চ
* $m$ বার রিলাক্সেশনের চেষ্টা

এই অপারেশনগুলোর সবচেয়ে সরল ইমপ্লিমেন্টেশনে প্রতিটি ইটারেশনে ভার্টেক্স সার্চে $O(n)$ অপারেশন লাগে এবং প্রতিটি রিলাক্সেশন $O(1)$-এ সম্পন্ন করা যায়। ফলে অ্যালগরিদমের অ্যাসিম্পটটিক কমপ্লেক্সিটি হলো:

$$O(n^2+m)$$

ডেন্স গ্রাফের জন্য, অর্থাৎ যখন $m \approx n^2$, এই কমপ্লেক্সিটি অপটিমাল।
তবে স্পার্স গ্রাফে, যখন $m$ সর্বোচ্চ এজ সংখ্যা $n^2$-এর তুলনায় অনেক ছোট, সমস্যাটি $O(n \log n + m)$ কমপ্লেক্সিটিতে সমাধান করা যায়। সেই অ্যালগরিদম ও ইমপ্লিমেন্টেশন [স্পার্স গ্রাফে ডায়াক্সট্রা](dijkstra_sparse.md) আর্টিকেলে পাওয়া যাবে।


```cpp
const int INF = 1000000000;
vector<vector<pair<int, int>>> adj;

void dijkstra(int s, vector<int> & d, vector<int> & p) {
    int n = adj.size();
    d.assign(n, INF);
    p.assign(n, -1);
    vector<bool> u(n, false);

    d[s] = 0;
    for (int i = 0; i < n; i++) {
        int v = -1;
        for (int j = 0; j < n; j++) {
            if (!u[j] && (v == -1 || d[j] < d[v]))
                v = j;
        }

        if (d[v] == INF)
            break;

        u[v] = true;
        for (auto edge : adj[v]) {
            int to = edge.first;
            int len = edge.second;

            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                p[to] = v;
            }
        }
    }
}
```

এখানে গ্রাফ $\text{adj}$ অ্যাডজেসেন্সি লিস্ট হিসেবে সংরক্ষিত: প্রতিটি ভার্টেক্স $v$-এর জন্য $\text{adj}[v]$-তে এই ভার্টেক্স থেকে বের হওয়া এজগুলোর লিস্ট রয়েছে, অর্থাৎ `pair<int,int>`-এর লিস্ট যেখানে পেয়ারের প্রথম উপাদান হলো এজের অপর প্রান্তের ভার্টেক্স এবং দ্বিতীয় উপাদান হলো এজের ওয়েট।

ফাংশনটি সোর্স ভার্টেক্স $s$ এবং দুটি ভেক্টর নেয় যা রিটার্ন ভ্যালু হিসেবে ব্যবহৃত হবে।

প্রথমে কোড অ্যারেগুলো ইনিশিয়ালাইজ করে: দূরত্ব $d[]$, লেবেল $u[]$ এবং প্রিডিসেসর $p[]$। তারপর এটি $n$ টি ইটারেশন চালায়। প্রতিটি ইটারেশনে সব আনমার্কড ভার্টেক্সের মধ্যে সবচেয়ে ছোট দূরত্ব $d[v]$ বিশিষ্ট ভার্টেক্স $v$ নির্বাচন করা হয়। নির্বাচিত ভার্টেক্স $v$-এর দূরত্ব অসীম হলে অ্যালগরিদম থেমে যায়। অন্যথায় ভার্টেক্সটি মার্ক করা হয়, এবং এই ভার্টেক্স থেকে বের হওয়া সব এজ পরীক্ষা করা হয়। এজ বরাবর রিলাক্সেশন সম্ভব হলে (অর্থাৎ দূরত্ব $d[\text{to}]$ উন্নত করা গেলে), দূরত্ব $d[\text{to}]$ এবং প্রিডিসেসর $p[\text{to}]$ আপডেট করা হয়।

সব ইটারেশন সম্পন্ন হওয়ার পর অ্যারে $d[]$-তে সব ভার্টেক্সে শর্টেস্ট পাথের দৈর্ঘ্য সংরক্ষিত থাকে, এবং অ্যারে $p[]$-তে সব ভার্টেক্সের প্রিডিসেসর সংরক্ষিত থাকে (সোর্স ভার্টেক্স $s$ ব্যতীত)। যেকোনো ভার্টেক্স $t$-এর পাথ নিম্নলিখিত উপায়ে পুনরুদ্ধার করা যায়:

```cpp
vector<int> restore_path(int s, int t, vector<int> const& p) {
    vector<int> path;

    for (int v = t; v != s; v = p[v])
        path.push_back(v);
    path.push_back(s);

    reverse(path.begin(), path.end());
    return path;
}
```

## রেফারেন্স

* Edsger Dijkstra. A note on two problems in connexion with graphs [1959]
* Thomas Cormen, Charles Leiserson, Ronald Rivest, Clifford Stein. Introduction to Algorithms [2005]

## অনুশীলন সমস্যা
* [Timus - Ivan's Car](http://acm.timus.ru/problem.aspx?space=1&num=1930) [Difficulty:Medium]
* [Timus - Sightseeing Trip](http://acm.timus.ru/problem.aspx?space=1&num=1004)
* [SPOJ - SHPATH](http://www.spoj.com/problems/SHPATH/) [Difficulty:Easy]
* [Codeforces - Dijkstra?](http://codeforces.com/problemset/problem/20/C) [Difficulty:Easy]
* [Codeforces - Shortest Path](http://codeforces.com/problemset/problem/59/E)
* [Codeforces - Jzzhu and Cities](http://codeforces.com/problemset/problem/449/B)
* [Codeforces - The Classic Problem](http://codeforces.com/problemset/problem/464/E)
* [Codeforces - President and Roads](http://codeforces.com/problemset/problem/567/E)
* [Codeforces - Complete The Graph](http://codeforces.com/problemset/problem/715/B)
* [TopCoder - SkiResorts](https://community.topcoder.com/stat?c=problem_statement&pm=12468)
* [TopCoder - MaliciousPath](https://community.topcoder.com/stat?c=problem_statement&pm=13596)
* [SPOJ - Ada and Trip](http://www.spoj.com/problems/ADATRIP/)
* [LA - 3850 - Here We Go(relians) Again](https://vjudge.net/problem/UVALive-3850)
* [GYM - Destination Unknown (D)](http://codeforces.com/gym/100625)
* [UVA 12950 - Even Obsession](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=4829)
* [GYM - Journey to Grece (A)](http://codeforces.com/gym/100753)
* [UVA 13030 - Brain Fry](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=866&page=show_problem&problem=4918)
* [UVA 1027 - Toll](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3468)
* [UVA 11377 - Airport Setup](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2372)
* [Codeforces - Dynamic Shortest Path](http://codeforces.com/problemset/problem/843/D)
* [UVA 11813 - Shopping](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2913)
* [UVA 11833 - Route Change](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=226&page=show_problem&problem=2933)
* [SPOJ - Easy Dijkstra Problem](http://www.spoj.com/problems/EZDIJKST/en/)
* [LA - 2819 - Cave Raider](https://vjudge.net/problem/UVALive-2819)
* [UVA 12144 - Almost Shortest Path](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3296)
* [UVA 12047 - Highest Paid Toll](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3198)
* [UVA 11514 - Batman](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2509)
* [Codeforces - Team Rocket Rises Again](http://codeforces.com/contest/757/problem/F)
* [UVA - 11338 - Minefield](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2313)
* [UVA 11374 - Airport Express](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2369)
* [UVA 11097 - Poor My Problem](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2038)
* [UVA 13172 - The music teacher](https://uva.onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=5083)
* [Codeforces - Dirty Arkady's Kitchen](http://codeforces.com/contest/827/problem/F)
* [SPOJ - Delivery Route](http://www.spoj.com/problems/DELIVER/)
* [SPOJ - Costly Chess](http://www.spoj.com/problems/CCHESS/)
* [CSES - Shortest Routes 1](https://cses.fi/problemset/task/1671)
* [CSES - Flight Discount](https://cses.fi/problemset/task/1195)
* [CSES - Flight Routes](https://cses.fi/problemset/task/1196)
