# AlgoBangla — বাংলায় CP Algorithms

[![Website](https://img.shields.io/badge/website-algobangla.web.app-blue)](https://algobangla.web.app)
[![Contributors](https://img.shields.io/github/contributors/joynahid/algobangla.svg)](https://github.com/joynahid/algobangla/graphs/contributors)
[![Pull Requests](https://img.shields.io/github/issues-pr/joynahid/algobangla.svg)](https://github.com/joynahid/algobangla/pulls)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Build](https://img.shields.io/github/actions/workflow/status/joynahid/algobangla/deploy-hugo.yml)](https://github.com/joynahid/algobangla/actions)

**AlgoBangla** is a free, ad-free, bilingual reference for competitive programming algorithms and data structures — in **Bangla and English**.

It is a Bangla adaptation of [cp-algorithms.com](https://cp-algorithms.com), which itself is based on the legendary Russian resource [e-maxx.ru/algo](https://e-maxx.ru/algo). The goal is simple: make world-class algorithm knowledge accessible to the millions of Bengali-speaking students and programmers who think and learn best in their first language.

🌐 **Live site:** [algobangla.com](https://algobangla.com)

---

## Vision

There are hundreds of thousands of Bengali-speaking competitive programmers in Bangladesh and West Bengal. Bangladesh regularly qualifies for ICPC World Finals. Yet no comprehensive, well-organized algorithm reference existed in Bangla.

English is a barrier — not because people can't read it, but because parsing dense mathematical explanations in a second language costs mental energy. That energy should go toward understanding algorithms, not decoding language.

**AlgoBangla's vision is to eliminate that barrier entirely.** Every article should read as naturally as a good textbook — clear, precise, and written in the language you think in.

---

## What's Covered

150+ articles across 13 topic areas:

| Topic | Articles |
|---|---|
| Algebra & Number Theory | Binary exponentiation, Sieve, FFT, CRT, Discrete log, Euler's totient... |
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

- **Generator:** [Hugo](https://gohugo.io) with [hugo-book](https://github.com/alex-shpak/hugo-book) theme
- **Hosting:** Firebase Hosting (global CDN)
- **CI/CD:** GitHub Actions — auto-deploys on every push to `hugo` branch
- **Math:** MathJax 3 (self-hosted)
- **Fonts:** Kalpurush + Tiro Bangla (self-hosted)
- **Content:** Markdown with LaTeX math

Zero external CDN dependencies at runtime.

---

## Contribute

The translations are AI-assisted — accurate but not always natural. **Native speakers can make them significantly better.**

Ways to contribute:

- **Fix a translation** — if something reads awkwardly, open a PR with a better version
- **Improve math terminology** — use clear, natural Bangla that students actually use
- **Write a new article** — in Bangla, English, or both
- **Report issues** — broken formulas, wrong links, typos

You don't need to know Git to get started. Open an [Issue](https://github.com/joynahid/algobangla/issues) and describe what you want to fix.

Every article has an **"Edit this page on GitHub"** link at the bottom.

---

## License

All content is licensed under [Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

Original algorithm articles are credited to the [e-maxx / cp-algorithms](https://cp-algorithms.com) community. Bangla translations and adaptations are by AlgoBangla contributors.

---

*Built for the Bengali CP community. Free forever.*
