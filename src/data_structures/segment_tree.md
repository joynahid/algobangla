---
tags:
  - Translated
e_maxx_link: segment_tree
---

# সেগমেন্ট ট্রি

সেগমেন্ট ট্রি হল একটি ডেটা স্ট্রাকচার যা অ্যারে ইন্টারভালের তথ্য একটি ট্রির আকারে সংরক্ষণ করে। এটি একটি অ্যারের উপর রেঞ্জ কোয়েরিতে দক্ষভাবে উত্তর দিতে দেয়, এবং একই সাথে অ্যারে দ্রুত পরিবর্তনের জন্য যথেষ্ট নমনীয়।
এতে $a[l \dots r]$ ক্রমাগত অ্যারে উপাদানের যোগফল খুঁজে পাওয়া বা এই ধরনের একটি রেঞ্জে ন্যূনতম উপাদান $O(\log n)$ সময়ে খুঁজে পাওয়া অন্তর্ভুক্ত।
এই ধরনের কোয়েরিতে উত্তর দেওয়ার মধ্যে, সেগমেন্ট ট্রি একটি উপাদান প্রতিস্থাপন করে অথবা সম্পূর্ণ সাবসেগমেন্টের উপাদান পরিবর্তন করে (যেমন সমস্ত উপাদান $a[l \dots r]$ যেকোনো মান নির্ধারণ করা, বা সাবসেগমেন্টের সমস্ত উপাদানে একটি মান যোগ করা) অ্যারে পরিবর্তন করতে দেয়।

সাধারণভাবে, সেগমেন্ট ট্রি একটি অত্যন্ত নমনীয় ডেটা স্ট্রাকচার, এবং এটির সাথে বিশাল সংখ্যক সমস্যা সমাধান করা যায়।
অতিরিক্তভাবে, আরও জটিল অপারেশন প্রয়োগ এবং আরও জটিল কোয়েরির উত্তর দেওয়াও সম্ভব (দেখুন [সেগমেন্ট ট্রির উন্নত সংস্করণ](segment_tree.md#advanced-versions-of-segment-trees))।
বিশেষত সেগমেন্ট ট্রি সহজেই বৃহত্তর মাত্রায় সাধারণীকৃত করা যায়।
উদাহরণস্বরূপ, একটি দ্বি-মাত্রিক সেগমেন্ট ট্রির সাথে আপনি একটি প্রদত্ত ম্যাট্রিক্সের কিছু সাবরেক্ট্যাঙ্গেলের উপর সাম বা ন্যূনতম কোয়েরিতে $O(\log^2 n)$ সময়ে উত্তর দিতে পারেন।

সেগমেন্ট ট্রির একটি গুরুত্বপূর্ণ বৈশিষ্ট্য হল তাদের কেবল রৈখিক পরিমাণ মেমোরি প্রয়োজন।
স্ট্যান্ডার্ড সেগমেন্ট ট্রি আকার $n$ এর একটি অ্যারেতে কাজ করার জন্য $4n$ ভার্টেক্স প্রয়োজন। 

## সেগমেন্ট ট্রির সহজতম রূপ

সহজভাবে শুরু করতে, আমরা সেগমেন্ট ট্রির সহজতম রূপ বিবেচনা করি।
আমরা সাম কোয়েরিতে দক্ষভাবে উত্তর দিতে চাই।
আমাদের কাজের আনুষ্ঠানিক সংজ্ঞা হল:
একটি অ্যারে $a[0 \dots n-1]$ দেওয়া হলে, সেগমেন্ট ট্রি অবশ্যই সূচক $l$ এবং $r$ এর মধ্যে উপাদানের যোগফল খুঁজে পেতে সক্ষম হতে হবে (অর্থাৎ যোগফল $\sum_{i=l}^r a[i]$ গণনা করা), এবং অ্যারেতে উপাদানের মান পরিবর্তন করতে সামলাতে হবে (অর্থাৎ $a[i] = x$ ফর্মের অ্যাসাইনমেন্ট সম্পাদন করা)।
সেগমেন্ট ট্রি **উভয়** কোয়েরি $O(\log n)$ সময়ে প্রক্রিয়া করতে সক্ষম হতে হবে।

এটি সরল পদ্ধতির একটি উন্নতি।
একটি সরল অ্যারে ইমপ্লিমেন্টেশন - শুধুমাত্র একটি সাধারণ অ্যারে ব্যবহার করা - উপাদান $O(1)$ এ আপডেট করতে পারে, কিন্তু প্রতিটি সাম কোয়েরি গণনা করতে $O(n)$ প্রয়োজন।
এবং পূর্বনির্ধারিত প্রিফিক্স সাম সাম কোয়েরি $O(1)$ এ গণনা করতে পারে, কিন্তু একটি অ্যারে উপাদান আপডেট করতে প্রিফিক্স সামের $O(n)$ পরিবর্তন প্রয়োজন।

### সেগমেন্ট ট্রির কাঠামো

অ্যারে সেগমেন্টের ক্ষেত্রে আমরা একটি ডিভাইড অ্যান্ড কনকার পদ্ধতি অনুসরণ করতে পারি।
আমরা সম্পূর্ণ অ্যারের উপাদানের যোগফল গণনা এবং সংরক্ষণ করি, অর্থাৎ সেগমেন্ট $a[0 \dots n-1]$ এর যোগফল।
তারপর আমরা অ্যারেকে দুটি অংশে ভাগ করি $a[0 \dots (n-1)/2]$ এবং $a[(n+1)/2 \dots n-1]$ এবং প্রতিটি অর্ধ অংশের যোগফল গণনা এবং সংরক্ষণ করি।
এই দুটি অর্ধ অংশের প্রত্যেকটি ক্রমে অর্ধেক করা হয়, এবং এভাবে চলে যতক্ষণ না সমস্ত সেগমেন্ট আকার $১$ এ পৌঁছায়।

আমরা এই সেগমেন্টগুলিকে একটি বাইনারি ট্রি তৈরি করার দৃষ্টিভঙ্গি থেকে দেখতে পারি:
এই ট্রির রুট হল সেগমেন্ট $a[0 \dots n-1]$, এবং প্রতিটি ভার্টেক্স (লিফ ভার্টেক্স ছাড়া) ঠিক দুটি চাইল্ড ভার্টেক্স রয়েছে।
এজন্যই ডেটা স্ট্রাকচারকে "সেগমেন্ট ট্রি" বলা হয়, যদিও বেশিরভাগ ইমপ্লিমেন্টেশনে ট্রিটি স্পষ্টভাবে নির্মিত হয় না (দেখুন [ইমপ্লিমেন্টেশন](segment_tree.md#implementation))।

$a = [1, 3, -2, 8, -7]$ অ্যারের উপর এই ধরনের সেগমেন্ট ট্রির একটি ভিজ্যুয়াল উপস্থাপনা এখানে রয়েছে:

!["সাম সেগমেন্ট ট্রি"](sum-segment-tree.png)

ডেটা স্ট্রাকচারের এই সংক্ষিপ্ত বর্ণনা থেকে, আমরা ইতিমধ্যে উপসংহার করতে পারি যে একটি সেগমেন্ট ট্রি শুধুমাত্র রৈখিক সংখ্যক ভার্টেক্স প্রয়োজন।
ট্রির প্রথম স্তরে একটি একক নোড (রুট) রয়েছে, দ্বিতীয় স্তরে দুটি ভার্টেক্স থাকবে, তৃতীয় স্তরে চারটি ভার্টেক্স থাকবে, যতক্ষণ না ভার্টেক্সের সংখ্যা $n$ এ পৌঁছায়।
এইভাবে সর্বোচ্চ ক্ষেত্রে ভার্টেক্সের সংখ্যা যোগফল $1 + 2 + 4 + \dots + 2^{\lceil\log_2 n\rceil} \lt 2^{\lceil\log_2 n\rceil + 1} \lt 4n$ দ্বারা অনুমান করা যায়।

এটি লক্ষ্য করার মতো যে যখনই $n$ দুইয়ের শক্তি নয়, সেগমেন্ট ট্রির সমস্ত স্তর সম্পূর্ণভাবে পূর্ণ হবে না।
আমরা ছবিতে সেই আচরণ দেখতে পারি।
আপাতত আমরা এই তথ্য ভুলতে পারি, কিন্তু এটি পরবর্তীতে ইমপ্লিমেন্টেশনের সময় গুরুত্বপূর্ণ হয়ে উঠবে।

সেগমেন্ট ট্রির উচ্চতা $O(\log n)$, কারণ রুট থেকে পাতার দিকে নেমে যাওয়ার সময় সেগমেন্টের আকার প্রায় অর্ধেক হ্রাস পায়। 

### নির্মাণ

সেগমেন্ট ট্রি নির্মাণের আগে, আমাদের সিদ্ধান্ত নিতে হবে:

১. সেগমেন্ট ট্রির প্রতিটি নোডে যা *মান* সংরক্ষিত হয়।
   উদাহরণস্বরূপ, একটি সাম সেগমেন্ট ট্রিতে, একটি নোড তার রেঞ্জ $[l, r]$ এ উপাদানগুলির যোগফল সংরক্ষণ করবে।
২. সেগমেন্ট ট্রিতে দুটি ভাইবোনকে মার্জ করে এমন *মার্জ* অপারেশন।
   উদাহরণস্বরূপ, একটি সাম সেগমেন্ট ট্রিতে, রেঞ্জ $a[l_1 \dots r_1]$ এবং $a[l_2 \dots r_2]$ এর সাথে সম্পর্কিত দুটি নোড রেঞ্জ $a[l_1 \dots r_2]$ এর সাথে সম্পর্কিত একটি নোডে দুটি নোডের মানগুলি যোগ করে মার্জ করা হবে।

মনে রাখবেন যে একটি ভার্টেক্স একটি "লিফ ভার্টেক্স", যদি এর সম্পর্কিত সেগমেন্ট মূল অ্যারেতে শুধুমাত্র একটি মান কভার করে। এটি সেগমেন্ট ট্রির সর্বনিম্ন স্তরে উপস্থিত। এর মান (সম্পর্কিত) উপাদান $a[i]$ এর সমান হবে।

এখন, সেগমেন্ট ট্রির নির্মাণের জন্য, আমরা নীচের স্তরে (লিফ ভার্টেক্স) শুরু করি এবং তাদের যথাযথ মানগুলি নির্ধারণ করি। এই মানগুলির ভিত্তিতে, আমরা `মার্জ` ফাংশন ব্যবহার করে পূর্ববর্তী স্তরের মানগুলি গণনা করতে পারি।
এবং সেগুলির ভিত্তিতে, আমরা পূর্ববর্তী স্তরের মানগুলি গণনা করতে পারি, এবং যতক্ষণ না আমরা রুট ভার্টেক্সে পৌঁছাই ততক্ষণ প্রক্রিয়াটি পুনরাবৃত্তি করি।

এই অপারেশনটি অন্য দিকে, অর্থাৎ রুট ভার্টেক্স থেকে লিফ ভার্টেক্স পর্যন্ত রিকার্সিভভাবে বর্ণনা করা সুবিধাজনক। নির্মাণ প্রক্রিয়া, যদি একটি নন-লিফ ভার্টেক্সে বলা হয়, তবে নিম্নোক্তটি করে:

१. দুটি চাইল্ড ভার্টেক্সের মানগুলি রিকার্সিভভাবে নির্মাণ করুন
२. এই চাইল্ডগুলির গণনা করা মানগুলি মার্জ করুন।

আমরা রুট ভার্টেক্সে নির্মাণ শুরু করি, এবং সুতরাং, আমরা সম্পূর্ণ সেগমেন্ট ট্রি গণনা করতে সক্ষম।

এই নির্মাণের সময় কমপ্লেক্সিটি $O(n)$, ধরে নিয়ে যে মার্জ অপারেশন ধ্রুবক সময় (মার্জ অপারেশন $n$ বার বলা হয়, যা সেগমেন্ট ট্রিতে অভ্যন্তরীণ নোডের সংখ্যার সমান)।

### সাম কোয়েরি

এখন আমরা সাম কোয়েরির উত্তর দিতে যাচ্ছি। ইনপুট হিসাবে আমরা দুটি পূর্ণসংখ্যা $l$ এবং $r$ পাই, এবং আমাদের সেগমেন্ট $a[l \dots r]$ এর যোগফল $O(\log n)$ সময়ে গণনা করতে হবে।

এটি করতে, আমরা সেগমেন্ট ট্রি অতিক্রম করব এবং সেগমেন্টগুলির পূর্বনির্ধারিত যোগফল ব্যবহার করব।
ধরুন আমরা বর্তমানে সেগমেন্ট $a[tl \dots tr]$ কভার করে এমন ভার্টেক্সে আছি।
তিনটি সম্ভাব্য ক্ষেত্র রয়েছে।

সবচেয়ে সহজ ক্ষেত্র হল যখন সেগমেন্ট $a[l \dots r]$ বর্তমান ভার্টেক্সের সম্পর্কিত সেগমেন্টের সমান (অর্থাৎ $a[l \dots r] = a[tl \dots tr]$), তখন আমরা শেষ এবং ভার্টেক্সে সংরক্ষিত পূর্বনির্ধারিত যোগফল ফেরত দিতে পারি।

বিকল্পভাবে কোয়েরির সেগমেন্ট বাম বা ডান চাইল্ডের ডোমেইনে সম্পূর্ণভাবে পড়তে পারে।
মনে রাখবেন যে বাম চাইল্ড সেগমেন্ট $a[tl \dots tm]$ কভার করে এবং ডান ভার্টেক্স সেগমেন্ট $a[tm + 1 \dots tr]$ কভার করে $tm = (tl + tr) / 2$ সহ।
এই ক্ষেত্রে আমরা সহজেই চাইল্ড ভার্টেক্সে যেতে পারি, যার সম্পর্কিত সেগমেন্ট কোয়েরি সেগমেন্ট কভার করে, এবং সেই ভার্টেক্সের সাথে এখানে বর্ণিত অ্যালগরিদম সম্পাদন করি।

এবং তারপর শেষ ক্ষেত্র আছে, কোয়েরি সেগমেন্ট উভয় চাইল্ডের সাথে ছেদ করে।
এই ক্ষেত্রে আমাদের কাছে দুটি রিকার্সিভ কল করার ছাড়া অন্য কোনো বিকল্প নেই, একটি প্রতিটি চাইল্ডের জন্য।
প্রথমে আমরা বাম চাইল্ডে যাই, এই ভার্টেক্সের জন্য একটি আংশিক উত্তর গণনা করি (অর্থাৎ কোয়েরির সেগমেন্ট এবং বাম চাইল্ডের সেগমেন্টের মধ্যে ছেদের মানগুলির যোগফল), তারপর ডান চাইল্ডে যাই, সেই ভার্টেক্স ব্যবহার করে আংশিক উত্তর গণনা করি, এবং তারপর উত্তরগুলি একসাথে যোগ করে সমন্বয় করি।
অন্য কথায়, বাম চাইল্ড সেগমেন্ট $a[tl \dots tm]$ এবং ডান চাইল্ড সেগমেন্ট $a[tm+1 \dots tr]$ প্রতিনিধিত্ব করে, আমরা বাম চাইল্ড ব্যবহার করে সাম কোয়েরি $a[l \dots tm]$ গণনা করি, এবং ডান চাইল্ড ব্যবহার করে সাম কোয়েরি $a[tm+1 \dots r]$ গণনা করি।

তাই একটি সাম কোয়েরি প্রক্রিয়া করা একটি ফাংশন যা বাম বা ডান চাইল্ডের একটি বা অন্যটির সাথে নিজেকে একবার রিকার্সিভভাবে কল করে (কোয়েরি সীমানা পরিবর্তন না করে), বা দুবার, একবার বাম এবং একবার ডান চাইল্ডের সাথে (কোয়েরিকে দুটি সাবকোয়েরিতে বিভাজন করে)। 
এবং রিকার্সন শেষ হয়, যখনই বর্তমান কোয়েরি সেগমেন্টের সীমানা বর্তমান ভার্টেক্সের সেগমেন্টের সীমানার সাথে মিলে যায়।
সেই ক্ষেত্রে উত্তর হবে এই সেগমেন্টের যোগফলের পূর্বনির্ধারিত মান, যা ট্রিতে সংরক্ষিত।

অন্য কথায়, কোয়েরির গণনা একটি ট্রি অতিক্রম, যা ট্রির সমস্ত প্রয়োজনীয় শাখা জুড়ে ছড়িয়ে পড়ে, এবং ট্রিতে সেগমেন্টগুলির পূর্বনির্ধারিত যোগফল মানগুলি ব্যবহার করে।

স্পষ্টতার জন্য আমরা সেগমেন্ট ট্রির রুট ভার্টেক্স থেকে অতিক্রম শুরু করব।

পদ্ধতিটি নিম্নলিখিত চিত্রে চিত্রিত হয়েছে।
আবার অ্যারে $a = [1, 3, -2, 8, -7]$ ব্যবহার করা হয়, এবং এখানে আমরা যোগফল $\sum_{i=2}^4 a[i]$ গণনা করতে চাই।
রঙিন ভার্টেক্সগুলি পরিদর্শন করা হবে, এবং আমরা সবুজ ভার্টেক্সগুলির পূর্বনির্ধারিত মানগুলি ব্যবহার করব।
এটি আমাদের ফলাফল $-2 + 1 = -1$ দেয়।

!["সাম সেগমেন্ট ট্রি কোয়েরি"](sum-segment-tree-query.png)

কেন এই অ্যালগরিদমের কমপ্লেক্সিটি $O(\log n)$?
এই কমপ্লেক্সিটি প্রদর্শন করতে আমরা ট্রির প্রতিটি স্তর দেখি।
দেখা যায় যে প্রতিটি স্তরের জন্য আমরা চারটিরও বেশি ভার্টেক্স পরিদর্শন করি না।
এবং যেহেতু ট্রির উচ্চতা $O(\log n)$, আমরা পছন্দসই চলমান সময় পাই।

আমরা এই প্রস্তাব (প্রতিটি স্তরে সর্বাধিক চারটি ভার্টেক্স) প্রমাণ করতে পারি ইন্ডাকশন দ্বারা।
প্রথম স্তরে, আমরা শুধুমাত্র একটি ভার্টেক্স, রুট ভার্টেক্স পরিদর্শন করি, তাই এখানে আমরা চারটিরও কম ভার্টেক্স পরিদর্শন করি।
এখন একটি স্বেচ্ছাচারী স্তর দেখি।
ইন্ডাকশন হাইপোথিসিস দ্বারা, আমরা সর্বাধিক চারটি ভার্টেক্স পরিদর্শন করি।
যদি আমরা সর্বাধিক দুটি ভার্টেক্স পরিদর্শন করি, পরবর্তী স্তরে সর্বাধিক চারটি ভার্টেক্স রয়েছে। এটি তুচ্ছ, কারণ প্রতিটি ভার্টেক্স সর্বাধিক দুটি রিকার্সিভ কল সৃষ্টি করতে পারে।
তাই আসুন ধরুন যে আমরা বর্তমান স্তরে তিন বা চারটি ভার্টেক্স পরিদর্শন করি।
সেই ভার্টেক্সগুলি থেকে, আমরা মধ্যের ভার্টেক্সগুলি আরও সাবধানে বিশ্লেষণ করব।
যেহেতু সাম কোয়েরি একটি ক্রমাগত সাবঅ্যারের যোগফল জিজ্ঞাসা করে, আমরা জানি যে মধ্যের পরিদর্শিত ভার্টেক্সগুলির সাথে সম্পর্কিত সেগমেন্টগুলি সাম কোয়েরির সেগমেন্ট দ্বারা সম্পূর্ণভাবে কভার করা হবে।
অতএব এই ভার্টেক্সগুলি কোনো রিকার্সিভ কল করবে না।
তাই শুধুমাত্র সবচেয়ে বাম এবং সবচেয়ে ডান ভার্টেক্সের রিকার্সিভ কল করার সম্ভাবনা থাকবে।
এবং সেগুলি শুধুমাত্র সর্বাধিক চারটি রিকার্সিভ কল সৃষ্টি করবে, তাই পরবর্তী স্তরও প্রস্তাব সন্তুষ্ট করবে।
আমরা বলতে পারি যে একটি শাখা কোয়েরির বাম সীমানার কাছে পৌঁছায়, এবং দ্বিতীয় শাখা ডানটির কাছে পৌঁছায়।

অতএব আমরা মোট সর্বাধিক $4 \log n$ ভার্টেক্স পরিদর্শন করি, এবং এটি $O(\log n)$ এর একটি চলমান সময়ের সমান।

উপসংহারে কোয়েরিটি ইনপুট সেগমেন্টকে বেশ কয়েকটি সাব-সেগমেন্টে বিভক্ত করে কাজ করে যার জন্য সমস্ত যোগফল ইতিমধ্যে প্রি-কম্পিউটেড এবং ট্রিতে সংরক্ষিত।
এবং যখনই কোয়েরি সেগমেন্ট ভার্টেক্স সেগমেন্টের সাথে মিলে যায় তখন যদি আমরা বিভাজন থামাই, তবে আমাদের শুধুমাত্র $O(\log n)$ এই ধরনের সেগমেন্ট প্রয়োজন, যা সেগমেন্ট ট্রির কার্যকারিতা দেয়। 

### আপডেট কোয়েরি

এখন আমরা অ্যারেতে একটি নির্দিষ্ট উপাদান পরিবর্তন করতে চাই, ধরুন আমরা অ্যাসাইনমেন্ট $a[i] = x$ করতে চাই।
এবং আমাদের সেগমেন্ট ট্রি পুনর্নির্মাণ করতে হবে, যাতে এটি নতুন, পরিবর্তিত অ্যারের সাথে মিল খায়।

এই কোয়েরি সাম কোয়েরির চেয়ে সহজ।
সেগমেন্ট ট্রির প্রতিটি স্তর অ্যারের একটি বিভাজন গঠন করে।
অতএব একটি উপাদান $a[i]$ প্রতিটি স্তর থেকে শুধুমাত্র একটি সেগমেন্টে অবদান রাখে।
এইভাবে শুধুমাত্র $O(\log n)$ ভার্টেক্স আপডেট করা প্রয়োজন।

এটি সহজে দেখা যায় যে আপডেট অনুরোধটি একটি রিকার্সিভ ফাংশন ব্যবহার করে প্রয়োগ করা যেতে পারে।
ফাংশনটি বর্তমান ট্রি ভার্টেক্স পাস করা হয়, এবং এটি দুটি চাইল্ড ভার্টেক্সের একটির সাথে নিজেকে রিকার্সিভভাবে কল করে (যেটি তার সেগমেন্টে $a[i]$ ধারণ করে), এবং এর পরে এর যোগফল মান পুনরায় গণনা করে, যেভাবে বিল্ড পদ্ধতিতে করা হয় (অর্থাৎ এর দুটি চাইল্ডের যোগফল হিসাবে)।

আবার এখানে একই অ্যারে ব্যবহার করে একটি ভিজ্যুয়ালাইজেশন রয়েছে।
এখানে আমরা আপডেট $a[2] = 3$ সম্পাদন করি।
সবুজ ভার্টেক্সগুলি হল সেই ভার্টেক্স যা আমরা পরিদর্শন এবং আপডেট করি।

!["সাম সেগমেন্ট ট্রি আপডেট"](sum-segment-tree-update.png)

### ইমপ্লিমেন্টেশন ### { #implementation}

প্রধান বিবেচনা হল সেগমেন্ট ট্রি কীভাবে সংরক্ষণ করা যায়।
অবশ্যই আমরা একটি $\text{ভার্টেক্স}$ স্ট্রাক্ট সংজ্ঞায়িত করতে পারি এবং বস্তু তৈরি করতে পারি, যা সেগমেন্টের সীমানা, এর যোগফল এবং অতিরিক্তভাবে এর চাইল্ড ভার্টেক্সের পয়েন্টার সংরক্ষণ করে।
তবে, এটি পয়েন্টার আকারে অনেক রিডানড্যান্ট তথ্য সংরক্ষণ করতে প্রয়োজন।
আমরা একটি সরল কৌশল ব্যবহার করব এটি আরও দক্ষ করতে একটি _ইমপ্লিসিট ডেটা স্ট্রাকচার_ ব্যবহার করে: শুধুমাত্র একটি অ্যারেতে যোগফল সংরক্ষণ করা।
(একটি অনুরূপ পদ্ধতি বাইনারি হিপের জন্য ব্যবহার করা হয়)।
সূচক १ এ রুট ভার্টেক্সের যোগফল, সূচক २ এবং ३ এ এর দুটি চাইল্ড ভার্টেক্সের যোগফল, সূচক ४ থেকে ७ এ সেই দুটি ভার্টেক্সের চাইল্ডদের যোগফল, এবং এভাবে চলে।
१-ইন্ডেক্সিং সহ, সুবিধামত সূচক $i$ এ একটি ভার্টেক্সের বাম চাইল্ড সূচক $२i$ তে সংরক্ষিত হয়, এবং ডানটি সূচক $२i + १$ তে।
সমানভাবে, সূচক $i$ এ একটি ভার্টেক্সের পিতামাতা $i/२$ তে সংরক্ষিত হয় (পূর্ণসংখ্যা বিভাগ)।

এটি ইমপ্লিমেন্টেশনকে অনেক সহজ করে।
আমাদের স্মৃতিতে ট্রির কাঠামো সংরক্ষণ করতে হবে না।
এটি অন্তর্নিহিতভাবে সংজ্ঞায়িত।
আমাদের শুধুমাত্র একটি অ্যারে প্রয়োজন যা সমস্ত সেগমেন্টের যোগফল ধারণ করে।

আগে উল্লেখ করা হয়েছে, আমাদের সর্বাধিক $4n$ ভার্টেক্স সংরক্ষণ করতে হবে।
এটি কম হতে পারে, তবে সুবিধার জন্য আমরা সর্বদা আকার $4n$ এর একটি অ্যারে বরাদ্দ করি।
যোগফল অ্যারেতে এমন কিছু উপাদান থাকবে যা প্রকৃত ট্রিতে কোনো ভার্টেক্সের সাথে সম্পর্কিত নয়, তবে এটি ইমপ্লিমেন্টেশনকে জটিল করে না।

তাই আমরা সেগমেন্ট ট্রি সহজভাবে একটি অ্যারে $t[]$ হিসাবে ইনপুট আকার $n$ এর চারগুণ আকার সহ সংরক্ষণ করি:

```{.cpp file=segment_tree_implementation_definition}
int n, t[4*MAXN];
```

একটি প্রদত্ত অ্যারে $a[]$ থেকে সেগমেন্ট ট্রি নির্মাণের পদ্ধতি এইরকম দেখায়:
এটি প্যারামিটার $a[]$ (ইনপুট অ্যারে), $v$ (বর্তমান ভার্টেক্সের সূচক), এবং বর্তমান সেগমেন্টের সীমানা $tl$ এবং $tr$ সহ একটি রিকার্সিভ ফাংশন।
প্রধান প্রোগ্রামে এই ফাংশনটি রুট ভার্টেক্সের প্যারামিটার সহ বলা হবে: $v = १$, $tl = ०$, এবং $tr = n - १$।

```{.cpp file=segment_tree_implementation_build}
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

```{.cpp file=segment_tree_implementation_sum}
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

```{.cpp file=segment_tree_implementation_update}
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

বেশিরভাগ মানুষ পূর্ববর্তী বিভাগ থেকে ইমপ্লিমেন্টেশন ব্যবহার করে। যদি আপনি অ্যারে `t` তাকান আপনি দেখতে পারবেন যে এটি একটি BFS ট্রাভার্সাল (স্তর-অর্ডার ট্রাভার্সাল) এর ক্রমে ট্রি নোডের নাম্বারিং অনুসরণ করে।
এই ট্রাভার্সাল ব্যবহার করে ভার্টেক্স $v$ এর চাইল্ডগুলি যথাক্রমে $२v$ এবং $२v + १$ হয়।
তবে যদি $n$ দুইয়ের শক্তি না হয়, এই পদ্ধতিটি কিছু সূচক এড়িয়ে যাবে এবং অ্যারে `t` এর কিছু অংশ অব্যবহৃত রেখে যাবে।
মেমোরি খরচ $4n$ দ্বারা সীমিত, যদিও $n$ উপাদানের একটি অ্যারের সেগমেন্ট ট্রির জন্য শুধুমাত্র $२n - १$ ভার্টেক্স প্রয়োজন।

তবে এটি হ্রাস করা যায়।
আমরা একটি Euler ট্যুর ট্রাভার্সাল (প্রি-অর্ডার ট্রাভার্সাল) এর ক্রমে ট্রির ভার্টেক্সগুলির নাম্বার পুনর্নির্ধারণ করি, এবং আমরা এই সমস্ত ভার্টেক্সগুলি একসাথে লিখি।

সূচক $v$ তে একটি ভার্টেক্স বিবেচনা করি, এবং এটি সেগমেন্ট $[l, r]$ এর জন্য দায়বদ্ধ, এবং $mid = \dfrac{l + r}{२}$।
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

The tree will have exactly the same structure as the tree described above. 
We only need to change the way $t[v]$ is computed in the $\text{build}$ and $\text{update}$ functions.
$t[v]$ will now store the maximum of the corresponding segment. 
And we also need to change the calculation of the returned value of the $\text{sum}$ function (replacing the summation by the maximum).

Of course this problem can be easily changed into computing the minimum instead of the maximum.

Instead of showing an implementation to this problem, the implementation will be given to a more complex version of this problem in the next section.

#### Finding the maximum and the number of times it appears 

This task is very similar to the previous one.
In addition of finding the maximum, we also have to find the number of occurrences of the maximum. 

To solve this problem, we store a pair of numbers at each vertex in the tree: 
In addition to the maximum we also store the number of occurrences of it in the corresponding segment. 
Determining the correct pair to store at $t[v]$ can still be done in constant time using the information of the pairs stored at the child vertices. 
Combining two such pairs should be done in a separate function, since this will be an operation that we will do while building the tree, while answering maximum queries and while performing modifications.

```{.cpp file=segment_tree_maximum_and_count}
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
#### Compute the greatest common divisor / least common multiple

In this problem we want to compute the GCD / LCM of all numbers of given ranges of the array. 

This interesting variation of the Segment Tree can be solved in exactly the same way as the Segment Trees we derived for sum / minimum / maximum queries:
it is enough to store the GCD / LCM of the corresponding vertex in each vertex of the tree. 
Combining two vertices can be done by computing the GCD / LCM of both vertices.

#### Counting the number of zeros, searching for the $k$-th zero { #counting-zero-search-kth data-toc-label="Counting the number of zeros, searching for the k-th zero"}

In this problem we want to find the number of zeros in a given range, and additionally find the index of the $k$-th zero using a second function.

Again we have to change the store values of the tree a bit:
This time we will store the number of zeros in each segment in $t[]$. 
It is pretty clear, how to implement the $\text{build}$, $\text{update}$ and $\text{count_zero}$ functions, we can simply use the ideas from the sum query problem.
Thus we solved the first part of the problem.

Now we learn how to solve the problem of finding the $k$-th zero in the array $a[]$. 
To do this task, we will descend the Segment Tree, starting at the root vertex, and moving each time to either the left or the right child, depending on which segment contains the $k$-th zero.
In order to decide to which child we need to go, it is enough to look at the number of zeros appearing in the segment corresponding to the left vertex.
If this precomputed count is greater or equal to $k$, it is necessary to descend to the left child, and otherwise descent to the right child.
Notice, if we chose the right child, we have to subtract the number of zeros of the left child from $k$.

In the implementation we can handle the special case, $a[]$ containing less than $k$ zeros, by returning -1.

```{.cpp file=segment_tree_kth_zero}
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

#### Searching for an array prefix with a given amount

The task is as follows: 
for a given value $x$ we have to quickly find smallest index $i$ such that the sum of the first $i$ elements of the array $a[]$ is greater or equal to $x$ (assuming that the array $a[]$ only contains non-negative values).

This task can be solved using binary search, computing the sum of the prefixes with the Segment Tree.
However this will lead to a $O(\log^2 n)$ solution.

Instead we can use the same idea as in the previous section, and find the position by descending the tree:
by moving each time to the left or the right, depending on the sum of the left child.
Thus finding the answer in $O(\log n)$ time.

#### Searching for the first element greater than a given amount

The task is as follows: 
for a given value $x$ and a range $a[l \dots r]$ find the smallest $i$  in the range $a[l \dots r]$, such that $a[i]$ is greater than $x$.

This task can be solved using binary search over max prefix queries with the Segment Tree.
However, this will lead to a $O(\log^2 n)$ solution.

Instead, we can use the same idea as in the previous sections, and find the position by descending the tree:
by moving each time to the left or the right, depending on the maximum value of the left child.
Thus finding the answer in $O(\log n)$ time. 

```{.cpp file=segment_tree_first_greater}
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

#### Finding subsegments with the maximal sum

Here again we receive a range $a[l \dots r]$ for each query, this time we have to find a subsegment $a[l^\prime \dots r^\prime]$ such that $l \le l^\prime$ and $r^\prime \le r$ and the sum of the elements of this segment is maximal. 
As before we also want to be able to modify individual elements of the array. 
The elements of the array can be negative, and the optimal subsegment can be empty (e.g. if all elements are negative).

This problem is a non-trivial usage of a Segment Tree.
This time we will store four values for each vertex: 
the sum of the segment, the maximum prefix sum, the maximum suffix sum, and the sum of the maximal subsegment in it.
In other words for each segment of the Segment Tree the answer is already precomputed as well as the answers for segments touching the left and the right boundaries of the segment.

How to build a tree with such data?
Again we compute it in a recursive fashion: 
we first compute all four values for the left and the right child, and then combine those to archive the four values for the current vertex.
Note the answer for the current vertex is either:

 * the answer of the left child, which means that the optimal subsegment is entirely placed in the segment of the left child
 * the answer of the right child, which means that the optimal subsegment is entirely placed in the segment of the right child
 * the sum of the maximum suffix sum of the left child and the maximum prefix sum of the right child, which means that the optimal subsegment intersects with both children.

Hence the answer to the current vertex is the maximum of these three values. 
Computing the maximum prefix / suffix sum is even easier. 
Here is the implementation of the $\text{combine}$ function, which receives only data from the left and right child, and returns the data of the current vertex. 

```{.cpp file=segment_tree_maximal_sum_subsegments1}
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

Using the $\text{combine}$ function it is easy to build the Segment Tree. 
We can implement it in exactly the same way as in the previous implementations.
To initialize the leaf vertices, we additionally create the auxiliary function $\text{make_data}$, which will return a $\text{data}$ object holding the information of a single value.

```{.cpp file=segment_tree_maximal_sum_subsegments2}
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

It only remains, how to compute the answer to a query. 
To answer it, we go down the tree as before, breaking the query into several subsegments that coincide with the segments of the Segment Tree, and combine the answers in them into a single answer for the query.
Then it should be clear, that the work is exactly the same as in the simple Segment Tree, but instead of summing / minimizing / maximizing the values, we use the $\text{combine}$ function.

```{.cpp file=segment_tree_maximal_sum_subsegments3}
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

### <a name="saving-the-entire-subarrays-in-each-vertex"></a>Saving the entire subarrays in each vertex

This is a separate subsection that stands apart from the others, because at each vertex of the Segment Tree we don't store information about the corresponding segment in compressed form (sum, minimum, maximum, ...), but store all elements of the segment.
Thus the root of the Segment Tree will store all elements of the array, the left child vertex will store the first half of the array, the right vertex the second half, and so on.

In its simplest application of this technique we store the elements in sorted order.
In more complex versions the elements are not stored in lists, but more advanced data structures (sets, maps, ...). 
But all these methods have the common factor, that each vertex requires linear memory (i.e. proportional to the length of the corresponding segment).

The first natural question, when considering these Segment Trees, is about memory consumption.
Intuitively this might look like $O(n^2)$ memory, but it turns out that the complete tree will only need $O(n \log n)$ memory.
Why is this so?
Quite simply, because each element of the array falls into $O(\log n)$ segments (remember the height of the tree is $O(\log n)$). 

So in spite of the apparent extravagance of such a Segment Tree, it consumes only slightly more memory than the usual Segment Tree. 

Several typical applications of this data structure are described below.
It is worth noting the similarity of these Segment Trees with 2D data structures (in fact this is a 2D data structure, but with rather limited capabilities).

#### Find the smallest number greater or equal to a specified number. No modification queries.

We want to answer queries of the following form: 
for three given numbers $(l, r, x)$ we have to find the minimal number in the segment $a[l \dots r]$ which is greater than or equal to $x$.

We construct a Segment Tree. 
In each vertex we store a sorted list of all numbers occurring in the corresponding segment, like described above. 
How to build such a Segment Tree as effectively as possible?
As always we approach this problem recursively: let the lists of the left and right children already be constructed, and we want to build the list for the current vertex.
From this view the operation is now trivial and can be accomplished in linear time:
We only need to combine the two sorted lists into one, which can be done by iterating over them using two pointers. 
The C++ STL already has an implementation of this algorithm.

Because this structure of the Segment Tree and the similarities to the merge sort algorithm, the data structure is also often called "Merge Sort Tree".

```{.cpp file=segment_tree_smallest_number_greater1}
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

We already know that the Segment Tree constructed in this way will require $O(n \log n)$ memory.
And thanks to this implementation its construction also takes $O(n \log n)$ time, after all each list is constructed in linear time in respect to its size. 

Now consider the answer to the query. 
We will go down the tree, like in the regular Segment Tree, breaking our segment $a[l \dots r]$ into several subsegments (into at most $O(\log n)$ pieces). 
It is clear that the answer of the whole answer is the minimum of each of the subqueries.
So now we only need to understand, how to respond to a query on one such subsegment that corresponds with some vertex of the tree.

We are at some vertex of the Segment Tree and we want to compute the answer to the query, i.e. find the minimum number greater that or equal to a given number $x$. 
Since the vertex contains the list of elements in sorted order, we can simply perform a binary search on this list and return the first number, greater than or equal to $x$.

Thus the answer to the query in one segment of the tree takes $O(\log n)$ time, and the entire query is processed in $O(\log^2 n)$.

```{.cpp file=segment_tree_smallest_number_greater2}
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

The constant $\text{INF}$ is equal to some large number that is bigger than all numbers in the array. 
Its usage means, that there is no number greater than or equal to $x$ in the segment. 
It has the meaning of "there is no answer in the given interval".

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

```{.cpp file=kth_smallest_persistent_segment_tree}
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

```{.cpp file=kth_smallest_persistent_segment_tree_build}
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

