---
title: "মৌলিক জ্যামিতি"
tags: 
weight: 10
---
# মৌলিক জ্যামিতি

এই আর্টিকেলে আমরা ইউক্লিডীয় স্থানে বিন্দুর উপর মৌলিক অপারেশনগুলো দেখব, যেগুলো পুরো অ্যানালিটিক্যাল জ্যামিতির (analytical geometry) ভিত্তি তৈরি করে।
প্রতিটি বিন্দু $\mathbf r$ এর জন্য আমরা $\mathbf 0$ থেকে $\mathbf r$ এর দিকে নির্দেশিত ভেক্টর $\vec{\mathbf r}$ ধরব।
পরবর্তীতে আমরা $\mathbf r$ আর $\vec{\mathbf r}$ এর মধ্যে পার্থক্য করব না, এবং **বিন্দু** শব্দটা **ভেক্টর** এর সমার্থক হিসেবে ব্যবহার করব।

## লিনিয়ার অপারেশন

দ্বিমাত্রিক আর ত্রিমাত্রিক উভয় বিন্দুই লিনিয়ার স্পেস (linear space) বজায় রাখে। মানে এদের জন্য বিন্দুর যোগ আর বিন্দুকে কোনো সংখ্যা দিয়ে গুণ ডিফাইন করা আছে। এখানে দ্বিমাত্রিকের জন্য সেই মৌলিক ইমপ্লিমেন্টেশনগুলো দেওয়া হলো:

```cpp
struct point2d {
    ftype x, y;
    point2d() {}
    point2d(ftype x, ftype y): x(x), y(y) {}
    point2d& operator+=(const point2d &t) {
        x += t.x;
        y += t.y;
        return *this;
    }
    point2d& operator-=(const point2d &t) {
        x -= t.x;
        y -= t.y;
        return *this;
    }
    point2d& operator*=(ftype t) {
        x *= t;
        y *= t;
        return *this;
    }
    point2d& operator/=(ftype t) {
        x /= t;
        y /= t;
        return *this;
    }
    point2d operator+(const point2d &t) const {
        return point2d(*this) += t;
    }
    point2d operator-(const point2d &t) const {
        return point2d(*this) -= t;
    }
    point2d operator*(ftype t) const {
        return point2d(*this) *= t;
    }
    point2d operator/(ftype t) const {
        return point2d(*this) /= t;
    }
};
point2d operator*(ftype a, point2d b) {
    return b * a;
}
```
এবং ত্রিমাত্রিক বিন্দু:
```cpp
struct point3d {
    ftype x, y, z;
    point3d() {}
    point3d(ftype x, ftype y, ftype z): x(x), y(y), z(z) {}
    point3d& operator+=(const point3d &t) {
        x += t.x;
        y += t.y;
        z += t.z;
        return *this;
    }
    point3d& operator-=(const point3d &t) {
        x -= t.x;
        y -= t.y;
        z -= t.z;
        return *this;
    }
    point3d& operator*=(ftype t) {
        x *= t;
        y *= t;
        z *= t;
        return *this;
    }
    point3d& operator/=(ftype t) {
        x /= t;
        y /= t;
        z /= t;
        return *this;
    }
    point3d operator+(const point3d &t) const {
        return point3d(*this) += t;
    }
    point3d operator-(const point3d &t) const {
        return point3d(*this) -= t;
    }
    point3d operator*(ftype t) const {
        return point3d(*this) *= t;
    }
    point3d operator/(ftype t) const {
        return point3d(*this) /= t;
    }
};
point3d operator*(ftype a, point3d b) {
    return b * a;
}
```

এখানে `ftype` হলো স্থানাঙ্কের জন্য ব্যবহৃত কোনো টাইপ, সাধারণত `int`, `double` বা `long long`।

## ডট প্রোডাক্ট

### সংজ্ঞা
ভেক্টর $\mathbf a$ আর $\mathbf b$ এর ডট (বা স্কেলার) প্রোডাক্ট $\mathbf a \cdot \mathbf b$ দুটো সমতুল্য উপায়ে ডিফাইন করা যায়।
জ্যামিতিকভাবে এটি হলো প্রথম ভেক্টরের দৈর্ঘ্যের সাথে দ্বিতীয় ভেক্টরের প্রথমটির উপর অভিক্ষেপের দৈর্ঘ্যের গুণফল।
নিচের চিত্র থেকে দেখা যায় এই অভিক্ষেপ হলো $|\mathbf a| \cos \theta$ যেখানে $\theta$ হলো $\mathbf a$ ও $\mathbf b$ এর মধ্যবর্তী কোণ। সুতরাং $\mathbf a\cdot  \mathbf b = |\mathbf a| \cos \theta \cdot |\mathbf b|$।

<div style="text-align: center;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Dot_Product.svg/300px-Dot_Product.svg.png" alt="">
</div>

ডট প্রোডাক্টের কিছু উল্লেখযোগ্য ধর্ম:

১. $\mathbf a \cdot \mathbf b = \mathbf b \cdot \mathbf a$
২. $(\alpha \cdot \mathbf a)\cdot \mathbf b = \alpha \cdot (\mathbf a \cdot \mathbf b)$
৩. $(\mathbf a + \mathbf b)\cdot \mathbf c = \mathbf a \cdot \mathbf c + \mathbf b \cdot \mathbf c$

অর্থাৎ এটি একটি বিনিময়যোগ্য ফাংশন যা উভয় আর্গুমেন্টের সাপেক্ষে লিনিয়ার।
একক ভেক্টরগুলোকে এভাবে চিহ্নিত করি

$$\mathbf e_x = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \mathbf e_y = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \mathbf e_z = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}.$$

এই চিহ্নিতকরণে আমরা ভেক্টর $\mathbf r = (x;y;z)$-কে $r = x \cdot \mathbf e_x + y \cdot \mathbf e_y + z \cdot \mathbf e_z$ হিসেবে লিখতে পারি।
এবং যেহেতু একক ভেক্টরের জন্য

$$\mathbf e_x\cdot \mathbf e_x = \mathbf e_y\cdot \mathbf e_y = \mathbf e_z\cdot \mathbf e_z = 1,\\
\mathbf e_x\cdot \mathbf e_y = \mathbf e_y\cdot \mathbf e_z = \mathbf e_z\cdot \mathbf e_x = 0$$

আমরা দেখতে পাই যে স্থানাঙ্কের ক্ষেত্রে $\mathbf a = (x_1;y_1;z_1)$ ও $\mathbf b = (x_2;y_2;z_2)$ এর জন্য

$$\mathbf a\cdot \mathbf b = (x_1 \cdot \mathbf e_x + y_1 \cdot\mathbf e_y + z_1 \cdot\mathbf e_z)\cdot( x_2 \cdot\mathbf e_x + y_2 \cdot\mathbf e_y + z_2 \cdot\mathbf e_z) = x_1 x_2 + y_1 y_2 + z_1 z_2$$

এটাই ডট প্রোডাক্টের বীজগণিতিক সংজ্ঞা। এটা থেকে আমরা হিসাব করার ফাংশন লিখতে পারি।

```cpp
ftype dot(point2d a, point2d b) {
    return a.x * b.x + a.y * b.y;
}
ftype dot(point3d a, point3d b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}
```

সমস্যা সমাধানের সময় ডট প্রোডাক্ট হিসাবের জন্য বীজগণিতিক সংজ্ঞা ব্যবহার করা উচিত, কিন্তু ব্যবহারের জন্য জ্যামিতিক সংজ্ঞা ও ধর্মগুলো মনে রাখা উচিত।

### ধর্মসমূহ

আমরা ডট প্রোডাক্ট দিয়ে অনেক জ্যামিতিক প্রোপার্টি ডিফাইন করতে পারি।
উদাহরণস্বরূপ

১. $\mathbf a$ এর নর্ম (বর্গ দৈর্ঘ্য): $|\mathbf a|^2 = \mathbf a\cdot \mathbf a$
২. $\mathbf a$ এর দৈর্ঘ্য: $|\mathbf a| = \sqrt{\mathbf a\cdot \mathbf a}$
৩. $\mathbf a$-র $\mathbf b$ এর উপর অভিক্ষেপ: $\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf b|}$
৪. ভেক্টরদ্বয়ের মধ্যবর্তী কোণ: $\arccos \left(\dfrac{\mathbf a\cdot \mathbf b}{|\mathbf a| \cdot |\mathbf b|}\right)$
৫. আগের পয়েন্ট থেকে আমরা দেখতে পাই যে ডট প্রোডাক্ট ধনাত্মক হয় যদি তাদের মধ্যবর্তী কোণ সূক্ষ্ম হয়, ঋণাত্মক হয় যদি স্থূল হয়, আর শূন্য হয় যদি তারা লম্ব হয় — মানে সমকোণ তৈরি করে।

লক্ষ্য করো, এই সব ফাংশন ডাইমেনশনের সংখ্যার উপর নির্ভর করে না, তাই 2D আর 3D কেসে একই হবে:

```cpp
ftype norm(point2d a) {
    return dot(a, a);
}
double abs(point2d a) {
    return sqrt(norm(a));
}
double proj(point2d a, point2d b) {
    return dot(a, b) / abs(b);
}
double angle(point2d a, point2d b) {
    return acos(dot(a, b) / abs(a) / abs(b));
}
```

পরবর্তী গুরুত্বপূর্ণ প্রোপার্টিটা বুঝতে আমাদের সেই বিন্দুগুলোর সেট $\mathbf r$ দেখতে হবে যাদের জন্য কোনো নির্দিষ্ট ধ্রুবক $C$-তে $\mathbf r\cdot \mathbf a = C$।
দেখা যায় এই বিন্দুর সেটটা হলো ঠিক সেই বিন্দুগুলো যাদের $\mathbf a$ এর উপর প্রজেকশন হলো $C \cdot \dfrac{\mathbf a}{|\mathbf a| ^ 2}$ বিন্দু, আর এরা $\mathbf a$-র সাথে লম্ব একটা হাইপারপ্লেন (hyperplane) তৈরি করে।
নিচের 2D চিত্রে তুমি $\mathbf a$ ভেক্টরটা এবং একই ডট প্রোডাক্টবিশিষ্ট কয়েকটা ভেক্টর দেখতে পাবে:

<div style="text-align: center;">
  <img src="https://i.imgur.com/eyO7St4.png" alt="Vectors having same dot product with a">
</div>

দ্বিমাত্রিকে এই ভেক্টরগুলো একটি রেখা গঠন করবে, ত্রিমাত্রিকে একটি সমতল গঠন করবে।
লক্ষ্য করো, এই ফলাফল আমাদের 2D-তে একটা রেখাকে $\mathbf r\cdot \mathbf n=C$ বা $(\mathbf r - \mathbf r_0)\cdot \mathbf n=0$ হিসেবে ডিফাইন করতে দেয়, যেখানে $\mathbf n$ হলো রেখার সাথে লম্ব ভেক্টর আর $\mathbf r_0$ হলো রেখার উপর আগে থেকেই থাকা যেকোনো ভেক্টর, এবং $C = \mathbf r_0\cdot \mathbf n$।
একইভাবে 3D-তে একটা সমতল ডিফাইন করা যায়।

## ক্রস প্রোডাক্ট

### সংজ্ঞা

ধরো, ত্রিমাত্রিক স্থানে তোমার তিনটা ভেক্টর $\mathbf a$, $\mathbf b$ এবং $\mathbf c$ আছে যেগুলো নিচের চিত্রের মতো একটা সামান্তরিকে (parallelepiped) যুক্ত:
<div style="text-align: center;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Parallelepiped_volume.svg/240px-Parallelepiped_volume.svg.png" alt="Three vectors">
</div>

তুমি এর আয়তন কীভাবে বের করবে?
স্কুল থেকে আমরা জানি যে ভূমির ক্ষেত্রফলকে উচ্চতা দিয়ে গুণ করতে হবে, যেটা হলো ভূমির সাথে লম্ব দিকে $\mathbf a$ এর প্রজেকশন।
তারমানে, যদি আমরা $\mathbf b \times \mathbf c$-কে সেই ভেক্টর হিসেবে ডিফাইন করি যেটা $\mathbf b$ আর $\mathbf c$ উভয়ের সাথে লম্ব এবং যার দৈর্ঘ্য $\mathbf b$ আর $\mathbf c$ দিয়ে তৈরি সামান্তরিকের ক্ষেত্রফলের সমান, তাহলে $|\mathbf a\cdot (\mathbf b\times\mathbf c)|$ হবে সামান্তরিকের আয়তনের সমান।
পুরোপুরি বলতে গেলে, $\mathbf b\times \mathbf c$ সবসময় এমনভাবে নির্দেশিত থাকবে যাতে $\mathbf b\times \mathbf c$ এর দিক থেকে দেখলে $\mathbf b$ থেকে $\mathbf c$-তে ঘোরাটা সবসময় ঘড়ির কাঁটার বিপরীতে হয় (নিচের চিত্র দেখো)।

<div style="text-align: center;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Cross_product_vector.svg/250px-Cross_product_vector.svg.png" alt="cross product">
</div>

এটাই ভেক্টর $\mathbf b$ আর $\mathbf c$ এর ক্রস (বা ভেক্টর) প্রোডাক্ট $\mathbf b\times \mathbf c$ এবং ভেক্টর $\mathbf a$, $\mathbf b$ আর $\mathbf c$ এর ট্রিপল প্রোডাক্ট $\mathbf a\cdot(\mathbf b\times \mathbf c)$ ডিফাইন করে।

ক্রস ও ট্রিপল প্রোডাক্টের কিছু উল্লেখযোগ্য ধর্ম:

১.  $\mathbf a\times \mathbf b = -\mathbf b\times \mathbf a$
২.  $(\alpha \cdot \mathbf a)\times \mathbf b = \alpha \cdot (\mathbf a\times \mathbf b)$
৩.  যেকোনো $\mathbf b$ ও $\mathbf c$ এর জন্য ঠিক একটি ভেক্টর $\mathbf r$ আছে যেন সব ভেক্টর $\mathbf a$ এর জন্য $\mathbf a\cdot (\mathbf b\times \mathbf c) = \mathbf a\cdot\mathbf r$। <br>আসলে যদি এরকম দুটি ভেক্টর $\mathbf r_1$ ও $\mathbf r_2$ থাকে তাহলে সব ভেক্টর $\mathbf a$ এর জন্য $\mathbf a\cdot (\mathbf r_1 - \mathbf r_2)=0$ যা কেবল $\mathbf r_1 = \mathbf r_2$ হলেই সম্ভব।
৪.  $\mathbf a\cdot (\mathbf b\times \mathbf c) = \mathbf b\cdot (\mathbf c\times \mathbf a) = -\mathbf a\cdot( \mathbf c\times \mathbf b)$
৫.  $(\mathbf a + \mathbf b)\times \mathbf c = \mathbf a\times \mathbf c + \mathbf b\times \mathbf c$।
    আসলে সব ভেক্টর $\mathbf r$ এর জন্য ইকুয়েশনের শৃঙ্খল প্রযোজ্য:

    \[\mathbf r\cdot( (\mathbf a + \mathbf b)\times \mathbf c) = (\mathbf a + \mathbf b) \cdot (\mathbf c\times \mathbf r) =  \mathbf a \cdot(\mathbf c\times \mathbf r) + \mathbf b\cdot(\mathbf c\times \mathbf r) = \mathbf r\cdot (\mathbf a\times \mathbf c) + \mathbf r\cdot(\mathbf b\times \mathbf c) = \mathbf r\cdot(\mathbf a\times \mathbf c + \mathbf b\times \mathbf c)\]

    যা বিন্দু ৩ অনুসারে $(\mathbf a + \mathbf b)\times \mathbf c = \mathbf a\times \mathbf c + \mathbf b\times \mathbf c$ প্রুফ করে।

৬.  $|\mathbf a\times \mathbf b|=|\mathbf a| \cdot |\mathbf b| \sin \theta$ যেখানে $\theta$ হলো $\mathbf a$ ও $\mathbf b$ এর মধ্যবর্তী কোণ, কারণ $|\mathbf a\times \mathbf b|$ হলো $\mathbf a$ ও $\mathbf b$ দ্বারা গঠিত সামান্তরিকের ক্ষেত্রফলের সমান।

এই সব আর একক ভেক্টরের জন্য নিচের ইকুয়েশন প্রযোজ্য দেওয়া থাকলে

$$\mathbf e_x\times \mathbf e_x = \mathbf e_y\times \mathbf e_y = \mathbf e_z\times \mathbf e_z = \mathbf 0,\\
\mathbf e_x\times \mathbf e_y = \mathbf e_z,~\mathbf e_y\times \mathbf e_z = \mathbf e_x,~\mathbf e_z\times \mathbf e_x = \mathbf e_y$$

আমরা $\mathbf a = (x_1;y_1;z_1)$ ও $\mathbf b = (x_2;y_2;z_2)$ এর ক্রস প্রোডাক্ট স্থানাঙ্ক আকারে হিসাব করতে পারি:

$$\mathbf a\times \mathbf b = (x_1 \cdot \mathbf e_x + y_1 \cdot \mathbf e_y + z_1 \cdot \mathbf e_z)\times (x_2 \cdot \mathbf e_x + y_2 \cdot \mathbf e_y + z_2 \cdot \mathbf e_z) =$$

$$(y_1 z_2 - z_1 y_2)\mathbf e_x  + (z_1 x_2 - x_1 z_2)\mathbf e_y + (x_1 y_2 - y_1 x_2)\mathbf e_z$$

যা আরো মার্জিত আকারেও লেখা যায়:

$$\mathbf a\times \mathbf b = \begin{vmatrix}\mathbf e_x & \mathbf e_y & \mathbf e_z \\ x_1 & y_1 & z_1 \\ x_2 & y_2 & z_2 \end{vmatrix},~a\cdot(b\times c) = \begin{vmatrix} x_1 & y_1 & z_1 \\ x_2 & y_2 & z_2 \\ x_3 & y_3 & z_3 \end{vmatrix}$$

এখানে $| \cdot |$ হলো ম্যাট্রিক্সের ডিটারমিন্যান্ট (determinant)।

ক্রস প্রোডাক্টের একধরনের রূপ (যথা সুডো-স্কেলার প্রোডাক্ট) দ্বিমাত্রিক ক্ষেত্রেও বাস্তবায়ন করা যায়।
যদি আমরা $\mathbf a$ ও $\mathbf b$ ভেক্টর দ্বারা গঠিত সামান্তরিকের ক্ষেত্রফল হিসাব করতে চাই তাহলে $|\mathbf e_z\cdot(\mathbf a\times \mathbf b)| = |x_1 y_2 - y_1 x_2|$ হিসাব করতে হবে।
একই ফলাফল পাওয়ার আরেকটি উপায় হলো $|\mathbf a|$ (সামান্তরিকের ভূমি) কে উচ্চতা দিয়ে গুণ করা, যা $90^\circ$ ঘোরানো $\mathbf a$ ভেক্টরের উপর $\mathbf b$ ভেক্টরের অভিক্ষেপ যা হলো $\widehat{\mathbf a}=(-y_1;x_1)$।
অর্থাৎ, $|\widehat{\mathbf a}\cdot\mathbf b|=|x_1y_2 - y_1 x_2|$ হিসাব করা।

যদি আমরা চিহ্ন কনসিডার করি তাহলে ক্ষেত্রফল ধনাত্মক হবে যদি $\mathbf a$ থেকে $\mathbf b$-তে ঘূর্ণন (অর্থাৎ $\mathbf e_z$ বিন্দুর দৃষ্টিকোণ থেকে) ঘড়ির কাঁটার বিপরীতে হয় এবং ঋণাত্মক অন্যথায়।
এটাই সুডো-স্কেলার প্রোডাক্ট ডিফাইন করে।
লক্ষ্য করো, এটা $|\mathbf a| \cdot |\mathbf b| \sin \theta$ এর সমানও, যেখানে $\theta$ হলো $\mathbf a$ থেকে $\mathbf b$ পর্যন্ত ঘড়ির কাঁটার বিপরীতে মাপা কোণ (আর ঋণাত্মক যদি ঘোরাটা ঘড়ির কাঁটার দিকে হয়)।

চলো এই সবকিছু ইমপ্লিমেন্ট করি!

```cpp
point3d cross(point3d a, point3d b) {
    return point3d(a.y * b.z - a.z * b.y,
                   a.z * b.x - a.x * b.z,
                   a.x * b.y - a.y * b.x);
}
ftype triple(point3d a, point3d b, point3d c) {
    return dot(a, cross(b, c));
}
ftype cross(point2d a, point2d b) {
    return a.x * b.y - a.y * b.x;
}
```

### ধর্মসমূহ

ক্রস প্রোডাক্টের ক্ষেত্রে, এটি শূন্য ভেক্টরের সমান হয় যদি এবং কেবল যদি ভেক্টর $\mathbf a$ ও $\mathbf b$ সমরেখ হয় (তারা একটি সাধারণ রেখা গঠন করে, অর্থাৎ সমান্তরাল)।
একই কথা ট্রিপল প্রোডাক্টের ক্ষেত্রেও প্রযোজ্য, এটি শূন্য হয় যদি এবং কেবল যদি ভেক্টর $\mathbf a$, $\mathbf b$ ও $\mathbf c$ সমতলীয় হয় (তারা একটি সাধারণ সমতল গঠন করে)।

এটা থেকে আমরা রেখা আর সমতল ডিফাইন করার সার্বজনীন ইকুয়েশন পেতে পারি।
একটা রেখা তার দিক ভেক্টর $\mathbf d$ আর একটা প্রারম্ভিক বিন্দু $\mathbf r_0$ দিয়ে, অথবা দুটো বিন্দু $\mathbf a$ আর $\mathbf b$ দিয়ে ডিফাইন করা যায়।
এটা $(\mathbf r - \mathbf r_0)\times\mathbf d=0$ বা $(\mathbf r - \mathbf a)\times (\mathbf b - \mathbf a) = 0$ হিসেবে ডিফাইন করা হয়।
সমতলের ক্ষেত্রে, এটা তিনটা বিন্দু $\mathbf a$, $\mathbf b$ আর $\mathbf c$ দিয়ে $(\mathbf r - \mathbf a)\cdot((\mathbf b - \mathbf a)\times (\mathbf c - \mathbf a))=0$ হিসেবে, অথবা প্রারম্ভিক বিন্দু $\mathbf r_0$ আর এই সমতলে থাকা দুটো দিক ভেক্টর $\mathbf d_1$ ও $\mathbf d_2$ দিয়ে $(\mathbf r - \mathbf r_0)\cdot(\mathbf d_1\times \mathbf d_2)=0$ হিসেবে ডিফাইন করা যায়।

দ্বিমাত্রিকে সুডো-স্কেলার প্রোডাক্টও দুটি ভেক্টরের মধ্যে অরিয়েন্টেশন পরীক্ষা করতে ব্যবহার করা যায় কারণ প্রথম থেকে দ্বিতীয় ভেক্টরে ঘূর্ণন ঘড়ির কাঁটার বিপরীতে হলে এটি ধনাত্মক এবং অন্যথায় ঋণাত্মক।
আর অবশ্যই, এটা পলিগনের ক্ষেত্রফল বের করতেও ব্যবহার করা যায়, যেটা আলাদা একটা আর্টিকেলে দেখানো হয়েছে।
ত্রিমাত্রিক স্থানে একই উদ্দেশ্যে ট্রিপল প্রোডাক্ট ব্যবহার করা যায়।

## অনুশীলনী

### রেখার ছেদবিন্দু

2D-তে একটা রেখা ডিফাইন করার অনেক সম্ভাব্য উপায় আছে আর তোমার সেগুলো মিলিয়ে ব্যবহার করতে দ্বিধা করা উচিত না।
উদাহরণস্বরূপ আমাদের দুটি রেখা আছে এবং আমরা তাদের ছেদবিন্দু খুঁজতে চাই।
আমরা বলতে পারি প্রথম রেখার সব বিন্দু $\mathbf r = \mathbf a_1 + t \cdot \mathbf d_1$ হিসেবে প্যারামেট্রাইজ করা যায় যেখানে $\mathbf a_1$ হলো প্রারম্ভিক বিন্দু, $\mathbf d_1$ হলো দিক এবং $t$ কোনো বাস্তব প্যারামিটার।
দ্বিতীয় রেখার সব বিন্দুকে $(\mathbf r - \mathbf a_2)\times \mathbf d_2=0$ সন্তুষ্ট করতে হবে। এটি থেকে আমরা সহজেই প্যারামিটার $t$ খুঁজতে পারি:

$$(\mathbf a_1 + t \cdot \mathbf d_1 - \mathbf a_2)\times \mathbf d_2=0 \quad\Rightarrow\quad t = \dfrac{(\mathbf a_2 - \mathbf a_1)\times\mathbf d_2}{\mathbf d_1\times \mathbf d_2}$$

চলো দুটো রেখার ছেদবিন্দু বের করার ফাংশন ইমপ্লিমেন্ট করি।

```cpp
point2d intersect(point2d a1, point2d d1, point2d a2, point2d d2) {
    return a1 + cross(a2 - a1, d2) / cross(d1, d2) * d1;
}
```

### সমতলের ছেদবিন্দু

তবে কখনো কখনো জ্যামিতিক ইনটুইশন ব্যবহার করা কঠিন হতে পারে।
যেমন ধরো, তোমাকে প্রারম্ভিক বিন্দু $\mathbf a_i$ আর দিক $\mathbf d_i$ দিয়ে ডিফাইন করা তিনটা সমতল দেওয়া আছে আর তুমি তাদের ছেদবিন্দু খুঁজতে চাও।
তুমি লক্ষ্য করবে যে তোমাকে শুধু এই ইকুয়েশন সিস্টেমটা সমাধান করতে হবে:

$$\begin{cases}\mathbf r\cdot \mathbf n_1 = \mathbf a_1\cdot \mathbf n_1, \\ \mathbf r\cdot \mathbf n_2 = \mathbf a_2\cdot \mathbf n_2, \\ \mathbf r\cdot \mathbf n_3 = \mathbf a_3\cdot \mathbf n_3\end{cases}$$

জ্যামিতিক পদ্ধতি নিয়ে মাথা ঘামানোর বদলে, তুমি একটা বীজগণিতিক পদ্ধতি বানাতে পারো যেটা সাথে সাথেই পাওয়া যায়।
যেমন, তুমি যদি আগেই একটা পয়েন্ট ক্লাস ইমপ্লিমেন্ট করে রাখো, তাহলে ক্র্যামারের নিয়ম (Cramer's rule) দিয়ে এই সিস্টেম সমাধান করা তোমার জন্য সহজ হবে — কারণ ট্রিপল প্রোডাক্ট আসলে সেই ম্যাট্রিক্সের ডিটারমিন্যান্ট যেটা ভেক্টরগুলোকে কলাম হিসেবে নিলে পাওয়া যায়:

```cpp
point3d intersect(point3d a1, point3d n1, point3d a2, point3d n2, point3d a3, point3d n3) {
    point3d x(n1.x, n2.x, n3.x);
    point3d y(n1.y, n2.y, n3.y);
    point3d z(n1.z, n2.z, n3.z);
    point3d d(dot(a1, n1), dot(a2, n2), dot(a3, n3));
    return point3d(triple(d, y, z),
                   triple(x, d, z),
                   triple(x, y, d)) / triple(n1, n2, n3);
}
```

এখন তুমি নিজে সাধারণ জ্যামিতিক অপারেশনের পদ্ধতি বের করার চেষ্টা করতে পারো — এই সবকিছুতে অভ্যস্ত হতে।
