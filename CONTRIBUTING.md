---
search:
  exclude: true
---

# কন্ট্রিবিউশন গাইড / How to Contribute

AlgoBangla-তে কন্ট্রিবিউট করতে চাওয়ার জন্য ধন্যবাদ! টাইপো ঠিক করা থেকে শুরু করে নতুন আর্টিকেল লেখা — সবধরনের অবদান স্বাগত। শুধু একটি [GitHub অ্যাকাউন্ট](https://github.com) দরকার।

📂 **রিপোজিটরি:** [github.com/wirestaq/algobangla](https://github.com/wirestaq/algobangla)
🌐 **লাইভ সাইট:** [algobangla.com](https://algobangla.com)

---

## দ্রুত শুরু / Quick Start

1. যে আর্টিকেলটি উন্নত করতে চান সেটি খুঁজুন — [algobangla.com](https://algobangla.com)-এ যান
2. আর্টিকেলের নিচে **"Edit this page on GitHub"** লিংকে ক্লিক করুন
3. GitHub-এ ফাইলটি এডিট করুন (প্রথমবার হলে fork করতে বলবে)
4. পরিবর্তনগুলো commit করুন এবং **Pull Request** তৈরি করুন
5. রিভিউ হবে এবং মার্জ করা হবে

---

## কোথায় কন্ট্রিবিউট করবেন? / Where to Contribute

### বাংলা অনুবাদ উন্নত করা (সবচেয়ে প্রয়োজন)

অনুবাদগুলো AI-সহায়তায় করা হয়েছে — নির্ভুল, কিন্তু সবসময় স্বাভাবিক নয়। **বাংলা মাতৃভাষী হিসেবে আপনি এগুলো অনেক ভালো করতে পারেন।**

- বাংলা কন্টেন্ট আছে: `hugo/content/bn/` ফোল্ডারে
- প্রতিটি আর্টিকেল একটি `.md` ফাইল
- কোড ব্লক ইংরেজিতেই থাকবে (C++ কোড ইউনিভার্সাল)
- গাণিতিক পরিভাষায় ছাত্ররা আসলে যা ব্যবহার করে, সেটা অনুসরণ করুন

### নতুন আর্টিকেল যোগ করা

নতুন অ্যালগরিদম আর্টিকেল যোগ করতে:

1. `hugo/content/en/[section]/` ফোল্ডারে ইংরেজি ফাইল তৈরি করুন
2. `hugo/content/bn/[section]/` ফোল্ডারে বাংলা ফাইল তৈরি করুন (একই ফাইলনাম)
3. উভয় ফাইলে front matter যোগ করুন (নিচে দেখুন)

### সমস্যা রিপোর্ট করা

ভুল পেলে একটি [Issue](https://github.com/wirestaq/algobangla/issues) খুলুন:
- ভাঙা ফর্মুলা বা রেন্ডারিং সমস্যা
- ভুল তথ্য বা কোড
- মৃত লিংক
- টাইপো

---

## আর্টিকেল ফরম্যাট / Article Format

আর্টিকেলগুলো [Markdown](https://daringfireball.net/projects/markdown) ফরম্যাটে লেখা, Hugo দিয়ে রেন্ডার করা হয়।

### Front Matter

প্রতিটি আর্টিকেলের শুরুতে:

```yaml
---
title: "Dijkstra Algorithm"
weight: 10
tags:
  - Translated
---
```

বাংলা আর্টিকেলের জন্য:

```yaml
---
title: "ডায়াক্সট্রা অ্যালগরিদম"
weight: 10
---
```

### গণিত / Math

[MathJax](https://www.mathjax.org/) ব্যবহার করা হয়। LaTeX সিনট্যাক্স:

- ইনলাইন: `$a^n$` → $a^n$
- ব্লক:
  ```
  $$
  d[v] = \min(d[v],\; d[u] + w(u, v))
  $$
  ```

**গুরুত্বপূর্ণ:** `$$` ব্লকের আগে ও পরে একটি ফাঁকা লাইন রাখুন।

### কোড ব্লক

C++ কোড ব্লক:

````markdown
```cpp
int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}
```
````

### প্র্যাকটিস প্রবলেম

আর্টিকেলের শেষে প্র্যাকটিস প্রবলেম যোগ করুন:

```markdown
## Practice Problems

- [CSES - Shortest Routes I](https://cses.fi/problemset/task/1671)
- [Codeforces - Dijkstra?](https://codeforces.com/problemset/problem/20/C)
```

প্রবলেমগুলো সহজ থেকে কঠিন ক্রমে সাজান।

---

## বাংলা লেখার নিয়মাবলি / Bangla Writing Guidelines

AlgoBangla-তে বাংলা লেখার সময় এই নিয়মগুলো অনুসরণ করুন:

### পরিভাষা

| ইংরেজি | বাংলা (ব্যবহার করুন) | পরিহার করুন |
|---|---|---|
| Algorithm | অ্যালগরিদম | এলগরিদম |
| Vertex / Node | ভার্টেক্স / নোড | শীর্ষবিন্দু |
| Edge | এজ | ধার / প্রান্ত |
| Graph | গ্রাফ | লেখচিত্র |
| Array | অ্যারে | বিন্যাস |
| Complexity | জটিলতা | — |
| Tree | ট্রি | বৃক্ষ |
| Queue | কিউ | — |
| Stack | স্ট্যাক | — |

- **প্রচলিত ইংরেজি টার্ম** transliterate করুন, জোর করে বাংলা করবেন না
- প্রথমবার ব্যবহারে ইংরেজি মূল শব্দটি বন্ধনীতে দিন: "ভার্টেক্স (vertex)"
- $O(n \log n)$ এর মতো গাণিতিক প্রকাশ LaTeX-এই রাখুন

### বানান ও বিরামচিহ্ন

- বাংলা দাঁড়ি (।) ব্যবহার করুন, পিরিয়ড (.) নয়
- সংখ্যা ইংরেজি অঙ্কেই (0-9) লিখুন — কোডের সাথে সামঞ্জস্য রাখতে
- ইংরেজি-বাংলা মিশ্র বাক্যে স্বাভাবিক ফ্লো বজায় রাখুন

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

# ব্রাউজারে দেখুন: http://localhost:1313
```

### প্রজেক্ট স্ট্রাকচার

```
algobangla/
├── hugo/
│   ├── content/
│   │   ├── en/          # ইংরেজি আর্টিকেল
│   │   │   ├── algebra/
│   │   │   ├── graph/
│   │   │   └── ...
│   │   └── bn/          # বাংলা আর্টিকেল
│   │       ├── algebra/
│   │       ├── graph/
│   │       └── ...
│   ├── static/          # ফেভিকন, ফন্ট, CSS, JS
│   ├── layouts/         # টেমপ্লেট ওভাররাইড
│   └── hugo.toml        # Hugo কনফিগারেশন
├── firebase.json        # Firebase হোস্টিং কনফিগ
├── CONTRIBUTING.md      # এই ফাইল
└── README.md
```

---

## ট্যাগ / Tags

আর্টিকেলের front matter-এ ট্যাগ যোগ করুন:

- **মূল আর্টিকেল:**
  ```yaml
  tags:
    - Original
  ```

- **অনূদিত আর্টিকেল:**
  ```yaml
  tags:
    - Translated
  ```

---

## লাইসেন্স / License

কন্ট্রিবিউট করলে আপনি সম্মত হচ্ছেন যে আপনার অবদান [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) লাইসেন্সের অধীনে প্রকাশিত হবে।

---

*প্রশ্ন? [Issue](https://github.com/wirestaq/algobangla/issues) খুলুন অথবা discussion-এ জানান।*
