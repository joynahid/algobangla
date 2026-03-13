---
title: "বৃত্ত-বৃত্ত ছেদবিন্দু"
tags: 
weight: 70
---
# বৃত্ত-বৃত্ত ছেদবিন্দু

তোমাকে 2D সমতলে দুটি বৃত্ত দেওয়া আছে, প্রতিটা তার কেন্দ্রের স্থানাঙ্ক আর ব্যাসার্ধ দিয়ে বর্ণনা করা। তাদের ছেদবিন্দু বের করো (সম্ভাব্য কেস: এক বা দুটো বিন্দু, কোনো ছেদ নেই, অথবা বৃত্তগুলো অভিন্ন)।

## সমাধান

চলো এই সমস্যাটাকে [বৃত্ত-রেখা ছেদবিন্দু সমস্যায়](circle-line-intersection.md) সরলীকৃত করি।

সাধারণতা না হারিয়ে ধরে নিই প্রথম বৃত্তের কেন্দ্র মূলবিন্দুতে (যদি না হয়, আমরা মূলবিন্দু প্রথম বৃত্তের কেন্দ্রে সরাতে পারি আর আউটপুটের সময় ছেদবিন্দুর স্থানাঙ্ক সেই অনুযায়ী অ্যাডজাস্ট করে নিতে পারি)। আমাদের দুটো ইকুয়েশনের সিস্টেম আছে:

$$x^2+y^2=r_1^2$$

$$(x - x_2)^2 + (y - y_2)^2 = r_2^2$$

চলকের দ্বিঘাত পদ থেকে মুক্তি পেতে দ্বিতীয় ইকুয়েশন থেকে প্রথমটি বিয়োগ করি:

$$x^2+y^2=r_1^2$$

$$x \cdot (-2x_2) + y \cdot (-2y_2) + (x_2^2+y_2^2+r_1^2-r_2^2) = 0$$

তারমানে, আমরা মূল সমস্যাটাকে প্রথম বৃত্ত আর একটা রেখার ছেদবিন্দু খোঁজার সমস্যায় নামিয়ে এনেছি:

$$Ax + By + C = 0$$

$$\begin{align}
A &= -2x_2 \\
B &= -2y_2 \\
C &= x_2^2+y_2^2+r_1^2-r_2^2
\end{align}$$

আর এই সমস্যাটা [সংশ্লিষ্ট আর্টিকেলে](circle-line-intersection.md) দেখানো পদ্ধতিতে সমাধান করা যায়।

একটাই ডিজেনারেট কেস আলাদা করে দেখতে হবে — যখন বৃত্তগুলোর কেন্দ্র একই জায়গায়। এই কেসে $x_2=y_2=0$, আর রেখার ইকুয়েশন হবে $C = r_1^2-r_2^2 = 0$। যদি বৃত্তগুলোর ব্যাসার্ধ একই হয়, তাহলে অসীম সংখ্যক ছেদবিন্দু আছে। আর ভিন্ন হলে কোনো ছেদ নেই।

## অনুশীলন সমস্যা

- [RadarFinder](https://community.topcoder.com/stat?c=problem_statement&pm=7766)
- [Runaway to a shadow - Codeforces Round #357](http://codeforces.com/problemset/problem/681/E)
- [ASC 1 Problem F "Get out!"](http://codeforces.com/gym/100199/problem/F)
- [SPOJ: CIRCINT](http://www.spoj.com/problems/CIRCINT/)
- [UVA - 10301 - Rings and Glue](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1242)
- [Codeforces 933C A Colorful Prospect](https://codeforces.com/problemset/problem/933/C)
- [TIMUS 1429 Biscuits](https://acm.timus.ru/problem.aspx?space=1&num=1429)
