---
tags:
  - Translated
e_maxx_link: segments_intersection_checking
---

# দুটি সেগমেন্ট ছেদ করে কিনা পরীক্ষা

আপনাকে দুটি সেগমেন্ট $(a, b)$ এবং $(c, d)$ দেওয়া আছে।
আপনাকে পরীক্ষা করতে হবে এরা ছেদ করে কিনা।
অবশ্যই, আপনি তাদের ছেদবিন্দু খুঁজে পরীক্ষা করতে পারেন এটি খালি কিনা, কিন্তু পূর্ণ সংখ্যা স্থানাঙ্কবিশিষ্ট সেগমেন্টের জন্য পূর্ণ সংখ্যায় এটি করা সম্ভব নয়।
এখানে বর্ণিত পদ্ধতিটি পূর্ণ সংখ্যায় কাজ করতে পারে।

## অ্যালগরিদম

প্রথমে, সেই ক্ষেত্রটি বিবেচনা করি যখন সেগমেন্টগুলো একই রেখার অংশ।
এই ক্ষেত্রে $Ox$ ও $Oy$-তে তাদের অভিক্ষেপ ছেদ করে কিনা পরীক্ষা করাই যথেষ্ট।
অন্য ক্ষেত্রে $a$ ও $b$ রেখা $(c, d)$-র একই পাশে থাকা উচিত নয়, এবং $c$ ও $d$ রেখা $(a, b)$-র একই পাশে থাকা উচিত নয়।
এটি কয়েকটি ক্রস প্রোডাক্ট দিয়ে পরীক্ষা করা যায়।

## ইমপ্লিমেন্টেশন

প্রদত্ত অ্যালগরিদমটি পূর্ণ সংখ্যা বিন্দুর জন্য ইমপ্লিমেন্ট করা হয়েছে। অবশ্যই, এটি সহজেই ডাবলের সাথে কাজ করতে পরিবর্তন করা যায়।

```{.cpp file=check-segments-inter}
struct pt {
    long long x, y;
    pt() {}
    pt(long long _x, long long _y) : x(_x), y(_y) {}
    pt operator-(const pt& p) const { return pt(x - p.x, y - p.y); }
    long long cross(const pt& p) const { return x * p.y - y * p.x; }
    long long cross(const pt& a, const pt& b) const { return (a - *this).cross(b - *this); }
};

int sgn(const long long& x) { return x >= 0 ? x ? 1 : 0 : -1; }

bool inter1(long long a, long long b, long long c, long long d) {
    if (a > b)
        swap(a, b);
    if (c > d)
        swap(c, d);
    return max(a, c) <= min(b, d);
}

bool check_inter(const pt& a, const pt& b, const pt& c, const pt& d) {
    if (c.cross(a, d) == 0 && c.cross(b, d) == 0)
        return inter1(a.x, b.x, c.x, d.x) && inter1(a.y, b.y, c.y, d.y);
    return sgn(a.cross(b, c)) != sgn(a.cross(b, d)) &&
           sgn(c.cross(d, a)) != sgn(c.cross(d, b));
}
```
