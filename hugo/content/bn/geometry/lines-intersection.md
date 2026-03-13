---
title: "সরলরেখার ছেদবিন্দু"
tags: 
weight: 30
---
# সরলরেখার ছেদবিন্দু

দুটো সরলরেখা দেওয়া আছে, $a_1 x + b_1 y + c_1 = 0$ এবং $a_2 x + b_2 y + c_2 = 0$ ইকুয়েশন দ্বারা দেখানো হয়েছে।
আমাদের সরলরেখাদ্বয়ের ছেদবিন্দু (intersection point) খুঁজতে হবে, অথবা বের করতে হবে যে সরলরেখা দুটো সমান্তরাল।

## সমাধান

দুটো সরলরেখা সমান্তরাল না হলে, তারা ছেদ করে।
তাদের ছেদবিন্দু খুঁজতে, আমাদের নিচের রৈখিক ইকুয়েশন ব্যবস্থা সমাধান করতে হবে:

$$\begin{cases} a_1 x + b_1 y + c_1 = 0 \\
a_2 x + b_2 y + c_2 = 0
\end{cases}$$

ক্র্যামারের নিয়ম (Cramer's rule) ব্যবহার করে, আমরা সরাসরি ব্যবস্থার সমাধান লিখতে পারি, যেটা আমাদের সরলরেখাদ্বয়ের প্রয়োজনীয় ছেদবিন্দু দেবে:

$$x = - \frac{\begin{vmatrix}c_1 & b_1 \cr c_2 & b_2\end{vmatrix}}{\begin{vmatrix}a_1 & b_1 \cr a_2 & b_2\end{vmatrix} } = - \frac{c_1 b_2 - c_2 b_1}{a_1 b_2 - a_2 b_1},$$

$$y = - \frac{\begin{vmatrix}a_1 & c_1 \cr a_2 & c_2\end{vmatrix}}{\begin{vmatrix}a_1 & b_1 \cr a_2 & b_2\end{vmatrix}} = - \frac{a_1 c_2 - a_2 c_1}{a_1 b_2 - a_2 b_1}.$$

যদি হর $0$ হয়, অর্থাৎ

$$\begin{vmatrix}a_1 & b_1 \cr a_2 & b_2\end{vmatrix} = a_1 b_2 - a_2 b_1 = 0 $$

তাহলে হয় ব্যবস্থার কোনো সমাধান নেই (সরলরেখাগুলো সমান্তরাল এবং ভিন্ন) অথবা অসীম সংখ্যক সমাধান আছে (সরলরেখাগুলো একই)।
যদি এই দুটো ক্ষেত্র আলাদা করতে হয়, তাহলে সহগ $c$ গুলো $a$ এবং $b$ সহগের সাথে একই অনুপাতে সমানুপাতিক কি না তা পরীক্ষা করতে হবে।
এটা করতে শুধু নিচের ডিটারমিন্যান্টগুলো (determinants) গণনা করতে হবে, এবং যদি দুটোই $0$ হয়, তাহলে সরলরেখাগুলো একই:

$$\begin{vmatrix}a_1 & c_1 \cr a_2 & c_2\end{vmatrix}, \begin{vmatrix}b_1 & c_1 \cr b_2 & c_2\end{vmatrix} $$

লক্ষ্য কর, ছেদবিন্দু গণনার একটা ভিন্ন পদ্ধতি [বেসিক জিওমেট্রি](basic-geometry.md) আর্টিকেলে ব্যাখ্যা করা আছে।

## ইমপ্লিমেন্টেশন

```cpp
struct pt {
    double x, y;
};

struct line {
    double a, b, c;
};

const double EPS = 1e-9;

double det(double a, double b, double c, double d) {
    return a*d - b*c;
}

bool intersect(line m, line n, pt & res) {
    double zn = det(m.a, m.b, n.a, n.b);
    if (abs(zn) < EPS)
        return false;
    res.x = -det(m.c, m.b, n.c, n.b) / zn;
    res.y = -det(m.a, m.c, n.a, n.c) / zn;
    return true;
}

bool parallel(line m, line n) {
    return abs(det(m.a, m.b, n.a, n.b)) < EPS;
}

bool equivalent(line m, line n) {
    return abs(det(m.a, m.b, n.a, n.b)) < EPS
        && abs(det(m.a, m.c, n.a, n.c)) < EPS
        && abs(det(m.b, m.c, n.b, n.c)) < EPS;
}
```
