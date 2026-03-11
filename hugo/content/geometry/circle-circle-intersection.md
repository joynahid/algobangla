---
title: "বৃত্ত-বৃত্ত ছেদবিন্দু"
tags: 
weight: 70
---
# বৃত্ত-বৃত্ত ছেদবিন্দু

আপনাকে ২D সমতলে দুটি বৃত্ত দেওয়া আছে, প্রতিটি তার কেন্দ্রের স্থানাঙ্ক ও ব্যাসার্ধ দ্বারা বর্ণিত। তাদের ছেদবিন্দু খুঁজুন (সম্ভাব্য ক্ষেত্র: এক বা দুটি বিন্দু, কোনো ছেদ নেই বা বৃত্তগুলো অভিন্ন)।

## সমাধান

আসুন এই সমস্যাটিকে [বৃত্ত-রেখা ছেদবিন্দু সমস্যায়](circle-line-intersection.md) সরলীকৃত করি।

সাধারণতা না হারিয়ে ধরে নিই প্রথম বৃত্তের কেন্দ্র মূলবিন্দুতে (যদি না হয়, আমরা মূলবিন্দু প্রথম বৃত্তের কেন্দ্রে সরাতে পারি এবং আউটপুটের সময় ছেদবিন্দুর স্থানাঙ্ক সেই অনুযায়ী সমন্বয় করতে পারি)। আমাদের দুটি সমীকরণের ব্যবস্থা আছে:

$$x^2+y^2=r_1^2$$

$$(x - x_2)^2 + (y - y_2)^2 = r_2^2$$

চলকের দ্বিঘাত পদ থেকে মুক্তি পেতে দ্বিতীয় সমীকরণ থেকে প্রথমটি বিয়োগ করি:

$$x^2+y^2=r_1^2$$

$$x \cdot (-2x_2) + y \cdot (-2y_2) + (x_2^2+y_2^2+r_1^2-r_2^2) = 0$$

সুতরাং, আমরা মূল সমস্যাটিকে প্রথম বৃত্ত ও একটি রেখার ছেদবিন্দু খোঁজার সমস্যায় সরলীকৃত করেছি:

$$Ax + By + C = 0$$

$$\begin{align}
A &= -2x_2 \\
B &= -2y_2 \\
C &= x_2^2+y_2^2+r_1^2-r_2^2
\end{align}$$

এবং এই সমস্যাটি [সংশ্লিষ্ট আর্টিকেলে](circle-line-intersection.md) বর্ণিত পদ্ধতিতে সমাধান করা যায়।

একমাত্র অবক্ষয়িত ক্ষেত্র যা আমাদের আলাদাভাবে বিবেচনা করতে হবে তা হলো যখন বৃত্তগুলোর কেন্দ্র মিলে যায়। এই ক্ষেত্রে $x_2=y_2=0$, এবং রেখার সমীকরণ হবে $C = r_1^2-r_2^2 = 0$। যদি বৃত্তগুলোর ব্যাসার্ধ একই হয়, অসীম সংখ্যক ছেদবিন্দু আছে, যদি ভিন্ন হয়, কোনো ছেদ নেই।

## অনুশীলন সমস্যা

- [RadarFinder](https://community.topcoder.com/stat?c=problem_statement&pm=7766)
- [Runaway to a shadow - Codeforces Round #357](http://codeforces.com/problemset/problem/681/E)
- [ASC 1 Problem F "Get out!"](http://codeforces.com/gym/100199/problem/F)
- [SPOJ: CIRCINT](http://www.spoj.com/problems/CIRCINT/)
- [UVA - 10301 - Rings and Glue](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1242)
- [Codeforces 933C A Colorful Prospect](https://codeforces.com/problemset/problem/933/C)
- [TIMUS 1429 Biscuits](https://acm.timus.ru/problem.aspx?space=1&num=1429)
