# AlgoBangla — Bengali Wikipedia Article Draft: Summary

## Article Overview

**Article title:** অ্যালগোবাংলা (AlgoBangla)
**Target Wikipedia:** Bengali Wikipedia (bn.wikipedia.org)
**Draft file:** `WIKIPEDIA-DRAFT-bn.wiki`

---

## What the Article Covers

### Introduction
AlgoBangla (অ্যালগোবাংলা) is a free, ad-free, volunteer-run bilingual educational website providing Bengali and English articles on competitive programming algorithms and data structures. It is hosted at https://algobangla.web.app and is an adaptation/translation of cp-algorithms.com (which itself adapted e-maxx.ru/algo). Published under CC BY-SA 4.0.

### Background (পটভূমি)
- Bangladesh has a large, active competitive programming community — regular ICPC World Finals participants, strong Codeforces presence.
- Despite this, no structured, comprehensive Bangla-language algorithm reference existed before AlgoBangla.
- AlgoBangla fills this gap by adapting the content lineage: e-maxx.ru/algo (Russian) → cp-algorithms.com (English) → AlgoBangla (Bangla).

### Content (বিষয়বস্তু)
150+ articles across 10 topic categories:
1. Algebra & Number Theory — modular arithmetic, binary exponentiation, Euler's sieve, FFT, etc.
2. Graph Algorithms — BFS, DFS, Dijkstra, Bellman-Ford, MST, SCC, max-flow, LCA, etc.
3. Data Structures — Segment Tree, Fenwick Tree, Sparse Table, Treap, DSU, etc.
4. Dynamic Programming — LIS, divide-and-conquer DP, Knuth optimization, profile DP, Knapsack, etc.
5. Geometry — convex hull, segment intersection, polygon area, Delaunay triangulation, etc.
6. String Algorithms — prefix function, Z-function, KMP, Aho-Corasick, suffix array, suffix automaton, Manacher, etc.
7. Combinatorics — binomial coefficients, Catalan numbers, inclusion-exclusion, Burnside, etc.
8. Linear Algebra — Gaussian elimination, determinants, Kraut's algorithm, etc.
9. Numerical Methods — binary search, ternary search, Newton's method, Simpson integration, simulated annealing, etc.
10. Game Theory — Sprague-Grundy theorem, Nim, games on graphs, etc.

### Technology (প্রযুক্তি)
- Static site generator: Hugo with hugo-book theme
- Hosting: Google Firebase (https://algobangla.web.app)
- Source code: Open on GitHub at https://github.com/joynahid/algobangla
- CI/CD: GitHub Actions for automatic build and deployment
- Content format: Markdown with LaTeX math rendering
- Completely ad-free, volunteer-run

### License (লাইসেন্স)
CC BY-SA 4.0. Adapted from cp-algorithms.com. Original content credits: e-maxx/ru.maxx project and the cp-algorithms community.

---

## Wikipedia Conventions Used

- **Infobox:** `{{তথ্যছক ওয়েবসাইট}}` — standard Bengali Wikipedia website infobox
- **References:** `{{ওয়েব উদ্ধৃতি}}` — standard web citation template, citing the site itself, GitHub, cp-algorithms.com, and e-maxx.ru
- **Section headings:** Standard Bengali Wikipedia `== heading ==` format with Bangla headings
- **English terms:** Transliterated into Bangla script with English in parentheses where needed (following bn.wikipedia.org convention observed in the অ্যালগরিদম article)
- **Terminology:** NCTB-style Bangla mathematical terminology used (e.g., কলনবিধি for algorithm, সংখ্যা তত্ত্ব for number theory, রৈখিক বীজগণিত for linear algebra)
- **Tone:** Encyclopedic, neutral, formal Bangla — not a literal word-for-word English translation

## Notability Argument

AlgoBangla is notable as the **first structured, comprehensive Bangla-language resource for competitive programming algorithms**. This is significant given:
- Bangladesh has a large competitive programming community with ICPC World Finals history
- Strong Codeforces and regional olympiad participation by Bangla-speaking programmers
- No equivalent native-language reference existed before this project
- The site covers 150+ articles spanning 10 major topic areas, making it encyclopedic in scope

## Categories Added
- বিষয়শ্রেণী:প্রোগ্রামিং
- বিষয়শ্রেণী:শিক্ষামূলক ওয়েবসাইট
- বিষয়শ্রেণী:বাংলাদেশের ওয়েবসাইট
- বিষয়শ্রেণী:অ্যালগরিদম
- বিষয়শ্রেণী:মুক্ত শিক্ষা
- বিষয়শ্রেণী:২০২৬-এ প্রতিষ্ঠিত ওয়েবসাইট

---

## Source Research Notes

- Observed Bengali Wikipedia article style from: bn.wikipedia.org/wiki/অ্যালগরিদম
- Bengali Wikipedia uses transliteration of English tech terms in Bangla script, with English originals in parentheses
- Section headings: সম্পাদনা-linked headings, standard == == format
- References use {{ওয়েব উদ্ধৃতি}} template with named params
- Categories use [[বিষয়শ্রেণী:...]] syntax
- Project launch date: March 2026 (based on git commit history: first Bangla translation commits dated 2026-03-11, Firebase deployment 2026-03-12)
- Article count per section: Algebra (~31), Graph (~46), Data Structures (~11), Strings (~13), plus others
