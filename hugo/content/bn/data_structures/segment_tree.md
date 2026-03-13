---
title: "সেগমেন্ট ট্রি"
tags: 
weight: 40
---
# সেগমেন্ট ট্রি

সেগমেন্ট ট্রি (Segment Tree) হলো এমন একটা ডাটা স্ট্রাকচার যেটা অ্যারের ইন্টারভাল সংক্রান্ত তথ্য ট্রি আকারে রাখে। এটা দিয়ে তুমি অ্যারের উপর রেঞ্জ কুয়েরি দ্রুত করতে পারবে, আবার অ্যারে আপডেটও করতে পারবে।
যেমন, $a[l \dots r]$ রেঞ্জের যোগফল বের করা বা মিনিমাম বের করা — সব $O(\log n)$ সময়ে হয়ে যায়।
কুয়েরির পাশাপাশি, সেগমেন্ট ট্রি দিয়ে তুমি একটা নির্দিষ্ট এলিমেন্ট বদলাতে পারবে, বা পুরো একটা সাবসেগমেন্টের সব এলিমেন্টে কিছু যোগ করতে বা নতুন মান বসাতে পারবে।

মোটের উপর, সেগমেন্ট ট্রি খুবই ফ্লেক্সিবল একটা ডাটা স্ট্রাকচার। এটা দিয়ে বিশাল সংখ্যক প্রবলেম সলভ করা যায়।
আরও জটিল অপারেশন আর কুয়েরিও হ্যান্ডেল করা সম্ভব (দেখো [সেগমেন্ট ট্রির অ্যাডভান্সড ভার্সন](segment_tree.md#advanced-versions-of-segment-trees))।
সেগমেন্ট ট্রি সহজেই হায়ার ডাইমেনশনে নিয়ে যাওয়া যায়।
যেমন, 2D সেগমেন্ট ট্রি দিয়ে তুমি একটা ম্যাট্রিক্সের যেকোনো সাবরেক্ট্যাঙ্গেলের সাম বা মিনিমাম $O(\log^2 n)$ সময়ে বের করতে পারবে।

সেগমেন্ট ট্রির একটা বড় সুবিধা হলো এটার মেমোরি লাগে লিনিয়ার।
$n$ সাইজের অ্যারের জন্য স্ট্যান্ডার্ড সেগমেন্ট ট্রিতে $4n$ ভার্টেক্স লাগে।

## সেগমেন্ট ট্রির সহজতম রূপ

চলো সবচেয়ে সিম্পল ভার্সন দিয়ে শুরু করি।
আমরা সাম কুয়েরি দ্রুত করতে চাই।
প্রবলেমটা হলো এরকম:
একটা অ্যারে $a[0 \dots n-1]$ দেওয়া আছে। তোমাকে ইনডেক্স $l$ থেকে $r$ পর্যন্ত এলিমেন্টের যোগফল $\sum_{i=l}^r a[i]$ বের করতে হবে, আবার $a[i] = x$ টাইপের আপডেটও করতে হবে।
সেগমেন্ট ট্রি দিয়ে **দুটোই** $O(\log n)$ সময়ে করা যায়।

এটা নেইভ অ্যাপ্রোচের থেকে অনেক ভালো।
শুধু অ্যারে রাখলে আপডেট $O(1)$ এ হয়, কিন্তু সাম কুয়েরিতে $O(n)$ লাগে।
আর প্রিফিক্স সাম রাখলে কুয়েরি $O(1)$ এ হয়, কিন্তু একটা এলিমেন্ট আপডেট করলে প্রিফিক্স সামে $O(n)$ চেঞ্জ দরকার হয়।

### সেগমেন্ট ট্রির কাঠামো

এখানে আমরা ডিভাইড অ্যান্ড কনকার (Divide and Conquer) পদ্ধতি ফলো করি।
প্রথমে পুরো অ্যারে $a[0 \dots n-1]$ এর যোগফল বের করে রাখি।
তারপর অ্যারেটাকে দুই ভাগে ভাগ করি — $a[0 \dots (n-1)/2]$ আর $a[(n+1)/2 \dots n-1]$ — এবং দুই ভাগেরই যোগফল আলাদা করে রাখি।
প্রতিটা ভাগকে আবার অর্ধেক করি, এভাবে চলতে থাকে যতক্ষণ না সেগমেন্টের সাইজ $1$ হয়ে যায়।

এটাকে তুমি একটা বাইনারি ট্রি হিসেবে ভাবতে পারো।
ট্রির রুট হলো পুরো অ্যারে $a[0 \dots n-1]$, আর প্রতিটা নোডের (লিফ ছাড়া) ঠিক দুইটা চাইল্ড আছে।
এজন্যই এটাকে "সেগমেন্ট ট্রি" বলে। তবে বেশিরভাগ ইমপ্লিমেন্টেশনে আসল ট্রি বানানোর দরকার পড়ে না (দেখো [ইমপ্লিমেন্টেশন](segment_tree.md#implementation))।

$a = [1, 3, -2, 8, -7]$ অ্যারের জন্য সেগমেন্ট ট্রি দেখতে এরকম:

!["সাম সেগমেন্ট ট্রি"](/images/data_structures/sum-segment-tree.png)

এই বর্ণনা থেকেই বোঝা যায়, সেগমেন্ট ট্রিতে লিনিয়ার সংখ্যক ভার্টেক্স লাগে।
ট্রির প্রথম লেভেলে 1টা নোড (রুট), দ্বিতীয় লেভেলে 2টা, তৃতীয় লেভেলে 4টা — এভাবে $n$ পর্যন্ত যায়।
তারমানে সর্বোচ্চ ভার্টেক্স সংখ্যা $1 + 2 + 4 + \dots + 2^{\lceil\log_2 n\rceil} \lt 2^{\lceil\log_2 n\rceil + 1} \lt 4n$।

একটা জিনিস খেয়াল করো — $n$ যদি 2 এর পাওয়ার না হয়, তাহলে ট্রির সব লেভেল পুরোপুরি ভর্তি হবে না।
ছবিতেও সেটা দেখতে পাচ্ছ।
এখন এটা নিয়ে চিন্তা না করলেও চলবে, তবে ইমপ্লিমেন্টেশনের সময় কাজে লাগবে।

সেগমেন্ট ট্রির উচ্চতা $O(\log n)$, কারণ রুট থেকে লিফের দিকে নামলে প্রতিবার সেগমেন্ট সাইজ প্রায় অর্ধেক হয়ে যায়।

### নির্মাণ

সেগমেন্ট ট্রি বানানোর আগে দুইটা জিনিস ঠিক করতে হবে:

1. প্রতিটা নোডে কী *ভ্যালু* রাখবে।
   যেমন, সাম সেগমেন্ট ট্রিতে একটা নোড তার রেঞ্জ $[l, r]$ এর এলিমেন্টগুলোর যোগফল রাখবে।
2. দুইটা চাইল্ডকে কিভাবে *মার্জ* করবে।
   যেমন, সাম সেগমেন্ট ট্রিতে $a[l_1 \dots r_1]$ আর $a[l_2 \dots r_2]$ রেঞ্জের দুইটা নোড মার্জ হয়ে $a[l_1 \dots r_2]$ রেঞ্জের নোড বানাবে — শুধু দুই নোডের ভ্যালু যোগ করলেই হবে।

মনে রাখো, কোনো ভার্টেক্স "লিফ ভার্টেক্স" যদি সেটার সেগমেন্ট মূল অ্যারের শুধু একটা এলিমেন্ট কভার করে। এটা ট্রির সবচেয়ে নিচের লেভেলে থাকে। এর ভ্যালু হবে সেই এলিমেন্ট $a[i]$ এর সমান।

এখন ট্রি বানাতে, আমরা সবচেয়ে নিচের লেভেল (লিফ) থেকে শুরু করি আর সঠিক ভ্যালু বসাই। এরপর `merge` ফাংশন দিয়ে উপরের লেভেলের ভ্যালু বের করি।
এভাবে লেভেল বাই লেভেল উপরে উঠে রুট পর্যন্ত পৌঁছাই।

তবে এটা রিকার্সিভভাবে উল্টো দিক থেকে, মানে রুট থেকে লিফের দিকে, বর্ণনা করা বেশি সুবিধাজনক। কোনো নন-লিফ ভার্টেক্সের জন্য নির্মাণ প্রক্রিয়া এরকম:

1. দুইটা চাইল্ড ভার্টেক্সের ভ্যালু রিকার্সিভভাবে বানাও
2. চাইল্ডগুলোর ভ্যালু মার্জ করো।

রুট থেকে শুরু করলে পুরো সেগমেন্ট ট্রি বানানো হয়ে যায়।

এই নির্মাণের টাইম কমপ্লেক্সিটি $O(n)$, যদি মার্জ অপারেশন কনস্ট্যান্ট টাইমে হয় (মার্জ মোট $n$ বার কল হয়, যেটা ট্রির ইন্টারনাল নোডের সংখ্যার সমান)।

### সাম কুয়েরি

এবার সাম কুয়েরি কিভাবে কাজ করে দেখি। ইনপুট হিসেবে দুইটা ইন্টিজার $l$ আর $r$ পাবে, আর $a[l \dots r]$ এর যোগফল $O(\log n)$ এ বের করতে হবে।

এর জন্য আমরা সেগমেন্ট ট্রি ট্রাভার্স করব আর আগে থেকে হিসাব করা যোগফলগুলো কাজে লাগাব।
ধরো, তুমি এমন একটা ভার্টেক্সে আছ যেটা সেগমেন্ট $a[tl \dots tr]$ কভার করে।
তিনটা কেস হতে পারে।

সবচেয়ে সহজ কেস — কুয়েরি সেগমেন্ট $a[l \dots r]$ আর বর্তমান ভার্টেক্সের সেগমেন্ট একদম মিলে গেলে (মানে $a[l \dots r] = a[tl \dots tr]$)। তখন সোজা ভার্টেক্সে রাখা ভ্যালু রিটার্ন করলেই হবে।

আরেকটা কেস — কুয়েরি সেগমেন্ট পুরোটাই বাম অথবা ডান চাইল্ডের মধ্যে পড়ে।
মনে রাখো, বাম চাইল্ড $a[tl \dots tm]$ কভার করে আর ডান চাইল্ড $a[tm + 1 \dots tr]$ কভার করে, যেখানে $tm = (tl + tr) / 2$।
এই কেসে শুধু সেই চাইল্ডে গিয়ে একই অ্যালগরিদম চালালেই হবে।

আর শেষ কেস — কুয়েরি সেগমেন্ট দুই চাইল্ডেই পড়ে।
তখন দুইটা রিকার্সিভ কল করতে হবে, একটা বাম চাইল্ডে আর একটা ডান চাইল্ডে।
বাম চাইল্ড থেকে $a[l \dots tm]$ রেঞ্জের আংশিক উত্তর পাবে, ডান চাইল্ড থেকে $a[tm+1 \dots r]$ রেঞ্জের। দুইটা যোগ করলেই ফাইনাল উত্তর।
সোজা কথায়, বাম চাইল্ড দিয়ে সাম কুয়েরি $a[l \dots tm]$ আর ডান চাইল্ড দিয়ে সাম কুয়েরি $a[tm+1 \dots r]$ করি।

তাহলে সাম কুয়েরি মূলত একটা ফাংশন যেটা হয় একটা চাইল্ডে রিকার্সিভ কল করে (কুয়েরি বাউন্ডারি না বদলে), অথবা দুইটা চাইল্ডেই কল করে (কুয়েরিকে দুই ভাগে ভেঙে)।
কুয়েরি সেগমেন্টের সীমানা ভার্টেক্সের সেগমেন্টের সাথে মিলে গেলে রিকার্সন থামে।
সেক্ষেত্রে ট্রিতে আগে থেকে রাখা ভ্যালু রিটার্ন হয়।

মানে পুরো ব্যাপারটা একটা ট্রি ট্রাভার্সাল — দরকারি শাখাগুলোতে ঢুকে প্রি-কম্পিউটেড ভ্যালু কাজে লাগানো।

আমরা রুট ভার্টেক্স থেকে ট্রাভার্সাল শুরু করি।

নিচের ছবিতে ব্যাপারটা দেখানো হয়েছে।
আবার $a = [1, 3, -2, 8, -7]$ অ্যারে ধরো, আর আমরা $\sum_{i=2}^4 a[i]$ বের করতে চাই।
রঙিন ভার্টেক্সগুলো ভিজিট হবে, আর সবুজগুলোর প্রি-কম্পিউটেড ভ্যালু ব্যবহার হবে।
ফলাফল $-2 + 1 = -1$।

!["সাম সেগমেন্ট ট্রি কোয়েরি"](/images/data_structures/sum-segment-tree-query.png)

এই অ্যালগরিদমের কমপ্লেক্সিটি $O(\log n)$ কেন?
ট্রির প্রতিটা লেভেলে আমরা সর্বোচ্চ 4টা ভার্টেক্স ভিজিট করি — এটাই মূল কথা।
আর ট্রির উচ্চতা $O(\log n)$, তাই টোটাল টাইম $O(\log n)$।

এটা ইন্ডাকশন দিয়ে প্রুফ করা যায়।
প্রথম লেভেলে শুধু রুট ভিজিট হয়, তাই 4 এর কম।
এবার যেকোনো লেভেল ধরো। ইন্ডাকশন হাইপোথিসিস অনুযায়ী সেখানে সর্বোচ্চ 4টা ভার্টেক্স ভিজিট হয়।
যদি 2টা বা কম ভিজিট হয়, তাহলে পরের লেভেলে সর্বোচ্চ 4টা হবে — কারণ প্রতিটা ভার্টেক্স সর্বোচ্চ 2টা রিকার্সিভ কল করে।
এবার ধরো কোনো লেভেলে 3 বা 4টা ভার্টেক্স ভিজিট হচ্ছে।
মাঝের ভার্টেক্সগুলো ভালো করে দেখো।
যেহেতু সাম কুয়েরি একটা কন্টিগুয়াস সাবঅ্যারের জন্য, মাঝের ভার্টেক্সগুলোর সেগমেন্ট পুরোটাই কুয়েরি দিয়ে কভার হবে।
তারমানে এই ভার্টেক্সগুলো আর রিকার্সিভ কল করবে না।
শুধু সবচেয়ে বাম আর সবচেয়ে ডান ভার্টেক্স রিকার্সিভ কল করতে পারে।
আর সেগুলো মিলে সর্বোচ্চ 4টা কল করবে, তাই পরের লেভেলেও 4 এর বেশি হবে না।
বলা যায়, একটা ব্রাঞ্চ কুয়েরির বাম সীমানার দিকে যায় আর আরেকটা ডান সীমানার দিকে।

তাহলে মোট সর্বোচ্চ $4 \log n$ ভার্টেক্স ভিজিট হয়, যেটা $O(\log n)$।

সারমর্ম হলো, কুয়েরি ইনপুট সেগমেন্টকে কয়েকটা সাব-সেগমেন্টে ভাগ করে যেগুলোর যোগফল আগেই ট্রিতে রাখা আছে।
কুয়েরি সেগমেন্ট ভার্টেক্স সেগমেন্টের সাথে মিললেই ভাগ করা থামে, আর এরকম সেগমেন্ট লাগে মাত্র $O(\log n)$ টা। এটাই সেগমেন্ট ট্রির এফিশিয়েন্সি।

### আপডেট কুয়েরি

এবার ধরো, তুমি অ্যারের একটা নির্দিষ্ট এলিমেন্ট বদলাতে চাও — মানে $a[i] = x$ করতে চাও।
তাহলে সেগমেন্ট ট্রিও আপডেট করতে হবে যাতে নতুন অ্যারের সাথে মিলে যায়।

এটা সাম কুয়েরির চেয়ে সহজ।
ট্রির প্রতিটা লেভেল অ্যারের একটা পার্টিশন। তারমানে $a[i]$ প্রতিটা লেভেলে শুধু একটা সেগমেন্টে পড়ে।
তাই মাত্র $O(\log n)$ টা ভার্টেক্স আপডেট করলেই হবে।

এটা রিকার্সিভ ফাংশন দিয়ে সহজে করা যায়।
ফাংশনটা বর্তমান ভার্টেক্স নিয়ে কাজ করে — দুই চাইল্ডের মধ্যে যেটার সেগমেন্টে $a[i]$ আছে সেটাতে রিকার্সিভ কল করে, তারপর বিল্ড মেথডের মতোই দুই চাইল্ডের যোগফল দিয়ে নিজের ভ্যালু আপডেট করে।

নিচে একই অ্যারে দিয়ে একটা ভিজ্যুয়ালাইজেশন দেওয়া হলো।
এখানে আমরা $a[2] = 3$ আপডেট করছি।
সবুজ ভার্টেক্সগুলো হলো যেগুলো ভিজিট করে আপডেট করা হয়েছে।

!["সাম সেগমেন্ট ট্রি আপডেট"](/images/data_structures/sum-segment-tree-update.png)

### ইমপ্লিমেন্টেশন ### { #implementation}

প্রধান কনসিডার হল সেগমেন্ট ট্রি কীভাবে সংরক্ষণ করা যায়।
অবশ্যই আমরা একটি $\text{vertex}$ স্ট্রাক্ট সংজ্ঞায়িত করতে পারি এবং বস্তু তৈরি করতে পারি, যা সেগমেন্টের সীমানা, এর যোগফল এবং অতিরিক্তভাবে এর চাইল্ড ভার্টেক্সের পয়েন্টার সংরক্ষণ করে।
তবে, এটি পয়েন্টার আকারে অনেক রিডানড্যান্ট তথ্য সংরক্ষণ করতে প্রয়োজন।
আমরা একটি সরল কৌশল ব্যবহার করব এটি আরও দক্ষ করতে একটি _ইমপ্লিসিট ডেটা স্ট্রাকচার_ ব্যবহার করে: শুধুমাত্র একটি অ্যারেতে যোগফল সংরক্ষণ করা।
(একটি অনুরূপ পদ্ধতি বাইনারি হিপের জন্য ব্যবহার করা হয়)।
সূচক १ এ রুট ভার্টেক্সের যোগফল, সূচক २ এবং ३ এ এর দুটি চাইল্ড ভার্টেক্সের যোগফল, সূচক ४ থেকে ७ এ সেই দুটি ভার্টেক্সের চাইল্ডদের যোগফল, এবং এভাবে চলে।
१-ইন্ডেক্সিং সহ, সুবিধামত সূচক $i$ এ একটি ভার্টেক্সের বাম চাইল্ড সূচক $२i$ তে স্টোর করা হয়, এবং ডানটি সূচক $२i + १$ তে।
সমানভাবে, সূচক $i$ এ একটি ভার্টেক্সের পিতামাতা $i/२$ তে স্টোর করা হয় (পূর্ণসংখ্যা বিভাগ)।

এটি ইমপ্লিমেন্টেশনকে অনেক সহজ করে।
আমাদের স্মৃতিতে ট্রির কাঠামো সংরক্ষণ করতে হবে না।
এটি অন্তর্নিহিতভাবে সংজ্ঞায়িত।
আমাদের শুধুমাত্র একটি অ্যারে প্রয়োজন যা সমস্ত সেগমেন্টের যোগফল ধারণ করে।

আগে উল্লেখ করা হয়েছে, আমাদের সর্বাধিক $4n$ ভার্টেক্স সংরক্ষণ করতে হবে।
এটি কম হতে পারে, তবে সুবিধার জন্য আমরা সর্বদা আকার $4n$ এর একটি অ্যারে বরাদ্দ করি।
যোগফল অ্যারেতে এমন কিছু উপাদান থাকবে যা প্রকৃত ট্রিতে কোনো ভার্টেক্সের সাথে সম্পর্কিত নয়, তবে এটি ইমপ্লিমেন্টেশনকে জটিল করে না।

তাই আমরা সেগমেন্ট ট্রি সহজভাবে একটি অ্যারে $t[]$ হিসাবে ইনপুট আকার $n$ এর চারগুণ আকার সহ সংরক্ষণ করি:

```cpp
int n, t[4*MAXN];
```

একটা দেওয়া অ্যারে $a[]$ থেকে সেগমেন্ট ট্রি নির্মাণের পদ্ধতি এইরকম দেখায়:
এটি প্যারামিটার $a[]$ (ইনপুট অ্যারে), $v$ (বর্তমান ভার্টেক্সের সূচক), এবং বর্তমান সেগমেন্টের সীমানা $tl$ এবং $tr$ সহ একটি রিকার্সিভ ফাংশন।
প্রধান প্রোগ্রামে এই ফাংশনটি রুট ভার্টেক্সের প্যারামিটার সহ বলা হবে: $v = १$, $tl = ०$, এবং $tr = n - १$।

```cpp
void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = t[v*2] + t[v*2+1];
    }
}
```

এর বাইরে সাম কোয়েরিতে উত্তর দেওয়ার ফাংশনটিও একটি রিকার্সিভ ফাংশন, যা বর্তমান ভার্টেক্স/সেগমেন্ট সম্পর্কিত তথ্য (অর্থাৎ সূচক $v$ এবং সীমানা $tl$ এবং $tr$) এবং কোয়েরির সীমানা সম্পর্কিত তথ্য $l$ এবং $r$ প্যারামিটার হিসাবে পায়।
কোড সরল করার জন্য, এই ফাংশনটি সর্বদা দুটি রিকার্সিভ কল সম্পাদন করে, এমনকি যদি শুধুমাত্র একটি প্রয়োজন হয় - সেই ক্ষেত্রে অতিরিক্ত রিকার্সিভ কলটি $l > r$ হবে, এবং এটি ফাংশনের শুরুতে একটি অতিরিক্ত চেক ব্যবহার করে সহজেই ধরা যেতে পারে।

```cpp
int sum(int v, int tl, int tr, int l, int r) {
    if (l > r)
        return 0;
    if (l == tl && r == tr) {
        return t[v];
    }
    int tm = (tl + tr) / 2;
    return sum(v*2, tl, tm, l, min(r, tm))
           + sum(v*2+1, tm+1, tr, max(l, tm+1), r);
}
```

অবশেষে আপডেট কোয়েরি। ফাংশনটি বর্তমান ভার্টেক্স/সেগমেন্ট সম্পর্কিত তথ্যও পাবে, এবং অতিরিক্তভাবে আপডেট কোয়েরির প্যারামিটার (অর্থাৎ উপাদানের অবস্থান এবং এর নতুন মান)।

```cpp
void update(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        t[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
        t[v] = t[v*2] + t[v*2+1];
    }
}
```

### মেমোরি সাশ্রয়ী ইমপ্লিমেন্টেশন

বেশিরভাগ মানুষ আগের বিভাগ থেকে ইমপ্লিমেন্টেশন ব্যবহার করে। যদি আপনি অ্যারে `t` তাকান আপনি দেখতে পারবেন যে এটি একটি BFS ট্রাভার্সাল (স্তর-অর্ডার ট্রাভার্সাল) এর ক্রমে ট্রি নোডের নাম্বারিং অনুসরণ করে।
এই ট্রাভার্সাল ব্যবহার করে ভার্টেক্স $v$ এর চাইল্ডগুলি যথাক্রমে $२v$ এবং $२v + १$ হয়।
তবে যদি $n$ দুইয়ের শক্তি না হয়, এই পদ্ধতিটি কিছু সূচক এড়িয়ে যাবে এবং অ্যারে `t` এর কিছু অংশ অব্যবহৃত রেখে যাবে।
মেমোরি খরচ $4n$ দ্বারা সীমিত, যদিও $n$ উপাদানের একটি অ্যারের সেগমেন্ট ট্রির জন্য শুধুমাত্র $२n - १$ ভার্টেক্স প্রয়োজন।

তবে এটি হ্রাস করা যায়।
আমরা একটি Euler ট্যুর ট্রাভার্সাল (প্রি-অর্ডার ট্রাভার্সাল) এর ক্রমে ট্রির ভার্টেক্সগুলির নাম্বার পুনর্ডিটারমিন করি, এবং আমরা এই সমস্ত ভার্টেক্সগুলি একসাথে লিখি।

সূচক $v$ তে একটি ভার্টেক্স কনসিডার করি, এবং এটি সেগমেন্ট $[l, r]$ এর জন্য দায়বদ্ধ, এবং $mid = \dfrac{l + r}{२}$।
এটি স্পষ্ট যে বাম চাইল্ড সূচক $v + १$ থাকবে।
বাম চাইল্ড সেগমেন্ট $[l, mid]$ এর জন্য দায়বদ্ধ, অর্থাৎ মোট বাম চাইল্ডের সাবট্রিতে $२ * (mid - l + १) - १$ ভার্টেক্স থাকবে।
এইভাবে আমরা $v$ এর ডান চাইল্ডের সূচক গণনা করতে পারি। সূচকটি হবে $v + २ * (mid - l + १)$।
এই নাম্বারিং দ্বারা আমরা প্রয়োজনীয় মেমোরি $२n$ এ হ্রাস অর্জন করি।

## <a name="advanced-versions-of-segment-trees"></a>সেগমেন্ট ট্রির উন্নত সংস্করণ


একটি সেগমেন্ট ট্রি একটি অত্যন্ত নমনীয় ডেটা স্ট্রাকচার, এবং অনেক বিভিন্ন দিক থেকে ভেরিয়েশন এবং এক্সটেনশন অনুমোদন করে।
আসুন নীচের তাদের শ্রেণীবদ্ধ করার চেষ্টা করি।

### আরও জটিল কোয়েরি

সেগমেন্ট ট্রিকে একটি দিকে পরিবর্তন করা বেশ সহজ হতে পারে, যাতে এটি বিভিন্ন কোয়েরি গণনা করে (উদাহরণস্বরূপ সাম না করে ন্যূনতম / সর্বাধিক গণনা করা), তবে এটিও অত্যন্ত তুচ্ছ হতে পারে।

#### সর্বাধিক খুঁজে পাওয়া

আমরা উপরে বর্ণিত সমস্যার অবস্থা সামান্য পরিবর্তন করি: যোগফল কোয়েরি করার পরিবর্তে, আমরা এখন সর্বাধিক কোয়েরি করব।

ট্রিটি উপরে বর্ণিত ট্রির সঠিক একই কাঠামো থাকবে।
আমাদের শুধুমাত্র $\text{build}$ এবং $\text{update}$ ফাংশনে $t[v]$ কীভাবে গণনা করা হয় তা পরিবর্তন করতে হবে।
$t[v]$ এখন সম্পর্কিত সেগমেন্টের সর্বাধিক সংরক্ষণ করবে।
এবং আমাদের $\text{sum}$ ফাংশনের রিটার্ন মানের গণনাও পরিবর্তন করতে হবে (সর্বাধিক দ্বারা যোগফল প্রতিস্থাপন করা)।

অবশ্যই এই সমস্যাটি সর্বাধিক না করে ন্যূনতম গণনা করার জন্য সহজেই পরিবর্তন করা যেতে পারে।

এই সমস্যার একটি ইমপ্লিমেন্টেশন দেখানোর পরিবর্তে, পরবর্তী বিভাগে এই সমস্যার একটি আরও জটিল সংস্করণের জন্য ইমপ্লিমেন্টেশন দেওয়া হবে।

#### সর্বাধিক এবং এটি যতবার প্রদর্শিত হয় তার সংখ্যা খুঁজে পাওয়া

এই কাজটি আগের একটির সাথে অনুরূপ।
সর্বাধিক খুঁজে পাওয়া ছাড়াও, আমাদের সর্বাধিকের সংখ্যাও খুঁজে পেতে হবে।

এই সমস্যা সমাধানের জন্য, আমরা ট্রিতে প্রতিটি ভার্টেক্সে একটি সংখ্যার জোড়া সংরক্ষণ করি:
সর্বাধিক ছাড়াও আমরা সম্পর্কিত সেগমেন্টে এটির সংখ্যাও সংরক্ষণ করি।
$t[v]$ তে সংরক্ষণ করার জন্য সঠিক জোড়া ডিটারমিন করা এখনও চাইল্ড ভার্টেক্সে স্টোর করা জোড়ার তথ্য ব্যবহার করে ধ্রুবক সময়ে করা যায়।
এই ধরনের দুটি জোড়া একটি আলাদা ফাংশনে একত্রিত করা উচিত, কারণ এটি এমন একটি অপারেশন যা আমরা ট্রি তৈরি করার সময়, সর্বাধিক কোয়েরিতে উত্তর দেওয়ার সময় এবং পরিবর্তন সম্পাদনের সময় করব।

```cpp
pair<int, int> t[4*MAXN];

pair<int, int> combine(pair<int, int> a, pair<int, int> b) {
    if (a.first > b.first) 
        return a;
    if (b.first > a.first)
        return b;
    return make_pair(a.first, a.second + b.second);
}

void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = make_pair(a[tl], 1);
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = combine(t[v*2], t[v*2+1]);
    }
}

pair<int, int> get_max(int v, int tl, int tr, int l, int r) {
    if (l > r)
        return make_pair(-INF, 0);
    if (l == tl && r == tr)
        return t[v];
    int tm = (tl + tr) / 2;
    return combine(get_max(v*2, tl, tm, l, min(r, tm)), 
                   get_max(v*2+1, tm+1, tr, max(l, tm+1), r));
}

void update(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        t[v] = make_pair(new_val, 1);
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
        t[v] = combine(t[v*2], t[v*2+1]);
    }
}
```
#### সর্বশ্রেষ্ঠ সাধারণ ডিভাইজর / ন্যূনতম সাধারণ গুণিতক গণনা করা

এই সমস্যায় আমরা অ্যারের দেওয়া রেঞ্জের সমস্ত সংখ্যার GCD / LCM গণনা করতে চাই।

সেগমেন্ট ট্রির এই আকর্ষণীয় ভেরিয়েশনটি ঠিক একইভাবে সমাধান করা যায় যেমনিতে আমরা সাম / ন্যূনতম / সর্বাধিক কোয়েরির জন্য সেগমেন্ট ট্রি তৈরি করেছি:
ট্রির প্রতিটি ভার্টেক্সে সম্পর্কিত ভার্টেক্সের GCD / LCM সংরক্ষণ করা যথেষ্ট।
দুটি ভার্টেক্স একত্রিত করা উভয় ভার্টেক্সের GCD / LCM গণনা করে করা যেতে পারে।

#### শূন্যের সংখ্যা গণনা করা, $k$-তম শূন্য সার্চ করা { #counting-zero-search-kth data-toc-label="শূন্যের সংখ্যা গণনা করা, k-তম শূন্য সার্চ করা"}

এই সমস্যায় আমরা একটা দেওয়া রেঞ্জে শূন্যের সংখ্যা খুঁজে পেতে চাই, এবং অতিরিক্তভাবে একটি দ্বিতীয় ফাংশন ব্যবহার করে $k$-তম শূন্যের সূচক খুঁজে পেতে চাই।

আবার আমাদের ট্রির স্টোর করা মানগুলি কিছুটা পরিবর্তন করতে হবে:
এবার আমরা $t[]$ তে প্রতিটি সেগমেন্টে শূন্যের সংখ্যা সংরক্ষণ করব।
এটি পরিষ্কার যে $\text{build}$, $\text{update}$ এবং $\text{count\_zeros}$ ফাংশন কীভাবে প্রয়োগ করতে হয়, আমরা সরলভাবে সাম কোয়েরি সমস্যা থেকে ধারণা ব্যবহার করতে পারি।
এইভাবে আমরা সমস্যার প্রথম অংশ সমাধান করেছি।

এখন আমরা অ্যারে $a[]$ তে $k$-তম শূন্য খুঁজে পাওয়ার সমস্যা সমাধান করতে শিখি।
এই কাজ করার জন্য, আমরা সেগমেন্ট ট্রি নেমে আসব, রুট ভার্টেক্স থেকে শুরু করে, এবং প্রতিবার বাম বা ডান চাইল্ডে যাই, কোন সেগমেন্টে $k$-তম শূন্য আছে তার উপর নির্ভর করে।
কোন চাইল্ডে যেতে হবে তা সিদ্ধান্ত নিতে, বাম ভার্টেক্সের সাথে সম্পর্কিত সেগমেন্টে প্রদর্শিত শূন্যের সংখ্যা দেখা যথেষ্ট।
যদি এই পূর্বনির্ধারিত গণনা $k$ এর চেয়ে বড় বা সমান হয়, তবে বাম চাইল্ডে নেমে যাওয়া প্রয়োজন, অন্যথায় ডান চাইল্ডে নেমে যান।
লক্ষ্য করুন, যদি আমরা ডান চাইল্ড বেছে নিই, আমাদের $k$ থেকে বাম চাইল্ডের শূন্যের সংখ্যা বিয়োগ করতে হবে।

ইমপ্লিমেন্টেশনে আমরা বিশেষ ক্ষেত্র হ্যান্ডল করতে পারি, $a[]$ -১ ফেরত দিয়ে $k$ এর চেয়ে কম শূন্য থাকলে।

```cpp
int find_kth(int v, int tl, int tr, int k) {
    if (k > t[v])
        return -1;
    if (tl == tr)
        return tl;
    int tm = (tl + tr) / 2;
    if (t[v*2] >= k)
        return find_kth(v*2, tl, tm, k);
    else 
        return find_kth(v*2+1, tm+1, tr, k - t[v*2]);
}
```

#### দেওয়া পরিমাণ সহ অ্যারে প্রিফিক্স সার্চ করা

কাজটি নিম্নরূপ:
একটা দেওয়া মান $x$ এর জন্য আমাদের দ্রুত সবচেয়ে ছোট সূচক $i$ খুঁজে পেতে হবে যাতে অ্যারে $a[]$ এর প্রথম $i$ উপাদানের যোগফল $x$ এর চেয়ে বড় বা সমান হয় (ধরে নিয়ে যে অ্যারে $a[]$ শুধুমাত্র অ-নেতিবাচক মান ধারণ করে)।

এই কাজটি সেগমেন্ট ট্রির সাথে প্রিফিক্সের যোগফল গণনা করে বাইনারি সার্চ ব্যবহার করে সমাধান করা যায়।
তবে এটি $O(\log^2 n)$ সমাধানে নিয়ে যাবে।

পরিবর্তে আমরা আগের বিভাগের একই ধারণা ব্যবহার করতে পারি, এবং ট্রি নেমে আসার মাধ্যমে অবস্থান খুঁজে পেতে পারি:
বাম চাইল্ডের যোগফলের উপর নির্ভর করে প্রতিবার বাম বা ডানে যাই।
এইভাবে $O(\log n)$ সময়ে উত্তর খুঁজে পাই।

#### একটা দেওয়া পরিমাণের চেয়ে বড় প্রথম উপাদান সার্চ করা

কাজটি নিম্নরূপ:
একটা দেওয়া মান $x$ এবং রেঞ্জ $a[l \dots r]$ এর জন্য রেঞ্জ $a[l \dots r]$ তে সবচেয়ে ছোট $i$ খুঁজে পাই, যাতে $a[i]$ $x$ এর চেয়ে বড় হয়।

এই কাজটি সেগমেন্ট ট্রির সাথে সর্বাধিক প্রিফিক্স কোয়েরির উপর বাইনারি সার্চ ব্যবহার করে সমাধান করা যায়।
তবে, এটি $O(\log^2 n)$ সমাধানে নিয়ে যাবে।

পরিবর্তে, আমরা আগের বিভাগের একই ধারণা ব্যবহার করতে পারি, এবং ট্রি নেমে আসার মাধ্যমে অবস্থান খুঁজে পেতে পারি:
বাম চাইল্ডের সর্বাধিক মানের উপর নির্ভর করে প্রতিবার বাম বা ডানে যাই।
এইভাবে $O(\log n)$ সময়ে উত্তর খুঁজে পাই। 

```cpp
int get_first(int v, int tl, int tr, int l, int r, int x) {
    if(tl > r || tr < l) return -1;
    if(t[v] <= x) return -1;
    
    if (tl== tr) return tl;
    
    int tm = tl + (tr-tl)/2;
    int left = get_first(2*v, tl, tm, l, r, x);
    if(left != -1) return left;
    return get_first(2*v+1, tm+1, tr, l ,r, x);
}
```

#### সর্বাধিক যোগফল সহ সাবসেগমেন্ট খুঁজে পাওয়া

এখানে আবার প্রতিটি কোয়েরির জন্য একটি রেঞ্জ $a[l \dots r]$ পাই, এবার আমাদের একটি সাবসেগমেন্ট $a[l^\prime \dots r^\prime]$ খুঁজে পেতে হবে যাতে $l \le l^\prime$ এবং $r^\prime \le r$ এবং এই সেগমেন্টের উপাদানগুলির যোগফল সর্বাধিক হয়।
আগে যেমন আমরা অ্যারের স্বতন্ত্র উপাদান পরিবর্তন করতে চাই।
অ্যারের উপাদানগুলি ঋণাত্মক হতে পারে, এবং সর্বোত্তম সাবসেগমেন্ট খালি হতে পারে (উদাহরণস্বরূপ যদি সমস্ত উপাদান ঋণাত্মক হয়)।

এই সমস্যাটি সেগমেন্ট ট্রির একটি অ-তুচ্ছ ব্যবহার।
এবার আমরা প্রতিটি ভার্টেক্সের জন্য চারটি মান সংরক্ষণ করব:
সেগমেন্টের যোগফল, সর্বাধিক প্রিফিক্স যোগফল, সর্বাধিক সাফিক্স যোগফল, এবং এটিতে সর্বাধিক সাবসেগমেন্টের যোগফল।
অন্য কথায় সেগমেন্ট ট্রির প্রতিটি সেগমেন্টের জন্য উত্তর ইতিমধ্যে পূর্বনির্ধারিত যেমন সেগমেন্টের বাম এবং ডান সীমানা স্পর্শকারী সেগমেন্টের উত্তরগুলি।

এই ধরনের ডেটা সহ একটি ট্রি তৈরি করতে কীভাবে?
আবার আমরা এটি একটি রিকার্সিভ উপায়ে গণনা করি:
আমরা প্রথমে বাম এবং ডান চাইল্ডের জন্য সমস্ত চারটি মান গণনা করি, এবং তারপর বর্তমান ভার্টেক্সের চারটি মান সংরক্ষণ করতে সেগুলি একত্রিত করি।
বর্তমান ভার্টেক্সের উত্তর নিম্নোক্তগুলির মধ্যে যেকোনো একটি:

 * বাম চাইল্ডের উত্তর, যার অর্থ সর্বোত্তম সাবসেগমেন্ট সম্পূর্ণভাবে বাম চাইল্ডের সেগমেন্টে রাখা
 * ডান চাইল্ডের উত্তর, যার অর্থ সর্বোত্তম সাবসেগমেন্ট সম্পূর্ণভাবে ডান চাইল্ডের সেগমেন্টে রাখা
 * বাম চাইল্ডের সর্বাধিক সাফিক্স যোগফল এবং ডান চাইল্ডের সর্বাধিক প্রিফিক্স যোগফলের যোগফল, যার অর্থ সর্বোত্তম সাবসেগমেন্ট উভয় চাইল্ডের সাথে ছেদ করে।

সুতরাং বর্তমান ভার্টেক্সের উত্তর এই তিনটি মানের সর্বাধিক।
সর্বাধিক প্রিফিক্স / সাফিক্স যোগফল গণনা আরও সহজ।
এখানে $\text{merge}$ ফাংশনের ইমপ্লিমেন্টেশন রয়েছে, যা শুধুমাত্র বাম এবং ডান চাইল্ড থেকে ডেটা পায়, এবং বর্তমান ভার্টেক্সের ডেটা রিটার্ন করে।

```cpp
struct data {
    int sum, pref, suff, ans;
};

data combine(data l, data r) {
    data res;
    res.sum = l.sum + r.sum;
    res.pref = max(l.pref, l.sum + r.pref);
    res.suff = max(r.suff, r.sum + l.suff);
    res.ans = max(max(l.ans, r.ans), l.suff + r.pref);
    return res;
}
```

$\text{merge}$ ফাংশন ব্যবহার করে সেগমেন্ট ট্রি তৈরি করা সহজ।
আমরা এটি আগের ইমপ্লিমেন্টেশনের মতোই প্রয়োগ করতে পারি।
লিফ ভার্টেক্স শুরু করতে, আমরা অতিরিক্তভাবে সহায়ক ফাংশন $\text{make\_data}$ তৈরি করি, যা একটি একক মান সম্পর্কিত তথ্য ধারণ করে এমন একটি $\text{data}$ অবজেক্ট রিটার্ন করবে।

```cpp
data make_data(int val) {
    data res;
    res.sum = val;
    res.pref = res.suff = res.ans = max(0, val);
    return res;
}

void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = make_data(a[tl]);
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = combine(t[v*2], t[v*2+1]);
    }
}
 
void update(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        t[v] = make_data(new_val);
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
        t[v] = combine(t[v*2], t[v*2+1]);
    }
}
```

কোয়েরির উত্তর কিভাবে গণনা করতে হয় তা অবশেষ।
এর উত্তর দিতে, আমরা আগের মতো ট্রি নেমে যাই, কোয়েরিকে বেশ কয়েকটি সাবসেগমেন্টে বিভক্ত করি যা সেগমেন্ট ট্রির সেগমেন্টের সাথে মিল খায়, এবং তাদের উত্তরগুলি একটি একক উত্তরে একত্রিত করি কোয়েরির জন্য।
তারপর এটি স্পষ্ট হওয়া উচিত যে কাজটি সাধারণ সেগমেন্ট ট্রির মতোই, তবে মানগুলি যোগ করা / ন্যূনতম / সর্বাধিক করার পরিবর্তে, আমরা $\text{merge}$ ফাংশন ব্যবহার করি।

```cpp
data query(int v, int tl, int tr, int l, int r) {
    if (l > r) 
        return make_data(0);
    if (l == tl && r == tr) 
        return t[v];
    int tm = (tl + tr) / 2;
    return combine(query(v*2, tl, tm, l, min(r, tm)), 
                   query(v*2+1, tm+1, tr, max(l, tm+1), r));
}
```

### <a name="saving-the-entire-subarrays-in-each-vertex"></a>প্রতিটি ভার্টেক্সে সম্পূর্ণ সাবঅ্যারে সংরক্ষণ করা

এটি একটি আলাদা সাবসেকশন যা অন্যদের থেকে আলাদা হয়ে দাঁড়িয়ে আছে, কারণ সেগমেন্ট ট্রির প্রতিটি ভার্টেক্সে আমরা সম্পর্কিত সেগমেন্ট সম্পর্কিত তথ্য সংক্ষিপ্ত ফর্মে (যোগফল, ন্যূনতম, সর্বাধিক, ...) সংরক্ষণ করি না, বরং সেগমেন্টের সমস্ত উপাদান সংরক্ষণ করি।
এইভাবে সেগমেন্ট ট্রির মূল অ্যারের সমস্ত উপাদান সংরক্ষণ করবে, বাম চাইল্ড ভার্টেক্স অ্যারের প্রথম অর্ধ সংরক্ষণ করবে, ডান ভার্টেক্স দ্বিতীয় অর্ধ, এবং এভাবে চলে।

এই প্রযুক্তির সবচেয়ে সাধারণ প্রয়োগে আমরা উপাদানগুলি সাজানো ক্রমে সংরক্ষণ করি।
আরও জটিল সংস্করণে উপাদানগুলি তালিকায় স্টোর করা হয় না, বরং আরও উন্নত ডেটা স্ট্রাকচার (সেট, ম্যাপ, ...)।
তবে এই সমস্ত পদ্ধতির সাধারণ ফ্যাক্টর রয়েছে যে প্রতিটি ভার্টেক্স রৈখিক মেমোরি প্রয়োজন (অর্থাৎ সম্পর্কিত সেগমেন্টের দৈর্ঘ্যের সাথে সমানুপাতিক)।

এই সেগমেন্ট ট্রি কনসিডারর সময় প্রথম প্রাকৃতিক প্রশ্ন হল মেমোরি খরচ সম্পর্কে।
স্বজ্ঞাতভাবে এটি $O(n^२)$ মেমোরির মতো দেখতে পারে, তবে দেখা যায় যে সম্পূর্ণ ট্রি শুধুমাত্র $O(n \log n)$ মেমোরির প্রয়োজন।
কেন এটি এমন?
অত্যন্ত সহজভাবে, কারণ অ্যারের প্রতিটি উপাদান $O(\log n)$ সেগমেন্টে পড়ে (মনে রাখবেন ট্রির উচ্চতা $O(\log n)$)।

তাই এই ধরনের সেগমেন্ট ট্রির স্পষ্ট বিলাসিতা সত্ত্বেও, এটি সাধারণ সেগমেন্ট ট্রির চেয়ে সামান্য বেশি মেমোরি ব্যবহার করে।

এই ডেটা স্ট্রাকচারের বেশ কয়েকটি সাধারণ অ্যাপ্লিকেশন নিচে বর্ণিত।
এই সেগমেন্ট ট্রিগুলির २D ডেটা স্ট্রাকচারের সাথে সাদৃশ্য লক্ষ্য করা মূল্যবান (আসলে এটি একটি २D ডেটা স্ট্রাকচার, তবে বরং সীমিত ক্ষমতা সহ)।

#### নির্দিষ্ট সংখ্যার চেয়ে বড় বা সমান ক্ষুদ্রতম সংখ্যা খুঁজুন। কোনো পরিবর্তন কোয়েরি নেই।

আমরা নিম্নোক্ত ফর্মের কোয়েরির উত্তর দিতে চাই:
তিনটি দেওয়া সংখ্যার জন্য $(l, r, x)$ আমাদের সেগমেন্ট $a[l \dots r]$ তে ন্যূনতম সংখ্যা খুঁজে পেতে হবে যা $x$ এর চেয়ে বড় বা সমান।

আমরা একটি সেগমেন্ট ট्रি তৈরি করি।
প্রতিটি ভার্টেক্সে আমরা সম্পর্কিত সেগমেন্টে ঘটে এমন সমস্ত সংখ্যার একটি সাজানো তালিকা সংরক্ষণ করি, উপরে বর্ণিত হিসাবে।
এই ধরনের সেগমেন্ট ট्रি যতটা সম্ভব কার্যকরভাবে তৈরি করতে কীভাবে?
সর্বদার মতো আমরা এই সমস্যাটি রিকার্সিভভাবে পদ্ধতি করি: বাম এবং ডান চাইল্ডের তালিকাগুলি ইতিমধ্যে নির্মিত, এবং আমরা বর্তমান ভার্টেক্সের জন্য তালিকা তৈরি করতে চাই।
এই দৃষ্টিকোণ থেকে অপারেশন এখন তুচ্ছ এবং রৈখিক সময়ে সম্পাদিত হতে পারে:
আমাদের শুধুমাত্র দুটি সাজানো তালিকা একটিতে একত্রিত করতে হবে, যা দুটি পয়েন্টার ব্যবহার করে তাদের উপর পুনরাবৃত্তি করে করা যায়।
C++ STL ইতিমধ্যে এই অ্যালগরিদমের একটি ইমপ্লিমেন্টেশন রয়েছে।

সেগমেন্ট ট्রির এই কাঠামো এবং মার্জ সর্ট অ্যালগরিদমের সাথে সাদৃশ্যের কারণে, ডেটা স্ট্রাকচারকে প্রায়ই "মার্জ সর্ট ট्রি" বলা হয়।

```cpp
vector<int> t[4*MAXN];

void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = vector<int>(1, a[tl]);
    } else { 
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        merge(t[v*2].begin(), t[v*2].end(), t[v*2+1].begin(), t[v*2+1].end(),
              back_inserter(t[v]));
    }
}
```

আমরা ইতিমধ্যে জানি যে এইভাবে নির্মিত সেগমেন্ট ট्রি $O(n \log n)$ মেমোরির প্রয়োজন।
এবং এই ইমপ্লিমেন্টেশনের জন্য ধন্যবাদ এর নির্মাণও $O(n \log n)$ সময় নেয়, সর্বশেষ প্রতিটি তালিকা এর আকারের সাপেক্ষে রৈখিক সময়ে নির্মিত হয়।

এখন কোয়েরির উত্তর কনসিডার করুন।
আমরা ট্রি নেমে যাব, সাধারণ সেগমেন্ট ট्রির মতো, আমাদের সেগমেন্ট $a[l \dots r]$ কে বেশ কয়েকটি সাবসেগমেন্টে বিভক্ত করি (সর্বাধিক $O(\log n)$ টুকরায়)।
এটি স্পষ্ট যে সম্পূর্ণ উত্তর প্রতিটি সাবকোয়েরির ন্যূনতম।
তাই এখন আমাদের শুধুমাত্র বুঝতে হবে, ট্রির কিছু ভার্টেক্সের সাথে সামঞ্জস্যপূর্ণ এই ধরনের একটি সাবসেগমেন্টে কোয়েরির উত্তর কীভাবে দেওয়া যায়।

আমরা সেগমেন্ট ট्রির কোনো ভার্টেক্সে রয়েছি এবং কোয়েরির উত্তর গণনা করতে চাই, অর্থাৎ একটা দেওয়া সংখ্যা $x$ এর চেয়ে বড় বা সমান ন্যূনতম সংখ্যা খুঁজুন।
যেহেতু ভার্টেক্সে উপাদানের তালিকা সাজানো ক্রমে রয়েছে, আমরা সহজভাবে এই তালিকায় একটি বাইনারি সার্চ সম্পাদন করতে এবং $x$ এর চেয়ে বড় বা সমান প্রথম সংখ্যা রিটার্ন করতে পারি।

এইভাবে ট্রির একটি সেগমেন্টে কোয়েরির উত্তর $O(\log n)$ সময় নেয়, এবং সম্পূর্ণ কোয়েরি $O(\log^२ n)$ এ প্রক্রিয়া করা হয়।

```cpp
int query(int v, int tl, int tr, int l, int r, int x) {
    if (l > r)
        return INF;
    if (l == tl && r == tr) {
        vector<int>::iterator pos = lower_bound(t[v].begin(), t[v].end(), x);
        if (pos != t[v].end())
            return *pos;
        return INF;
    }
    int tm = (tl + tr) / 2;
    return min(query(v*2, tl, tm, l, min(r, tm), x), 
               query(v*2+1, tm+1, tr, max(l, tm+1), r, x));
}
```

ধ্রুবক $\text{INF}$ অ্যারেতে সমস্ত সংখ্যার চেয়ে বড় কিছু বড় সংখ্যার সমান।
এর ব্যবহার মানে সেগমেন্টে $x$ এর চেয়ে বড় বা সমান কোনো সংখ্যা নেই।
এটির অর্থ "দেওয়া ইন্টারভালে কোনো উত্তর নেই"।

#### Find the smallest number greater or equal to a specified number. With modification queries.

This task is similar to the previous.
The last approach has a disadvantage, it was not possible to modify the array between answering queries.
Now we want to do exactly this: a modification query will do the assignment $a[i] = y$.

The solution is similar to the solution of the previous problem, but instead of lists at each vertex of the Segment Tree, we will store a balanced list that allows you to quickly search for numbers, delete numbers, and insert new numbers. 
Since the array can contain a number repeated, the optimal choice is the data structure $\text{multiset}$. 

The construction of such a Segment Tree is done in pretty much the same way as in the previous problem, only now we need to combine $\text{multiset}$s and not sorted lists.
This leads to a construction time of $O(n \log^2 n)$ (in general merging two red-black trees can be done in linear time, but the C++ STL doesn't guarantee this time complexity).

The $\text{query}$ function is also almost equivalent, only now the $\text{lower_bound}$ function of the $\text{multiset}$ function should be called instead ($\text{std::lower_bound}$ only works in $O(\log n)$ time if used with random-access iterators).

Finally the modification request. 
To process it, we must go down the tree, and modify all $\text{multiset}$ from the corresponding segments that contain the affected element.
We simply delete the old value of this element (but only one occurrence), and insert the new value.

```cpp
void update(int v, int tl, int tr, int pos, int new_val) {
    t[v].erase(t[v].find(a[pos]));
    t[v].insert(new_val);
    if (tl != tr) {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
    } else {
        a[pos] = new_val;
    }
}
```

Processing of this modification query also takes $O(\log^2 n)$ time.

#### Find the smallest number greater or equal to a specified number. Acceleration with "fractional cascading".

We have the same problem statement, we want to find the minimal number greater than or equal to $x$ in a segment, but this time in $O(\log n)$ time.
We will improve the time complexity using the technique "fractional cascading".

Fractional cascading is a simple technique that allows you to improve the running time of multiple binary searches, which are conducted at the same time. 
Our previous approach to the search query was, that we divide the task into several subtasks, each of which is solved with a binary search. 
Fractional cascading allows you to replace all of these binary searches with a single one.

The simplest and most obvious example of fractional cascading is the following problem:
there are $k$ sorted lists of numbers, and we must find in each list the first number greater than or equal to the given number.

Instead of performing a binary search for each list, we could merge all lists into one big sorted list.
Additionally for each element $y$ we store a list of results of searching for $y$ in each of the $k$ lists.
Therefore if we want to find the smallest number greater than or equal to $x$, we just need to perform one single binary search, and from the list of indices we can determine the smallest number in each list.
This approach however requires $O(n \cdot k)$ ($n$ is the length of the combined lists), which can be quite inefficient. 

Fractional cascading reduces this memory complexity to $O(n)$ memory, by creating from the $k$ input lists $k$ new lists, in which each list contains the corresponding list and additionally also every second element of the following new list.
Using this structure it is only necessary to store two indices, the index of the element in the original list, and the index of the element in the following new list.
So this approach only uses $O(n)$ memory, and still can answer the queries using a single binary search. 

But for our application we do not need the full power of fractional cascading.
In our Segment Tree a vertex will contain the sorted list of all elements that occur in either the left or the right subtrees (like in the Merge Sort Tree). 
Additionally to this sorted list, we store two positions for each element.
For an element $y$ we store the smallest index $i$, such that the $i$th element in the sorted list of the left child is greater or equal to $y$.
And we store the smallest index $j$, such that the $j$th element in the sorted list of the right child is greater or equal to $y$.
These values can be computed in parallel to the merging step when we build the tree.

How does this speed up the queries?

Remember, in the normal solution we did a binary search in every node.
But with this modification, we can avoid all except one.

To answer a query, we simply do a binary search in the root node.
This gives us the smallest element $y \ge x$ in the complete array, but it also gives us two positions.
The index of the smallest element greater or equal $x$ in the left subtree, and the index of the smallest element $y$ in the right subtree. Notice that $\ge y$ is the same as $\ge x$, since our array doesn't contain any elements between $x$ and $y$.
In the normal Merge Sort Tree solution we would compute these indices via binary search, but with the help of the precomputed values we can just look them up in $O(1)$.
And we can repeat that until we visited all nodes that cover our query interval.

To summarize, as usual we touch $O(\log n)$ nodes during a query. In the root node we do a binary search, and in all other nodes we only do constant work.
This means the complexity for answering a query is $O(\log n)$.

But notice, that this uses three times more memory than a normal Merge Sort Tree, which already uses a lot of memory ($O(n \log n)$).

It is straightforward to apply this technique to a problem, that doesn't require any modification queries.
The two positions are just integers and can easily be computed by counting when merging the two sorted sequences.

It is still possible to also allow modification queries, but that complicates the entire code.
Instead of integers, you need to store the sorted array as `multiset`, and instead of indices you need to store iterators.
And you need to work very carefully, so that you increment or decrement the correct iterators during a modification query.

#### Other possible variations

This technique implies a whole new class of possible applications. 
Instead of storing a $\text{vector}$ or a $\text{multiset}$ in each vertex, other data structures can be used:
other Segment Trees (somewhat discussed in [Generalization to higher dimensions](segment_tree.md#generalization-to-higher-dimensions)), Fenwick Trees, Cartesian trees, etc.

### Range updates (Lazy Propagation)

All problems in the above sections discussed modification queries that only affected a single element of the array each.
However the Segment Tree allows applying modification queries to an entire segment of contiguous elements, and perform the query in the same time $O(\log n)$. 

#### Addition on segments

We begin by considering problems of the simplest form: the modification query should add a number $x$ to all numbers in the segment $a[l \dots r]$.
The second query, that we are supposed to answer, asked simply for the value of $a[i]$.

To make the addition query efficient, we store at each vertex in the Segment Tree how many we should add to all numbers in the corresponding segment. 
For example, if the query "add 3 to the whole array $a[0 \dots n-1]$" comes, then we place the number 3 in the root of the tree.
In general we have to place this number to multiple segments, which form a partition of the query segment. 
Thus we don't have to change all $O(n)$ values, but only $O(\log n)$ many.

If now there comes a query that asks the current value of a particular array entry, it is enough to go down the tree and add up all values found along the way.

```cpp
void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = 0;
    }
}

void update(int v, int tl, int tr, int l, int r, int add) {
    if (l > r)
        return;
    if (l == tl && r == tr) {
        t[v] += add;
    } else {
        int tm = (tl + tr) / 2;
        update(v*2, tl, tm, l, min(r, tm), add);
        update(v*2+1, tm+1, tr, max(l, tm+1), r, add);
    }
}

int get(int v, int tl, int tr, int pos) {
    if (tl == tr)
        return t[v];
    int tm = (tl + tr) / 2;
    if (pos <= tm)
        return t[v] + get(v*2, tl, tm, pos);
    else
        return t[v] + get(v*2+1, tm+1, tr, pos);
}
```

#### Assignment on segments

Suppose now that the modification query asks to assign each element of a certain segment $a[l \dots r]$ to some value $p$.
As a second query we will again consider reading the value of the array $a[i]$.

To perform this modification query on a whole segment, you have to store at each vertex of the Segment Tree whether the corresponding segment is covered entirely with the same value or not.
This allows us to make a "lazy" update: 
instead of changing all segments in the tree that cover the query segment, we only change some, and leave others unchanged.
A marked vertex will mean, that every element of the corresponding segment is assigned to that value, and actually also the complete subtree should only contain this value.
In a sense we are lazy and delay writing the new value to all those vertices.
We can do this tedious task later, if this is necessary.

So after the modification query is executed, some parts of the tree become irrelevant - some modifications remain unfulfilled in it.

For example if a modification query "assign a number to the whole array $a[0 \dots n-1]$" gets executed, in the Segment Tree only a single change is made - the number is placed in the root of the tree and this vertex gets marked.
The remaining segments remain unchanged, although in fact the number should be placed in the whole tree.

Suppose now that the second modification query says, that the first half of the array $a[0 \dots n/2]$ should be assigned with some other number. 
To process this query we must assign each element in the whole left child of the root vertex with that number. 
But before we do this, we must first sort out the root vertex first. 
The subtlety here is that the right half of the array should still be assigned to the value of the first query, and at the moment there is no information for the right half stored.

The way to solve this is to push the information of the root to its children, i.e. if the root of the tree was assigned with any number, then we assign the left and the right child vertices with this number and remove the mark of the root.
After that, we can assign the left child with the new value, without losing any necessary information.

Summarizing we get:
for any queries (a modification or reading query) during the descent along the tree we should always push information from the current vertex into both of its children. 
We can understand this in such a way, that when we descent the tree we apply delayed modifications, but exactly as much as necessary (so not to degrade the complexity of $O(\log n)$). 

For the implementation we need to make a $\text{push}$ function, which will receive the current vertex, and it will push the information for its vertex to both its children. 
We will call this function at the beginning of the query functions (but we will not call it from the leaves, because there is no need to push information from them any further).

```cpp
void push(int v) {
    if (marked[v]) {
        t[v*2] = t[v*2+1] = t[v];
        marked[v*2] = marked[v*2+1] = true;
        marked[v] = false;
    }
}

void update(int v, int tl, int tr, int l, int r, int new_val) {
    if (l > r) 
        return;
    if (l == tl && tr == r) {
        t[v] = new_val;
        marked[v] = true;
    } else {
        push(v);
        int tm = (tl + tr) / 2;
        update(v*2, tl, tm, l, min(r, tm), new_val);
        update(v*2+1, tm+1, tr, max(l, tm+1), r, new_val);
    }
}

int get(int v, int tl, int tr, int pos) {
    if (tl == tr) {
        return t[v];
    }
    push(v);
    int tm = (tl + tr) / 2;
    if (pos <= tm) 
        return get(v*2, tl, tm, pos);
    else
        return get(v*2+1, tm+1, tr, pos);
}
```

Notice: the function $\text{get}$ can also be implemented in a different way: 
do not make delayed updates, but immediately return the value $t[v]$ if $marked[v]$ is true.

#### Adding on segments, querying for maximum

Now the modification query is to add a number to all elements in a range, and the reading query is to find the maximum in a range.

So for each vertex of the Segment Tree we have to store the maximum of the corresponding subsegment. 
The interesting part is how to recompute these values during a modification request.

For this purpose we keep store an additional value for each vertex. 
In this value we store the addends we haven't propagated to the child vertices.
Before traversing to a child vertex, we call $\text{push}$ and propagate the value to both children.
We have to do this in both the $\text{update}$ function and the $\text{query}$ function.

```cpp
void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = max(t[v*2], t[v*2 + 1]);
    }
}

void push(int v) {
    t[v*2] += lazy[v];
    lazy[v*2] += lazy[v];
    t[v*2+1] += lazy[v];
    lazy[v*2+1] += lazy[v];
    lazy[v] = 0;
}

void update(int v, int tl, int tr, int l, int r, int addend) {
    if (l > r) 
        return;
    if (l == tl && tr == r) {
        t[v] += addend;
        lazy[v] += addend;
    } else {
        push(v);
        int tm = (tl + tr) / 2;
        update(v*2, tl, tm, l, min(r, tm), addend);
        update(v*2+1, tm+1, tr, max(l, tm+1), r, addend);
        t[v] = max(t[v*2], t[v*2+1]);
    }
}

int query(int v, int tl, int tr, int l, int r) {
    if (l > r)
        return -INF;
    if (l == tl && tr == r)
        return t[v];
    push(v);
    int tm = (tl + tr) / 2;
    return max(query(v*2, tl, tm, l, min(r, tm)), 
               query(v*2+1, tm+1, tr, max(l, tm+1), r));
}
```

### <a name="generalization-to-higher-dimensions"></a>Generalization to higher dimensions

A Segment Tree can be generalized quite natural to higher dimensions.
If in the one-dimensional case we split the indices of the array into segments, then in the two-dimensional we make an ordinary Segment Tree with respect to the first indices, and for each segment we build an ordinary Segment Tree with respect to the second indices.

#### Simple 2D Segment Tree

A matrix $a[0 \dots n-1, 0 \dots m-1]$ is given, and we have to find the sum (or minimum/maximum) on some submatrix $a[x_1 \dots x_2, y_1 \dots y_2]$, as well as perform modifications of individual matrix elements (i.e. queries of the form $a[x][y] = p$).

So we build a 2D Segment Tree: first the Segment Tree using the first coordinate ($x$), then the second ($y$).

To make the construction process more understandable, you can forget for a while that the matrix is two-dimensional, and only leave the first coordinate.
We will construct an ordinary one-dimensional Segment Tree using only the first coordinate.
But instead of storing a number in a segment, we store an entire Segment Tree: 
i.e. at this moment we remember that we also have a second coordinate; but because at this moment the first coordinate is already fixed to some interval $[l \dots r]$, we actually work with such a strip $a[l \dots r, 0 \dots m-1]$ and for it we build a Segment Tree.

Here is the implementation of the construction of a 2D Segment Tree.
It actually represents two separate blocks: 
the construction of a Segment Tree along the $x$ coordinate ($\text{build}_x$), and the $y$ coordinate ($\text{build}_y$).
For the leaf nodes in $\text{build}_y$ we have to separate two cases: 
when the current segment of the first coordinate $[tlx \dots trx]$ has length 1, and when it has a length greater than one. In the first case, we just take the corresponding value from the matrix, and in the second case we can combine the values of two Segment Trees from the left and the right son in the coordinate $x$.

```cpp
void build_y(int vx, int lx, int rx, int vy, int ly, int ry) {
    if (ly == ry) {
        if (lx == rx)
            t[vx][vy] = a[lx][ly];
        else
            t[vx][vy] = t[vx*2][vy] + t[vx*2+1][vy];
    } else {
        int my = (ly + ry) / 2;
        build_y(vx, lx, rx, vy*2, ly, my);
        build_y(vx, lx, rx, vy*2+1, my+1, ry);
        t[vx][vy] = t[vx][vy*2] + t[vx][vy*2+1];
    }
}

void build_x(int vx, int lx, int rx) {
    if (lx != rx) {
        int mx = (lx + rx) / 2;
        build_x(vx*2, lx, mx);
        build_x(vx*2+1, mx+1, rx);
    }
    build_y(vx, lx, rx, 1, 0, m-1);
}
```

Such a Segment Tree still uses a linear amount of memory, but with a larger constant: $16 n m$.
It is clear that the described procedure $\text{build}_x$ also works in linear time. 

Now we turn to processing of queries. We will answer to the two-dimensional query using the same principle: 
first break the query on the first coordinate, and then for every reached vertex, we call the corresponding Segment Tree of the second coordinate.

```cpp
int sum_y(int vx, int vy, int tly, int try_, int ly, int ry) {
    if (ly > ry) 
        return 0;
    if (ly == tly && try_ == ry)
        return t[vx][vy];
    int tmy = (tly + try_) / 2;
    return sum_y(vx, vy*2, tly, tmy, ly, min(ry, tmy))
         + sum_y(vx, vy*2+1, tmy+1, try_, max(ly, tmy+1), ry);
}

int sum_x(int vx, int tlx, int trx, int lx, int rx, int ly, int ry) {
    if (lx > rx)
        return 0;
    if (lx == tlx && trx == rx)
        return sum_y(vx, 1, 0, m-1, ly, ry);
    int tmx = (tlx + trx) / 2;
    return sum_x(vx*2, tlx, tmx, lx, min(rx, tmx), ly, ry)
         + sum_x(vx*2+1, tmx+1, trx, max(lx, tmx+1), rx, ly, ry);
}
```

This function works in $O(\log n \log m)$ time, since it first descends the tree in the first coordinate, and for each traversed vertex in the tree it makes a query in the corresponding Segment Tree along the second coordinate.

Finally we consider the modification query. 
We want to learn how to modify the Segment Tree in accordance with the change in the value of some element $a[x][y] = p$.
It is clear, that the changes will occur only in those vertices of the first Segment Tree that cover the coordinate $x$ (and such will be $O(\log n)$), and for Segment Trees corresponding to them the changes will only occurs at those vertices that covers the coordinate $y$ (and such will be $O(\log m)$).
Therefore the implementation will be not very different form the one-dimensional case, only now we first descend the first coordinate, and then the second.

```cpp
void update_y(int vx, int lx, int rx, int vy, int ly, int ry, int x, int y, int new_val) {
    if (ly == ry) {
        if (lx == rx)
            t[vx][vy] = new_val;
        else
            t[vx][vy] = t[vx*2][vy] + t[vx*2+1][vy];
    } else {
        int my = (ly + ry) / 2;
        if (y <= my)
            update_y(vx, lx, rx, vy*2, ly, my, x, y, new_val);
        else
            update_y(vx, lx, rx, vy*2+1, my+1, ry, x, y, new_val);
        t[vx][vy] = t[vx][vy*2] + t[vx][vy*2+1];
    }
}

void update_x(int vx, int lx, int rx, int x, int y, int new_val) {
    if (lx != rx) {
        int mx = (lx + rx) / 2;
        if (x <= mx)
            update_x(vx*2, lx, mx, x, y, new_val);
        else
            update_x(vx*2+1, mx+1, rx, x, y, new_val);
    }
    update_y(vx, lx, rx, 1, 0, m-1, x, y, new_val);
}
```

#### Compression of 2D Segment Tree

Let the problem be the following: there are $n$ points on the plane given by their coordinates $(x_i, y_i)$ and queries of the form "count the number of points lying in the rectangle $((x_1, y_1), (x_2, y_2))$".
It is clear that in the case of such a problem it becomes unreasonably wasteful to construct a two-dimensional Segment Tree with $O(n^2)$ elements.
Most on this memory will be wasted, since each single point can only get into $O(\log n)$ segments of the tree along the first coordinate, and therefore the total "useful" size of all tree segments on the second coordinate is $O(n \log n)$.

So we proceed as follows:
at each vertex of the Segment Tree with respect to the first coordinate we store a Segment Tree constructed only by those second coordinates that occur in the current segment of the first coordinates. 
In other words, when constructing a Segment Tree inside some vertex with index $vx$ and the boundaries $tlx$ and $trx$, we only consider those points that fall into this interval $x \in [tlx, trx]$, and build a Segment Tree just using them.

Thus we will achieve that each Segment Tree on the second coordinate will occupy exactly as much memory as it should.
As a result, the total amount of memory will decrease to $O(n \log n)$.
We still can answer the queries in $O(\log^2 n)$ time, we just have to make a binary search on the second coordinate, but this will not worsen the complexity.

But modification queries will be impossible with this structure:
in fact if a new point appears, we have to add a new element in the middle of some Segment Tree along the second coordinate, which cannot be effectively done.

In conclusion we note that the two-dimensional Segment Tree contracted in the described way becomes practically equivalent to the modification of the one-dimensional Segment Tree (see [Saving the entire subarrays in each vertex](segment_tree.md#saving-the-entire-subarrays-in-each-vertex)).
In particular the two-dimensional Segment Tree is just a special case of storing a subarray in each vertex of the tree.
It follows, that if you gave to abandon a two-dimensional Segment Tree due to the impossibility of executing a query, it makes sense to try to replace the nested Segment Tree with some more powerful data structure, for example a Cartesian tree.

### Preserving the history of its values (Persistent Segment Tree)

A persistent data structure is a data structure that remembers it previous state for each modification.
This allows to access any version of this data structure that interest us and execute a query on it.

Segment Tree is a data structure that can be turned into a persistent data structure efficiently (both in time and memory consumption).
We want to avoid copying the complete tree before each modification, and we don't want to loose the $O(\log n)$ time behavior for answering range queries.

In fact, any change request in the Segment Tree leads to a change in the data of only $O(\log n)$ vertices along the path starting from the root. 
So if we store the Segment Tree using pointers (i.e. a vertex stores pointers to the left and the right child vertices), then when performing the modification query, we simply need to create new vertices instead of changing the available vertices.
Vertices that are not affected by the modification query can still be used by pointing the pointers to the old vertices.
Thus for a modification query $O(\log n)$ new vertices will be created, including a new root vertex of the Segment Tree, and the entire previous version of the tree rooted at the old root vertex will remain unchanged.

Let's give an example implementation for the simplest Segment Tree: when there is only a query asking for sums, and modification queries of single elements. 

```cpp
struct Vertex {
    Vertex *l, *r;
    int sum;

    Vertex(int val) : l(nullptr), r(nullptr), sum(val) {}
    Vertex(Vertex *l, Vertex *r) : l(l), r(r), sum(0) {
        if (l) sum += l->sum;
        if (r) sum += r->sum;
    }
};

Vertex* build(int a[], int tl, int tr) {
    if (tl == tr)
        return new Vertex(a[tl]);
    int tm = (tl + tr) / 2;
    return new Vertex(build(a, tl, tm), build(a, tm+1, tr));
}

int get_sum(Vertex* v, int tl, int tr, int l, int r) {
    if (l > r)
        return 0;
    if (l == tl && tr == r)
        return v->sum;
    int tm = (tl + tr) / 2;
    return get_sum(v->l, tl, tm, l, min(r, tm))
         + get_sum(v->r, tm+1, tr, max(l, tm+1), r);
}

Vertex* update(Vertex* v, int tl, int tr, int pos, int new_val) {
    if (tl == tr)
        return new Vertex(new_val);
    int tm = (tl + tr) / 2;
    if (pos <= tm)
        return new Vertex(update(v->l, tl, tm, pos, new_val), v->r);
    else
        return new Vertex(v->l, update(v->r, tm+1, tr, pos, new_val));
}
```

For each modification of the Segment Tree we will receive a new root vertex.
To quickly jump between two different versions of the Segment Tree, we need to store this roots in an array.
To use a specific version of the Segment Tree we simply call the query using the appropriate root vertex.

With the approach described above almost any Segment Tree can be turned into a persistent data structure.

#### Finding the $k$-th smallest number in a range {data-toc-label="Finding the k-th smallest number in a range"}

This time we have to answer queries of the form "What is the $k$-th smallest element in the range $a[l \dots r]$. 
This query can be answered using a binary search and a Merge Sort Tree, but the time complexity for a single query would be $O(\log^3 n)$.
We will accomplish the same task using a persistent Segment Tree in $O(\log n)$.

First we will discuss a solution for a simpler problem:
We will only consider arrays in which the elements are bound by $0 \le a[i] \lt n$.
And we only want to find the $k$-th smallest element in some prefix of the array $a$.
It will be very easy to extent the developed ideas later for not restricted arrays and not restricted range queries.
Note that we will be using 1 based indexing for $a$.

We will use a Segment Tree that counts all appearing numbers, i.e. in the Segment Tree we will store the histogram of the array.
So the leaf vertices will store how often the values $0$, $1$, $\dots$, $n-1$ will appear in the array, and the other vertices store how many numbers in some range are in the array. 
In other words we create a regular Segment Tree with sum queries over the histogram of the array.
But instead of creating all $n$ Segment Trees for every possible prefix, we will create one persistent one, that will contain the same information.
We will start with an empty Segment Tree (all counts will be $0$) pointed to by $root_0$, and add the elements $a[1]$, $a[2]$, $\dots$, $a[n]$ one after another.
For each modification we will receive a new root vertex, let's call $root_i$ the root of the Segment Tree after inserting the first $i$ elements of the array $a$.
The Segment Tree rooted at $root_i$ will contain the histogram of the prefix $a[1 \dots i]$.
Using this Segment Tree we can find in $O(\log n)$ time the position of the $k$-th element using the same technique discussed in [Counting the number of zeros, searching for the $k$-th zero](segment_tree.md#counting-zero-search-kth).

Now to the not-restricted version of the problem.

First for the restriction on the queries: 
Instead of only performing these queries over a prefix of $a$, we want to use any arbitrary segments $a[l \dots r]$.
Here we need a Segment Tree that represents the histogram of the elements in the range $a[l \dots r]$. 
It is easy to see that such a Segment Tree is just the difference between the Segment Tree rooted at $root_{r}$ and the Segment Tree rooted at $root_{l-1}$, i.e. every vertex in the $[l \dots r]$ Segment Tree can be computed with the vertex of the $root_{r}$ tree minus the vertex of the $root_{l-1}$ tree.

In the implementation of the $\text{find_kth}$ function this can be handled by passing two vertex pointer and computing the count/sum of the current segment as difference of the two counts/sums of the vertices.

Here are the modified $\text{build}$, $\text{update}$  and $\text{find_kth}$ functions

```cpp
Vertex* build(int tl, int tr) {
    if (tl == tr)
        return new Vertex(0);
    int tm = (tl + tr) / 2;
    return new Vertex(build(tl, tm), build(tm+1, tr));
}

Vertex* update(Vertex* v, int tl, int tr, int pos) {
    if (tl == tr)
        return new Vertex(v->sum+1);
    int tm = (tl + tr) / 2;
    if (pos <= tm)
        return new Vertex(update(v->l, tl, tm, pos), v->r);
    else
        return new Vertex(v->l, update(v->r, tm+1, tr, pos));
}

int find_kth(Vertex* vl, Vertex *vr, int tl, int tr, int k) {
    if (tl == tr)
    	return tl;
    int tm = (tl + tr) / 2, left_count = vr->l->sum - vl->l->sum;
    if (left_count >= k)
    	return find_kth(vl->l, vr->l, tl, tm, k);
    return find_kth(vl->r, vr->r, tm+1, tr, k-left_count);
}
```

As already written above, we need to store the root of the initial Segment Tree, and also all the roots after each update.
Here is the code for building a persistent Segment Tree over an vector `a` with elements in the range `[0, MAX_VALUE]`.

```cpp
int tl = 0, tr = MAX_VALUE + 1;
std::vector<Vertex*> roots;
roots.push_back(build(tl, tr));
for (int i = 0; i < a.size(); i++) {
    roots.push_back(update(roots.back(), tl, tr, a[i]));
}

// find the 5th smallest number from the subarray [a[2], a[3], ..., a[19]]
int result = find_kth(roots[2], roots[20], tl, tr, 5);
```

Now to the restrictions on the array elements:
We can actually transform any array to such an array by index compression.
The smallest element in the array will gets assigned the value 0, the second smallest the value 1, and so forth.
It is easy to generate lookup tables (e.g. using $\text{map}$), that convert a value to its index and vice versa in $O(\log n)$ time.



### Dynamic segment tree

(Called so because its shape is dynamic and the nodes are usually dynamically allocated.
Also known as _implicit segment tree_ or _sparse segment tree_.)

Previously, we considered cases when we have the ability to build the original segment tree. But what to do if the original size is filled with some default element, but its size does not allow you to completely build up to it in advance?

We can solve this problem by creating a segment tree lazily (incrementally). Initially, we will create only the root, and we will create the other vertexes only when we need them.
In this case, we will use the implementation on pointers(before going to the vertex children, check whether they are created, and if not, create them).
Each query has still only the complexity $O(\log n)$, which is small enough for most use-cases (e.g. $\log_2 10^9 \approx 30$).

In this implementation we have two queries, adding a value to a position (initially all values  are $0$), and computing the sum of all values in a range.
`Vertex(0, n)` will be the root vertex of the implicit tree.

```cpp
struct Vertex {
    int left, right;
    int sum = 0;
    Vertex *left_child = nullptr, *right_child = nullptr;

    Vertex(int lb, int rb) {
        left = lb;
        right = rb;
    }

    void extend() {
        if (!left_child && left + 1 < right) {
            int t = (left + right) / 2;
            left_child = new Vertex(left, t);
            right_child = new Vertex(t, right);
        }
    }

    void add(int k, int x) {
        extend();
        sum += x;
        if (left_child) {
            if (k < left_child->right)
                left_child->add(k, x);
            else
                right_child->add(k, x);
        }
    }

    int get_sum(int lq, int rq) {
        if (lq <= left && right <= rq)
            return sum;
        if (max(left, lq) >= min(right, rq))
            return 0;
        extend();
        return left_child->get_sum(lq, rq) + right_child->get_sum(lq, rq);
    }
};
```

Obviously this idea can be extended in lots of different ways. E.g. by adding support for range updates via lazy propagation.

## Practice Problems

* [SPOJ - KQUERY](http://www.spoj.com/problems/KQUERY/) [Persistent segment tree / Merge sort tree]
* [Codeforces - Xenia and Bit Operations](https://codeforces.com/problemset/problem/339/D)
* [UVA 11402 - Ahoy, Pirates!](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2397)
* [SPOJ - GSS3](http://www.spoj.com/problems/GSS3/)
* [Codeforces - Distinct Characters Queries](https://codeforces.com/problemset/problem/1234/D)
* [Codeforces - Knight Tournament](https://codeforces.com/contest/356/problem/A) [For beginners]
* [Codeforces - Ant colony](https://codeforces.com/contest/474/problem/F)
* [Codeforces - Drazil and Park](https://codeforces.com/contest/515/problem/E)
* [Codeforces - Circular RMQ](https://codeforces.com/problemset/problem/52/C)
* [Codeforces - Lucky Array](https://codeforces.com/contest/121/problem/E)
* [Codeforces - The Child and Sequence](https://codeforces.com/contest/438/problem/D)
* [Codeforces - DZY Loves Fibonacci Numbers](https://codeforces.com/contest/446/problem/C) [Lazy propagation]
* [Codeforces - Alphabet Permutations](https://codeforces.com/problemset/problem/610/E)
* [Codeforces - Eyes Closed](https://codeforces.com/problemset/problem/895/E)
* [Codeforces - Kefa and Watch](https://codeforces.com/problemset/problem/580/E)
* [Codeforces - A Simple Task](https://codeforces.com/problemset/problem/558/E)
* [Codeforces - SUM and REPLACE](https://codeforces.com/problemset/problem/920/F)
* [Codeforces - XOR on Segment](https://codeforces.com/problemset/problem/242/E) [Lazy propagation]
* [Codeforces - Please, another Queries on Array?](https://codeforces.com/problemset/problem/1114/F) [Lazy propagation]
* [COCI - Deda](https://oj.uz/problem/view/COCI17_deda) [Last element smaller or equal to x / Binary search]
* [Codeforces - The Untended Antiquity](https://codeforces.com/problemset/problem/869/E) [2D]
* [CSES - Hotel Queries](https://cses.fi/problemset/task/1143)
* [CSES - Polynomial Queries](https://cses.fi/problemset/task/1736)
* [CSES - Range Updates and Sums](https://cses.fi/problemset/task/1735)

