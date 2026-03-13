---
title: "Depth First Search (DFS)"
tags: 
weight: 20
---
# Depth First Search (DFS)

DFS হলো প্রধান গ্রাফ অ্যালগরিদমগুলোর মধ্যে একটি।

DFS একটি সোর্স ভার্টেক্স $u$ থেকে প্রতিটি ভার্টেক্সে যাওয়ার লেক্সিকোগ্রাফিক্যালি প্রথম পাথ খুঁজে বের করে।
DFS একটি ট্রিতে শর্টেস্ট পাথও খুঁজে বের করবে (কারণ সেখানে কেবল একটি সিম্পল পাথ থাকে), কিন্তু সাধারণ গ্রাফের ক্ষেত্রে এটা প্রযোজ্য নয়।

অ্যালগরিদমটি $O(m + n)$ সময়ে কাজ করে, যেখানে $n$ হলো ভার্টেক্সের সংখ্যা এবং $m$ হলো এজের সংখ্যা।

## অ্যালগরিদমের বর্ণনা

ডিএফএস-এর মূল ধারণা হলো গ্রাফে যতটা সম্ভব গভীরে যাওয়া, এবং যখন এমন একটি ভার্টেক্সে পৌঁছানো যায় যার কোনো অভিজিটেড অ্যাডজেসেন্ট ভার্টেক্স নেই, তখন ব্যাকট্র্যাক করা।

অ্যালগরিদমটি রিকার্সিভভাবে বর্ণনা/ইমপ্লিমেন্ট করা খুবই সহজ:
আমরা একটি ভার্টেক্স থেকে সার্চ শুরু করি।
একটি ভার্টেক্স ভিজিট করার পর, আমরা প্রতিটি অ্যাডজেসেন্ট ভার্টেক্সের জন্য ডিএফএস চালাই যেটা আমরা আগে ভিজিট করিনি।
এভাবে আমরা স্টার্টিং ভার্টেক্স থেকে রিচেবল সব ভার্টেক্স ভিজিট করি।

আরও বিস্তারিত জানতে ইমপ্লিমেন্টেশন দেখো।

## Applications of DFS

  * সোর্স ভার্টেক্স $u$ থেকে সব ভার্টেক্সে গ্রাফে যেকোনো পাথ খুঁজে বের করা।

  * সোর্স $u$ থেকে সব ভার্টেক্সে গ্রাফে লেক্সিকোগ্রাফিক্যালি প্রথম পাথ খুঁজে বের করা।

  * একটি ট্রিতে কোনো ভার্টেক্স অন্য কোনো ভার্টেক্সের অ্যানসেস্টর কিনা পরীক্ষা করা:

    প্রতিটি সার্চ কলের শুরুতে ও শেষে আমরা প্রতিটি ভার্টেক্সের এন্ট্রি ও এক্সিট "টাইম" মনে রাখি।
    এখন যেকোনো ভার্টেক্স জোড়া $(i, j)$-এর জন্য $O(1)$-এ উত্তর বের করা যায়:
    ভার্টেক্স $i$, ভার্টেক্স $j$-এর অ্যানসেস্টর হবে যদি এবং কেবল যদি $\text{entry}[i] < \text{entry}[j]$ এবং $\text{exit}[i] > \text{exit}[j]$ হয়।

  * দুটি ভার্টেক্সের LCA খুঁজে বের করা।

  * টপোলজিক্যাল সর্টিং:

    একাধিক DFS চালিয়ে প্রতিটি ভার্টেক্স ঠিক একবার ভিজিট করা হয় $O(n + m)$ সময়ে।
    এক্সিট টাইমের উতরতি ক্রমে ভার্টেক্সগুলো সাজালেই প্রয়োজনীয় টপোলজিক্যাল অর্ডারিং পাওয়া যায়।


  * দেওয়া গ্রাফটি অ্যাসাইক্লিক কিনা পরীক্ষা করা এবং গ্রাফে সাইকেল খুঁজে বের করা। (নিচে উল্লেখ করা হয়েছে, প্রতিটি কানেক্টেড কম্পোনেন্টে ব্যাক এজ গণনা করে)।

  * একটি ডিরেক্টেড গ্রাফে স্ট্রংলি কানেক্টেড কম্পোনেন্ট খুঁজে বের করা:

    প্রথমে গ্রাফের টপোলজিক্যাল সর্টিং করতে হবে।
    তারপর গ্রাফটি ট্রান্সপোজ করে টপোলজিক্যাল সর্ট দ্বারা নির্ধারিত ক্রমে আরেকটি DFS সিরিজ চালাতে হবে। প্রতিটি ডিএফএস কলে তৈরি কম্পোনেন্টটি একটি স্ট্রংলি কানেক্টেড কম্পোনেন্ট।

  * একটি আনডিরেক্টেড গ্রাফে ব্রিজ খুঁজে বের করা:

    প্রথমে একাধিক DFS চালিয়ে দেওয়া গ্রাফটিকে একটি ডিরেক্টেড গ্রাফে রূপান্তর করতে হবে, প্রতিটি এজকে আমরা যে দিকে ট্রাভার্স করি সেই দিকে ডিরেক্ট করে। দ্বিতীয়ত, এই ডিরেক্টেড গ্রাফে স্ট্রংলি কানেক্টেড কম্পোনেন্ট খুঁজতে হবে। ব্রিজ হলো সেই এজগুলো যাদের দুই প্রান্ত ভিন্ন স্ট্রংলি কানেক্টেড কম্পোনেন্টে অবস্থিত।

## গ্রাফের এজের শ্রেণিবিভাগ

আমরা একটি গ্রাফ $G$-এর এজগুলোকে শ্রেণিবিভাগ করতে পারি, এজ $(u,v)$-এর প্রান্তবিন্দু $u$ ও $v$-এর এন্ট্রি ও এক্সিট টাইম ব্যবহার করে।
এই শ্রেণিবিভাগগুলো প্রায়ই [ব্রিজ খোঁজা](bridge-searching.md) এবং [আর্টিকুলেশন পয়েন্ট খোঁজা](cutpoints.md)-র মতো সমস্যায় ব্যবহৃত হয়।

আমরা একটি ডিএফএস চালাই এবং নিচের নিয়ম ব্যবহার করে প্রাপ্ত এজগুলোকে শ্রেণিবিভাগ করি:

যদি $v$ ভিজিটেড না হয়:

* ট্রি এজ - যদি $u$-এর পরে $v$ ভিজিট হয়, তাহলে এজ $(u,v)$-কে ট্রি এজ বলা হয়। অন্যভাবে বলতে গেলে, যদি $v$ প্রথমবার ভিজিট হচ্ছে এবং $u$ বর্তমানে ভিজিট হচ্ছে, তাহলে $(u,v)$-কে ট্রি এজ বলা হয়।
এই এজগুলো একটি ডিএফএস ট্রি গঠন করে, তাই এদের নাম ট্রি এজ।

যদি $v$, $u$-এর আগে ভিজিটেড হয়:

* ব্যাক এজ - যদি $v$, $u$-এর একটি অ্যানসেস্টর হয়, তাহলে এজ $(u,v)$ একটি ব্যাক এজ। $v$ তখনই অ্যানসেস্টর যখন আমরা ইতিমধ্যে $v$-এ এন্টার করেছি, কিন্তু এখনও এক্সিট করিনি। ব্যাক এজ একটি সাইকেল সম্পূর্ণ করে কারণ অ্যানসেস্টর $v$ থেকে ডিসেন্ড্যান্ট $u$ পর্যন্ত একটি পাথ আছে (ডিএফএস-এর রিকার্সনে) এবং ডিসেন্ড্যান্ট $u$ থেকে অ্যানসেস্টর $v$-তে একটি এজ আছে (ব্যাক এজ), ফলে একটি সাইকেল তৈরি হয়। ব্যাক এজ ব্যবহার করে সাইকেল ডিটেক্ট করা যায়।

* ফরওয়ার্ড এজ - যদি $v$, $u$-এর একটি ডিসেন্ড্যান্ট হয়, তাহলে এজ $(u, v)$ একটি ফরওয়ার্ড এজ। অন্যভাবে বলতে গেলে, যদি আমরা ইতিমধ্যে $v$ ভিজিট করে এক্সিট করেছি এবং $\text{entry}[u] < \text{entry}[v]$ হয়, তাহলে এজ $(u,v)$ একটি ফরওয়ার্ড এজ।
* ক্রস এজ: যদি $v$, $u$-এর অ্যানসেস্টর বা ডিসেন্ড্যান্ট কোনোটিই না হয়, তাহলে এজ $(u, v)$ একটি ক্রস এজ। অন্যভাবে বলতে গেলে, যদি আমরা ইতিমধ্যে $v$ ভিজিট করে এক্সিট করেছি এবং $\text{entry}[u] > \text{entry}[v]$ হয়, তাহলে $(u,v)$ একটি ক্রস এজ।

**থিওরেম।** ধরি $G$ একটি আনডিরেক্টেড গ্রাফ। তাহলে, $G$-এর উপর ডিএফএস চালালে প্রতিটি প্রাপ্ত এজকে ট্রি এজ বা ব্যাক এজ হিসেবে শ্রেণিবিভাগ করা হবে, অর্থাৎ ফরওয়ার্ড এজ ও ক্রস এজ শুধুমাত্র ডিরেক্টেড গ্রাফে বিদ্যমান।

ধরি $(u,v)$ হলো $G$-এর একটি যেকোনো এজ এবং সাধারণতা না হারিয়ে, $u$, $v$-এর আগে ভিজিটেড, অর্থাৎ $\text{entry}[u] < \text{entry}[v]$। যেহেতু ডিএফএস প্রতিটি এজ কেবল একবার প্রসেস করে, এজ $(u,v)$ প্রসেস ও শ্রেণিবিভাগ করার মাত্র দুটি উপায় আছে:

* প্রথমবার আমরা এজ $(u,v)$ এক্সপ্লোর করি $u$ থেকে $v$ দিকে। যেহেতু $\text{entry}[u] < \text{entry}[v]$, ডিএফএস-এর রিকার্সিভ প্রকৃতির কারণে নোড $v$ সম্পূর্ণ এক্সপ্লোর হয়ে এক্সিট হবে আমরা "কল স্ট্যাকে ওপরে উঠে" নোড $u$ এক্সিট করার আগে। সুতরাং, ডিএফএস যখন প্রথমবার $u$ থেকে $v$ দিকে এজ $(u,v)$ এক্সপ্লোর করে তখন নোড $v$ অবশ্যই অভিজিটেড থাকবে, কারণ অন্যথায় সার্চটি নোড $v$ এক্সিট করার আগে $v$ থেকে $u$ দিকে $(u,v)$ এক্সপ্লোর করত, যেহেতু নোড $u$ ও $v$ নেইবার। অতএব, এজ $(u,v)$ একটি ট্রি এজ।

* প্রথমবার আমরা এজ $(u,v)$ এক্সপ্লোর করি $v$ থেকে $u$ দিকে। যেহেতু আমরা নোড $v$-এর আগে নোড $u$ আবিষ্কার করেছি, এবং আমরা প্রতিটি এজ কেবল একবার প্রসেস করি, $v$ থেকে $u$ দিকে এজ $(u,v)$ এক্সপ্লোর করার একমাত্র উপায় হলো $u$ থেকে $v$-তে অন্য একটি পাথ থাকা যেটা এজ $(u,v)$ অন্তর্ভুক্ত করে না, ফলে $u$ হয় $v$-এর অ্যানসেস্টর। এজ $(u,v)$ তাই একটি সাইকেল সম্পূর্ণ করে কারণ এটা ডিসেন্ড্যান্ট $v$ থেকে অ্যানসেস্টর $u$-তে যাচ্ছে, যেটা আমরা এখনও এক্সিট করিনি। অতএব, এজ $(u,v)$ একটি ব্যাক এজ।

যেহেতু এজ $(u,v)$ প্রসেস করার মাত্র দুটি উপায় আছে, উপরে বর্ণিত দুটি ক্ষেত্র ও তাদের শ্রেণিবিভাগ অনুসারে, $G$-এর উপর ডিএফএস চালালে প্রতিটি প্রাপ্ত এজকে ট্রি এজ বা ব্যাক এজ হিসেবে শ্রেণিবিভাগ করা হবে, অর্থাৎ ফরওয়ার্ড এজ ও ক্রস এজ শুধুমাত্র ডিরেক্টেড গ্রাফে বিদ্যমান। এতে প্রুফ সম্পূর্ণ হলো।

## ইমপ্লিমেন্টেশন

```cpp
vector<vector<int>> adj; // graph represented as an adjacency list
int n; // number of vertices

vector<bool> visited;

void dfs(int v) {
	visited[v] = true;
	for (int u : adj[v]) {
		if (!visited[u])
			dfs(u);
    }
}
```
এটা DFS-এর সবচেয়ে সরল ইমপ্লিমেন্টেশন।
অ্যাপ্লিকেশন অংশে বর্ণিত হিসাবে, এন্ট্রি ও এক্সিট টাইম এবং ভার্টেক্স কালার কম্পিউট করাও কাজে আসতে পারে।
আমরা সব ভার্টেক্সকে কালার ০ দিয়ে চিহ্নিত করব যদি আমরা সেগুলো ভিজিট না করে থাকি, কালার ১ দিয়ে যদি আমরা সেগুলো ভিজিট করে থাকি, এবং কালার ২ দিয়ে যদি আমরা ইতিমধ্যে ভার্টেক্সটি থেকে এক্সিট করে থাকি।

এখানে একটি জেনেরিক ইমপ্লিমেন্টেশন দেওয়া হলো যা অতিরিক্তভাবে এগুলো কম্পিউট করে:

```cpp
vector<vector<int>> adj; // graph represented as an adjacency list
int n; // number of vertices

vector<int> color;

vector<int> time_in, time_out;
int dfs_timer = 0;

void dfs(int v) {
	time_in[v] = dfs_timer++;
	color[v] = 1;
	for (int u : adj[v])
		if (color[u] == 0)
			dfs(u);
	color[v] = 2;
	time_out[v] = dfs_timer++;
}
```

## অনুশীলন সমস্যা

* [SPOJ: ABCPATH](http://www.spoj.com/problems/ABCPATH/)
* [SPOJ: EAGLE1](http://www.spoj.com/problems/EAGLE1/)
* [Codeforces: Kefa and Park](http://codeforces.com/problemset/problem/580/C)
* [Timus:Werewolf](http://acm.timus.ru/problem.aspx?space=1&num=1242)
* [Timus:Penguin Avia](http://acm.timus.ru/problem.aspx?space=1&num=1709)
* [Timus:Two Teams](http://acm.timus.ru/problem.aspx?space=1&num=1106)
* [SPOJ - Ada and Island](http://www.spoj.com/problems/ADASEA/)
* [UVA 657 - The die is cast](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=598)
* [SPOJ - Sheep](http://www.spoj.com/problems/KOZE/)
* [SPOJ - Path of the Rightenous Man](http://www.spoj.com/problems/RIOI_2_3/)
* [SPOJ - Validate the Maze](http://www.spoj.com/problems/MAKEMAZE/)
* [SPOJ - Ghosts having Fun](http://www.spoj.com/problems/GHOSTS/)
* [Codeforces - Underground Lab](http://codeforces.com/contest/781/problem/C)
* [DevSkill - Maze Tester (archived)](http://web.archive.org/web/20200319103915/https://www.devskill.com/CodingProblems/ViewProblem/3)
* [DevSkill - Tourist (archived)](http://web.archive.org/web/20190426175135/https://devskill.com/CodingProblems/ViewProblem/17)
* [Codeforces - Anton and Tree](http://codeforces.com/contest/734/problem/E)
* [Codeforces - Transformation: From A to B](http://codeforces.com/contest/727/problem/A)
* [Codeforces - One Way Reform](http://codeforces.com/contest/723/problem/E)
* [Codeforces - Centroids](http://codeforces.com/contest/709/problem/E)
* [Codeforces - Generate a String](http://codeforces.com/contest/710/problem/E)
* [Codeforces - Broken Tree](http://codeforces.com/contest/758/problem/E)
* [Codeforces - Dasha and Puzzle](http://codeforces.com/contest/761/problem/E)
* [Codeforces - Making genome In Berland](http://codeforces.com/contest/638/problem/B)
* [Codeforces - Road Improvement](http://codeforces.com/contest/638/problem/C)
* [Codeforces - Garland](http://codeforces.com/contest/767/problem/C)
* [Codeforces - Labeling Cities](http://codeforces.com/contest/794/problem/D)
* [Codeforces - Send the Fool Futher!](http://codeforces.com/contest/802/problem/K)
* [Codeforces - The tag Game](http://codeforces.com/contest/813/problem/C)
* [Codeforces - Leha and Another game about graphs](http://codeforces.com/contest/841/problem/D)
* [Codeforces - Shortest path problem](http://codeforces.com/contest/845/problem/G)
* [Codeforces - Upgrading Tree](http://codeforces.com/contest/844/problem/E)
* [Codeforces - From Y to Y](http://codeforces.com/contest/849/problem/C)
* [Codeforces - Chemistry in Berland](http://codeforces.com/contest/846/problem/E)
* [Codeforces - Wizards Tour](http://codeforces.com/contest/861/problem/F)
* [Codeforces - Ring Road](http://codeforces.com/contest/24/problem/A)
* [Codeforces - Mail Stamps](http://codeforces.com/contest/29/problem/C)
* [Codeforces - Ant on the Tree](http://codeforces.com/contest/29/problem/D)
* [SPOJ - Cactus](http://www.spoj.com/problems/CAC/)
* [SPOJ - Mixing Chemicals](http://www.spoj.com/problems/AMR10J/)
