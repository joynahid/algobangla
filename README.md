# algobangla

[![Website](https://img.shields.io/badge/website-algobangla.com-blue)](https://algobangla.com)
[![Contributors](https://img.shields.io/github/contributors/wirestaq/algobangla.svg)](https://github.com/wirestaq/algobangla/graphs/contributors)
[![Pull Requests](https://img.shields.io/github/issues-pr/wirestaq/algobangla.svg)](https://github.com/wirestaq/algobangla/pulls)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

**algobangla** is a free, ad-free, bilingual reference for competitive programming algorithms and data structures — in **Bangla and English**.

It is a Bangla adaptation of [cp-algorithms.com](https://cp-algorithms.com), built to make world-class algorithm knowledge accessible to Bangladeshi students and programmers in their own language.

**Live site:** [algobangla.com](https://algobangla.com)

---

## Why

Bangladesh regularly qualifies for ICPC World Finals. Hundreds of thousands of Bangladeshi programmers compete on Codeforces, AtCoder, and LeetCode. Yet no comprehensive algorithm reference existed in Bangla.

English is a barrier — not because people can't read it, but because parsing dense mathematical explanations in a second language costs mental energy. That energy should go toward understanding algorithms, not decoding language.

**algobangla eliminates that barrier.** Every article reads like a good textbook — clear, precise, and in the language you think in.

---

## What's Covered

150+ articles across 13 topic areas:

| Topic | Examples |
|---|---|
| Algebra & Number Theory | Binary exponentiation, Sieve, FFT, CRT, Euler's totient... |
| Graph Algorithms | BFS/DFS, Dijkstra, Bellman-Ford, SCC, LCA, Max flow (Dinic, Push-Relabel)... |
| Data Structures | Segment Tree, Fenwick Tree, Sparse Table, Treap, DSU, sqrt decomposition... |
| Dynamic Programming | LIS, Knapsack, D&C DP, Knuth's optimization, Profile DP... |
| String Algorithms | KMP, Z-function, Aho-Corasick, Suffix Array, Suffix Automaton, Manacher... |
| Geometry | Convex Hull, halfplane intersection, Delaunay triangulation... |
| Combinatorics | Binomial coefficients, Catalan numbers, inclusion-exclusion, Burnside... |
| Linear Algebra | Gaussian elimination, Determinant, Rank... |
| Numerical Methods | Binary search, Ternary search, Newton's method, Simpson integration... |
| Game Theory | Sprague-Grundy theorem, Nim, Games on graphs... |
| Sequences | LIS, RMQ, MEX, k-th order statistics... |
| Schedules | Single/two-machine scheduling... |
| Others | 15-puzzle, Josephus problem, Stern-Brocot tree... |

Every article is available at `/bn/` (Bangla) and `/en/` (English).

---

## Tech Stack

| Component | Tool |
|---|---|
| Site generator | [Hugo](https://gohugo.io) + [hugo-book](https://github.com/alex-shpak/hugo-book) theme |
| Hosting | Firebase Hosting (global CDN) |
| CI/CD | GitHub Actions |
| Math rendering | MathJax 3 (self-hosted) |
| Bangla fonts | Kalpurush + Tiro Bangla (self-hosted) |
| Content format | Markdown + LaTeX |

Zero external CDN dependencies at runtime.

---

## Contribute

The translations are AI-assisted — accurate but not always natural. **Native Bangla speakers can make them significantly better.**

Ways to contribute:

- **Fix a translation** — if something reads awkwardly, open a PR with a better version
- **Improve math terminology** — use clear, natural Bangla that students actually use
- **Write a new article** — in Bangla, English, or both
- **Report issues** — broken formulas, wrong links, typos

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

You don't need to know Git. Open an [Issue](https://github.com/wirestaq/algobangla/issues) and describe what you want to fix. Every article has an **"Edit this page on GitHub"** link at the bottom.

---

## Local Development

```bash
git clone https://github.com/wirestaq/algobangla.git
cd algobangla

# Install Hugo (v0.147+)
# https://gohugo.io/installation/

cd hugo
hugo server -D

# Open http://localhost:1313
```

---

## License

All content is licensed under [Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

Original algorithm articles are credited to the [cp-algorithms](https://cp-algorithms.com) community. Bangla translations and adaptations are by algobangla contributors.

---

*Built for the Bangladeshi CP community. Free forever.*
