---
search:
  exclude: true
---

# How to Contribute

Thanks for your interest in contributing to algobangla! Whether you want to fix a typo, improve a translation, or write a new article — all contributions are welcome. You just need a [GitHub account](https://github.com).

**Repository:** [github.com/wirestaq/algobangla](https://github.com/wirestaq/algobangla)
**Live site:** [algobangla.com](https://algobangla.com)

---

## Quick Start

1. Find the article you want to improve on [algobangla.com](https://algobangla.com)
2. Click the **"Edit this page on GitHub"** link at the bottom of the article
3. Edit the file on GitHub (you'll be asked to fork if it's your first time)
4. Commit your changes and create a **Pull Request**
5. It will be reviewed and merged

---

## Where to Contribute

### Improve Bangla Translations (Most Needed)

The translations are AI-assisted — accurate but not always natural. **Native speakers can make them significantly better.**

- Bangla content lives in: `hugo/content/bn/`
- Each article is a `.md` file
- Code blocks stay in English (C++ code is universal)
- Use the Bangla terminology that students actually use in practice

### Write New Articles

To add a new algorithm article:

1. Create an English file in `hugo/content/en/[section]/`
2. Create a Bangla file in `hugo/content/bn/[section]/` (same filename)
3. Add front matter to both files (see below)

### Report Issues

Found a problem? Open an [Issue](https://github.com/wirestaq/algobangla/issues):
- Broken formulas or rendering problems
- Incorrect information or code
- Dead links
- Typos

---

## Article Format

Articles are written in [Markdown](https://daringfireball.net/projects/markdown) and rendered with Hugo.

### Front Matter

Every article starts with:

```yaml
---
title: "Dijkstra Algorithm"
weight: 10
tags:
  - Translated
---
```

For Bangla articles:

```yaml
---
title: "ডায়াক্সট্রা অ্যালগরিদম"
weight: 10
---
```

### Math

We use [MathJax](https://www.mathjax.org/) with LaTeX syntax:

- Inline: `$a^n$`
- Block:
  ```
  $$
  d[v] = \min(d[v],\; d[u] + w(u, v))
  $$
  ```

**Important:** Leave an empty line before and after `$$` blocks.

### Code Blocks

C++ code blocks:

````markdown
```cpp
int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}
```
````

### Practice Problems

Add practice problems at the end of articles, ordered from easy to hard:

```markdown
## Practice Problems

- [CSES - Shortest Routes I](https://cses.fi/problemset/task/1671)
- [Codeforces - Dijkstra?](https://codeforces.com/problemset/problem/20/C)
```

---

## Bangla Writing Guidelines

When writing or editing Bangla content, follow these conventions:

### Terminology

| English | Bangla (preferred) | Avoid |
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

- **Transliterate common English terms** — don't force awkward Bangla translations
- On first use, include the English term in parentheses: "ভার্টেক্স (vertex)"
- Keep mathematical expressions in LaTeX: $O(n \log n)$

### Spelling and Punctuation

- Use Bangla dari (।) not English period (.)
- Write numbers in English digits (0-9) — keeps consistency with code
- In mixed English-Bangla sentences, maintain natural flow

---

## Project Structure

```
algobangla/
├── hugo/
│   ├── content/
│   │   ├── en/          # English articles
│   │   │   ├── algebra/
│   │   │   ├── graph/
│   │   │   └── ...
│   │   └── bn/          # Bangla articles
│   │       ├── algebra/
│   │       ├── graph/
│   │       └── ...
│   ├── static/          # Favicon, fonts, CSS, JS
│   ├── layouts/         # Template overrides
│   └── hugo.toml        # Hugo configuration
├── firebase.json        # Firebase hosting config
├── CONTRIBUTING.md      # This file
└── README.md
```

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

## Tags

Add tags to article front matter:

- **Original articles:**
  ```yaml
  tags:
    - Original
  ```

- **Translated articles:**
  ```yaml
  tags:
    - Translated
  ```

---

## License

By contributing, you agree that your contributions will be published under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

---

*Questions? Open an [Issue](https://github.com/wirestaq/algobangla/issues) or start a discussion.*
