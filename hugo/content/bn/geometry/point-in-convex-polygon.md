---
title: $O(\log N)$-এ একটি বিন্দু উত্তল পলিগনের অন্তর্গত কি না পরীক্ষা করা
tags: 
weight: 30
---
# $O(\log N)$-এ একটি বিন্দু উত্তল পলিগনের অন্তর্গত কি না পরীক্ষা করা

নিচের সমস্যাটা ধরো: তোমাকে পূর্ণসংখ্যা ভার্টেক্স (vertex) বিশিষ্ট একটা উত্তল পলিগন (convex polygon) ও অনেকগুলো কুয়েরি দেওয়া আছে।
প্রতিটি কুয়েরি একটি বিন্দু, যার জন্য আমাদের নির্ণয় করতে হবে এটা পলিগনের ভেতরে বা সীমানায় অবস্থিত কি না।
ধরো পলিগনটা ঘড়ির কাঁটার বিপরীত দিকে সাজানো। আমরা প্রতিটা কুয়েরি $O(\log n)$-এ অনলাইনে উত্তর দেব।

## অ্যালগরিদম
সবচেয়ে ছোট x-স্থানাঙ্ক বিশিষ্ট বিন্দুটি বেছে নিই। একাধিক থাকলে, সবচেয়ে ছোট y-স্থানাঙ্ক বিশিষ্টটি নিই। একে $p_0$ বলি।
এখন পলিগনের অন্য সব বিন্দু $p_1,\dots,p_n$ সিলেক্টেড বিন্দু থেকে তাদের পোলার কোণ অনুযায়ী সাজানো (কারণ পলিগন ঘড়ির কাঁটার বিপরীত দিকে সাজানো)।

বিন্দুটি পলিগনের অন্তর্গত হলে, এটা কোনো ত্রিভুজ $p_0, p_i, p_{i + 1}$-র অন্তর্গত (সীমানায় থাকলে একাধিক ত্রিভুজেও হতে পারে)।
ত্রিভুজ $p_0, p_i, p_{i + 1}$ ধরো যেখানে $p$ এই ত্রিভুজের অন্তর্গত এবং এমন সব ত্রিভুজের মধ্যে $i$ সর্বাধিক।

একটা বিশেষ ক্ষেত্র আছে। $p$ রেখাখণ্ড $(p_0, p_n)$-এর উপর অবস্থিত। এই ক্ষেত্রটা আমরা আলাদাভাবে পরীক্ষা করব।
অন্যথায় $j \le i$ সকল $p_j$ বিন্দু $p_0$-এর সাপেক্ষে $p$-থেকে ঘড়ির কাঁটার বিপরীত দিকে, এবং বাকি সব বিন্দু ঘড়ির কাঁটার বিপরীত দিকে নয়।
এর মানে হলো আমরা $p_i$ বিন্দুর জন্য বাইনারি সার্চ প্রয়োগ করতে পারি, যেখানে $p_i$ $p_0$-এর সাপেক্ষে $p$-থেকে ঘড়ির কাঁটার বিপরীত দিকে নয়, এবং এমন সব বিন্দুর মধ্যে $i$ সর্বাধিক।
এরপর আমরা পরীক্ষা করি বিন্দুটি আসলেই নির্ণীত ত্রিভুজে আছে কি না।

$(a - c) \times (b - c)$-এর চিহ্ন আমাদের বলবে, $c$ বিন্দুর সাপেক্ষে $a$ বিন্দু $b$ থেকে ঘড়ির কাঁটার দিকে নাকি বিপরীত দিকে।
যদি $(a - c) \times (b - c) > 0$ হয়, তাহলে $a$ বিন্দু $c$ থেকে $b$-তে যাওয়া ভেক্টরের ডানদিকে, অর্থাৎ $c$-এর সাপেক্ষে $b$ থেকে ঘড়ির কাঁটার দিকে।
এবং যদি $(a - c) \times (b - c) < 0$ হয়, তাহলে বিন্দুটি বামদিকে, বা ঘড়ির কাঁটার বিপরীত দিকে।
এবং এটা ঠিক $b$ ও $c$ বিন্দুর মধ্যবর্তী রেখার উপর।

অ্যালগরিদমে ফিরে যাই:
একটি কুয়েরি বিন্দু $p$ ধরো।
প্রথমে, আমাদের পরীক্ষা করতে হবে বিন্দুটি $p_1$ ও $p_n$-এর মধ্যে অবস্থিত কি না।
অন্যথায় আমরা ইতিমধ্যেই জানি এটা পলিগনের অংশ হতে পারে না।
এটা পরীক্ষা করা যায় $(p_1 - p_0)\times(p - p_0)$ শূন্য কি না বা $(p_1 - p_0)\times(p_n - p_0)$-এর সাথে একই চিহ্ন আছে কি না, এবং $(p_n - p_0)\times(p - p_0)$ শূন্য কি না বা $(p_n - p_0)\times(p_1 - p_0)$-এর সাথে একই চিহ্ন আছে কি না দেখে।
তারপর আমরা বিশেষ ক্ষেত্রটি সামলাই যেখানে $p$ রেখা $(p_0, p_1)$-এর অংশ।
এরপর আমরা $p_1,\dots p_n$ থেকে শেষ বিন্দু বাইনারি সার্চ করতে পারি যেটা $p_0$-এর সাপেক্ষে $p$-থেকে ঘড়ির কাঁটার বিপরীত দিকে নয়।
একটি নির্দিষ্ট বিন্দু $p_i$-র জন্য এই শর্ত পরীক্ষা করা যায় $(p_i - p_0)\times(p - p_0) \le 0$ কি না দেখে। এমন বিন্দু $p_i$ পাওয়ার পর, আমাদের পরীক্ষা করতে হবে $p$ ত্রিভুজ $p_0, p_i, p_{i + 1}$-এর ভেতরে আছে কি না।
ত্রিভুজের অন্তর্গত কি না পরীক্ষা করতে, আমরা সহজেই যাচাই করতে পারি $|(p_i - p_0)\times(p_{i + 1} - p_0)| = |(p_0 - p)\times(p_i - p)| + |(p_i - p)\times(p_{i + 1} - p)| + |(p_{i + 1} - p)\times(p_0 - p)|$।
এটা পরীক্ষা করে যে ত্রিভুজ $p_0, p_i, p_{i+1}$-এর ক্ষেত্রফল ত্রিভুজ $p_0, p_i, p$, ত্রিভুজ $p_0, p, p_{i+1}$ ও ত্রিভুজ $p_i, p_{i+1}, p$-এর ক্ষেত্রফলের যোগফলের সমান কি না।
$p$ বাইরে থাকলে, এই তিনটি ত্রিভুজের যোগফল মূল ত্রিভুজের ক্ষেত্রফলের চেয়ে বেশি হবে।
ভেতরে থাকলে, সমান হবে।

## ইমপ্লিমেন্টেশন

`prepare` ফাংশনটি নিশ্চিত করবে যে লেক্সিকোগ্রাফিক্যালি ক্ষুদ্রতম বিন্দু (সর্বনিম্ন x মান, টাইয়ের ক্ষেত্রে সর্বনিম্ন y মান) $p_0$ হবে, এবং $p_i - p_0$ ভেক্টরগুলো গণনা করবে।
এরপর `pointInConvexPolygon` ফাংশনটি একটি কুয়েরির ফলাফল গণনা করবে।
আমরা অতিরিক্তভাবে $p_0$ বিন্দু মনে রাখি এবং সব কুয়েরি বিন্দু এটা দিয়ে সরিয়ে নিই যাতে সঠিক দূরত্ব গণনা করা যায়, কারণ ভেক্টরের কোনো আদি বিন্দু নেই।
কুয়েরি বিন্দু সরানোর মাধ্যমে আমরা ধরে নিতে পারি সব ভেক্টর মূলবিন্দু $(0, 0)$ থেকে শুরু হয়, এবং দূরত্ব ও দৈর্ঘ্যের গণনা সরল হয়।

```cpp
struct pt {
    long long x, y;
    pt() {}
    pt(long long _x, long long _y) : x(_x), y(_y) {}
    pt operator+(const pt &p) const { return pt(x + p.x, y + p.y); }
    pt operator-(const pt &p) const { return pt(x - p.x, y - p.y); }
    long long cross(const pt &p) const { return x * p.y - y * p.x; }
    long long dot(const pt &p) const { return x * p.x + y * p.y; }
    long long cross(const pt &a, const pt &b) const { return (a - *this).cross(b - *this); }
    long long dot(const pt &a, const pt &b) const { return (a - *this).dot(b - *this); }
    long long sqrLen() const { return this->dot(*this); }
};

bool lexComp(const pt &l, const pt &r) {
    return l.x < r.x || (l.x == r.x && l.y < r.y);
}

int sgn(long long val) { return val > 0 ? 1 : (val == 0 ? 0 : -1); }

vector<pt> seq;
pt translation;
int n;

bool pointInTriangle(pt a, pt b, pt c, pt point) {
    long long s1 = abs(a.cross(b, c));
    long long s2 = abs(point.cross(a, b)) + abs(point.cross(b, c)) + abs(point.cross(c, a));
    return s1 == s2;
}

void prepare(vector<pt> &points) {
    n = points.size();
    int pos = 0;
    for (int i = 1; i < n; i++) {
        if (lexComp(points[i], points[pos]))
            pos = i;
    }
    rotate(points.begin(), points.begin() + pos, points.end());

    n--;
    seq.resize(n);
    for (int i = 0; i < n; i++)
        seq[i] = points[i + 1] - points[0];
    translation = points[0];
}

bool pointInConvexPolygon(pt point) {
    point = point - translation;
    if (seq[0].cross(point) != 0 &&
            sgn(seq[0].cross(point)) != sgn(seq[0].cross(seq[n - 1])))
        return false;
    if (seq[n - 1].cross(point) != 0 &&
            sgn(seq[n - 1].cross(point)) != sgn(seq[n - 1].cross(seq[0])))
        return false;

    if (seq[0].cross(point) == 0)
        return seq[0].sqrLen() >= point.sqrLen();

    int l = 0, r = n - 1;
    while (r - l > 1) {
        int mid = (l + r) / 2;
        int pos = mid;
        if (seq[pos].cross(point) >= 0)
            l = mid;
        else
            r = mid;
    }
    int pos = l;
    return pointInTriangle(seq[pos], seq[pos + 1], pt(0, 0), point);
}
```

## অনুশীলন সমস্যা
* [SGU253 Theodore Roosevelt](https://codeforces.com/problemsets/acmsguru/problem/99999/253)
* [Codeforces 55E Very simple problem](https://codeforces.com/contest/55/problem/E)
* [Codeforces 166B Polygons](https://codeforces.com/problemset/problem/166/B)
