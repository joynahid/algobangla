---
tags:
  - Translated
e_maxx_link: kirchhoff_theorem
---

# কির্শহফের উপপাদ্য। স্প্যানিং ট্রির সংখ্যা খুঁজে পাওয়া

সমস্যা: আপনাকে একটি সংযুক্ত অনিয়ন্ত্রিত গ্রাফ (সম্ভাব্য একাধিক এজ সহ) দেওয়া হয় যা একটি সংলগ্নতা ম্যাট্রিক্স ব্যবহার করে প্রতিনিধিত্ব করা হয়। এই গ্রাফের বিভিন্ন স্প্যানিং ট্রির সংখ্যা খুঁজে বের করুন।

১৮৪৭ সালে কির্শহফ দ্বারা নিম্নলিখিত সূত্রটি প্রমাণ করা হয়েছিল।

## কির্শহফের ম্যাট্রিক্স ট্রি উপপাদ্য

$A$ গ্রাফের সংলগ্নতা ম্যাট্রিক্স হতে দিন: $A_{u,v}$ হল $u$ এবং $v$ এর মধ্যে এজের সংখ্যা।
$D$ গ্রাফের ডিগ্রি ম্যাট্রিক্স হতে দিন: একটি কর্ণ ম্যাট্রিক্স যেখানে $D_{u,u}$ হল ভার্টেক্স $u$ এর ডিগ্রি (একাধিক এজ এবং লুপ সহ - এজ যা ভার্টেক্স $u$ কে নিজের সাথে সংযুক্ত করে)।

The Laplacian matrix of the graph is defined as $L = D - A$.
According to Kirchhoff's theorem, all cofactors of this matrix are equal to each other, and they are equal to the number of spanning trees of the graph.
The $(i,j)$ cofactor of a matrix is the product of $(-1)^{i + j}$ with the determinant of the matrix that you get after removing the $i$-th row and $j$-th column.
So you can, for example, delete the last row and last column of the matrix $L$, and the absolute value of the determinant of the resulting matrix will give you the number of spanning trees.

The determinant of the matrix can be found in $O(N^3)$ by using the [Gaussian method](../linear_algebra/determinant-gauss.md).

The proof of this theorem is quite difficult and is not presented here; for an outline of the proof and variations of the theorem for graphs without multiple edges and for directed graphs refer to [Wikipedia](https://en.wikipedia.org/wiki/Kirchhoff%27s_theorem).

## Relation to Kirchhoff's circuit laws

Kirchhoff's matrix tree theorem and Kirchhoff's laws for electrical circuit are related in a beautiful way. It is possible to show (using Ohm's law and Kirchhoff's first law) that resistance $R_{ij}$ between two points of the circuit $i$ and $j$ is

$$R_{ij} = \frac{ \left| L^{(i,j)} \right| }{ | L^j | }.$$

Here the matrix $L$ is obtained from the matrix of inverse resistances $A$ ($A_{i,j}$ is inverse of the resistance of the conductor between points $i$ and $j$) using the procedure described in Kirchhoff's matrix tree theorem.
$T^j$ is the matrix with row and column $j$ removed, $T^{(i,j)}$ is the matrix with two rows and two columns $i$ and $j$ removed.

Kirchhoff's theorem gives this formula geometric meaning.

## অনুশীলন সমস্যা
 - [CODECHEF: Roads in Stars](https://www.codechef.com/problems/STARROAD)
 - [SPOJ: Maze](http://www.spoj.com/problems/KPMAZE/)
 - [CODECHEF: Complement Spanning Trees](https://www.codechef.com/problems/CSTREE)
