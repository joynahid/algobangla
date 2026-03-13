# AlgoBangla — বাংলায় অ্যালগরিদম

[![Website](https://img.shields.io/badge/website-algobangla.com-blue)](https://algobangla.com)
[![Contributors](https://img.shields.io/github/contributors/wirestaq/algobangla.svg)](https://github.com/wirestaq/algobangla/graphs/contributors)
[![Pull Requests](https://img.shields.io/github/issues-pr/wirestaq/algobangla.svg)](https://github.com/wirestaq/algobangla/pulls)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

**AlgoBangla** হলো কম্পিটিটিভ প্রোগ্রামিং অ্যালগরিদম ও ডেটা স্ট্রাকচারের একটি বিনামূল্যের, বিজ্ঞাপনমুক্ত, দ্বিভাষিক রেফারেন্স — **বাংলা ও ইংরেজিতে**।

**AlgoBangla** is a free, ad-free, bilingual reference for competitive programming algorithms and data structures — in **Bangla and English**.

🌐 **Live:** [algobangla.com](https://algobangla.com)

---

## কেন AlgoBangla? / Why AlgoBangla?

বাংলাদেশ ও পশ্চিমবঙ্গের লক্ষ লক্ষ প্রোগ্রামার আছেন যারা বাংলায় চিন্তা করেন, কিন্তু বিশ্বমানের অ্যালগরিদম রিসোর্স শুধুই ইংরেজিতে। ঘন গাণিতিক ব্যাখ্যা দ্বিতীয় ভাষায় পড়া মানসিক শক্তি নষ্ট করে — সেই শক্তি অ্যালগরিদম বোঝায় খরচ হওয়া উচিত।

**AlgoBangla-র লক্ষ্য সেই বাধা দূর করা।** প্রতিটি আর্টিকেল যেন ভালো টেক্সটবুকের মতো পড়া যায় — স্পষ্ট, নির্ভুল, আর তোমার নিজের ভাষায়।

---

## কী কী আছে? / What's Covered

150+ আর্টিকেল, 13টি টপিক এরিয়ায়:

| টপিক | উদাহরণ |
|---|---|
| বীজগণিত ও সংখ্যাতত্ত্ব | বাইনারি এক্সপোনেনশিয়েশন, সিভ, FFT, CRT, অয়লারের টোশেন্ট... |
| গ্রাফ অ্যালগরিদম | BFS/DFS, ডায়াক্সট্রা, বেলম্যান-ফোর্ড, SCC, LCA, ম্যাক্স ফ্লো... |
| ডেটা স্ট্রাকচার | সেগমেন্ট ট্রি, ফেনউইক ট্রি, স্পার্স টেবিল, ট্রিপ, DSU... |
| ডায়নামিক প্রোগ্রামিং | LIS, ন্যাপস্যাক, D&C DP, নুথ'স অপ্টিমাইজেশন... |
| স্ট্রিং অ্যালগরিদম | KMP, Z-ফাংশন, আহো-কোরাসিক, সাফিক্স অ্যারে... |
| জ্যামিতি | কনভেক্স হাল, ডেলোনে ট্রায়াঙ্গুলেশন, হাফপ্লেন ইন্টারসেকশন... |
| কম্বিনেটরিক্স | দ্বিপদী সহগ, ক্যাটালান সংখ্যা, অন্তর্ভুক্তি-বর্জন... |
| রৈখিক বীজগণিত | গাউসিয়ান এলিমিনেশন, ডিটারমিন্যান্ট, র‍্যাঙ্ক... |
| সাংখ্যিক পদ্ধতি | বাইনারি সার্চ, টার্নারি সার্চ, নিউটনের পদ্ধতি... |
| গেম থিওরি | স্প্র্যাগ-গ্রুন্ডি উপপাদ্য, নিম... |
| সিকুয়েন্স | LIS, RMQ, MEX, k-তম অর্ডার স্ট্যাটিস্টিক... |
| শিডিউলিং | এক/দুই মেশিন শিডিউলিং... |
| অন্যান্য | ১৫-পাজল, জোসেফাস সমস্যা, স্টার্ন-ব্রকট ট্রি... |

প্রতিটি আর্টিকেল `/bn/` (বাংলা) ও `/en/` (ইংরেজি) উভয় ভাষায় পাওয়া যায়।

---

## টেক স্ট্যাক / Tech Stack

| কম্পোনেন্ট | টুল |
|---|---|
| সাইট জেনারেটর | [Hugo](https://gohugo.io) + [hugo-book](https://github.com/alex-shpak/hugo-book) থিম |
| হোস্টিং | Firebase Hosting (গ্লোবাল CDN) |
| CI/CD | GitHub Actions |
| গণিত রেন্ডারিং | MathJax 3 (সেল্ফ-হোস্টেড) |
| বাংলা ফন্ট | কালপুরুষ + Tiro Bangla (সেল্ফ-হোস্টেড) |
| কন্টেন্ট ফরম্যাট | Markdown + LaTeX |

রানটাইমে কোনো বাহ্যিক CDN নির্ভরতা নেই।

---

## কন্ট্রিবিউট করুন / Contribute

AlgoBangla একটি কমিউনিটি প্রজেক্ট। যেকোনো ধরনের অবদান স্বাগত:

- **অনুবাদ উন্নত করুন** — যদি কোনো বাংলা লেখা অস্বাভাবিক লাগে, ভালো সংস্করণ PR করুন
- **গাণিতিক পরিভাষা ঠিক করুন** — ছাত্ররা আসলে যে বাংলা ব্যবহার করে, সেটা ব্যবহার করুন
- **নতুন আর্টিকেল লিখুন** — বাংলায়, ইংরেজিতে, বা উভয়ভাষায়
- **সমস্যা রিপোর্ট করুন** — ভাঙা ফর্মুলা, ভুল লিংক, টাইপো

বিস্তারিত জানতে দেখুন: [CONTRIBUTING.md](CONTRIBUTING.md)

Git না জানলেও সমস্যা নেই। একটি [Issue](https://github.com/wirestaq/algobangla/issues) খুলুন। প্রতিটি আর্টিকেলের নিচে **"Edit this page on GitHub"** লিংক আছে।

---

## লোকাল ডেভেলপমেন্ট / Local Development

```bash
# রিপোজিটরি ক্লোন করুন
git clone https://github.com/wirestaq/algobangla.git
cd algobangla

# Hugo ইনস্টল করুন (v0.147+)
# https://gohugo.io/installation/

# ডেভ সার্ভার চালান
cd hugo
hugo server -D

# সাইট দেখুন: http://localhost:1313
```

---

## লাইসেন্স / License

সকল কন্টেন্ট [Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) লাইসেন্সের অধীনে।

মূল অ্যালগরিদম আর্টিকেলগুলো [cp-algorithms](https://cp-algorithms.com) কমিউনিটির কৃতিত্ব। বাংলা অনুবাদ ও অভিযোজন AlgoBangla কন্ট্রিবিউটরদের দ্বারা।

---

*বাংলা CP কমিউনিটির জন্য তৈরি। চিরকাল বিনামূল্যে।*
