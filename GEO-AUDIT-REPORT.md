# GEO Audit Report: algobangla.com

**Date:** 2026-03-13
**URL:** https://algobangla.com
**Business Type:** Educational Publisher (Competitive Programming Algorithms)
**Languages:** English + Bangla (Bengali)
**Total Pages:** ~688 (320 EN + 368 BN)
**Framework:** Hugo (Static Site Generation) + Cloudflare CDN

---

## Composite GEO Score: 43/100 [Poor]

| Category | Weight | Score | Weighted | Status |
|----------|--------|-------|----------|--------|
| AI Citability & Visibility | 25% | 38/100 | 9.5 | Poor |
| Brand Authority Signals | 20% | 8/100 | 1.6 | Critical |
| Content Quality & E-E-A-T | 20% | 42/100 | 8.4 | Poor |
| Technical Foundations | 15% | 86/100 | 12.9 | Good |
| Structured Data | 10% | 62/100 | 6.2 | Fair |
| Platform Optimization | 10% | 46/100 | 4.6 | Poor |
| **TOTAL** | **100%** | | **43.2** | **Poor** |

**Score Interpretation:**
- 0-20: Critical -- Invisible to AI search
- 21-40: Poor -- Minimal AI discoverability
- 41-60: Fair -- Some visibility, significant gaps
- 61-80: Good -- Solid presence, room for improvement
- 81-100: Excellent -- Strong AI search visibility

---

## AI Platform Readiness

| Platform | Score | Status |
|----------|-------|--------|
| Google AI Overviews | 52/100 | Fair |
| Google Gemini | 44/100 | Poor |
| Perplexity AI | 41/100 | Poor |
| ChatGPT Web Search | 38/100 | Poor |
| Bing Copilot | 37/100 | Poor |

---

## AI Crawler Access: 100/100 (Excellent)

| Crawler | Status |
|---------|--------|
| GPTBot (OpenAI) | Allowed |
| OAI-SearchBot (OpenAI) | Allowed |
| ChatGPT-User | Allowed |
| ClaudeBot (Anthropic) | Allowed |
| anthropic-ai | Allowed |
| PerplexityBot | Allowed |
| Google-Extended | Allowed |
| Googlebot | Allowed |
| Bingbot | Allowed |
| Amazonbot | Allowed |
| FacebookBot | Allowed |

The robots.txt is exemplary -- one of the most AI-friendly configurations possible. All major AI crawlers are explicitly allowed with `Allow: /`.

**Missing (recommended to add):** Bytespider, CCBot, Applebot-Extended, Cohere-ai

---

## Key Findings

### Critical Issues

1. **Site not indexed by Google or Bing.** `site:algobangla.com` returns zero results. No AI platform can cite content it cannot find in search indexes. Submit sitemap to Google Search Console and Bing Webmaster Tools immediately.

2. **Near-zero brand recognition (8/100).** AlgoBangla has no Wikipedia article, no Wikidata entry, no Reddit mentions, no YouTube presence, no LinkedIn page, and 0 GitHub stars/forks. AI models cannot recognize AlgoBangla as a legitimate entity without external corroborating signals.

3. **No privacy policy.** Google Analytics (G-KJT02RWWKZ) collects user data with no privacy disclosure. This is both a trust signal failure and a potential legal issue.

4. **Invalid `datePublished` in schema markup.** Every article emits `"datePublished": "0001-01-01T00:00:00Z"` -- a Hugo zero-value placeholder. Google will reject Article rich results.

### High Priority Issues

5. **No llms.txt file.** Both `/llms.txt` and `/llms-full.txt` return 404. This is a zero-cost, high-impact action.

6. **Content is derivative of cp-algorithms.com.** English content closely mirrors the upstream source. AI models already have cp-algorithms.com deeply embedded in training data. Minimal original value beyond translation.

7. **Zero visual content.** All sampled article pages have 0 images/diagrams. Algorithm content (especially graph algorithms like Dijkstra) benefits enormously from step-by-step visualizations.

8. **No author identity or credentials.** No named authors, no author bios, no Person schema. Author is listed as "cp-algorithms contributors" -- a collective with no verifiable expertise signals.

9. **Missing `image` property in TechArticle schema.** Required by Google for Article rich result eligibility.

10. **hreflang x-default hardcoded to `/bn/` (Bangla).** For a site with `defaultContentLanguage = "en"`, x-default should point to English.

### Medium Priority Issues

11. **Organization schema `sameAs` has only 1 link (GitHub).** Needs 3+ platforms (Wikipedia, LinkedIn, YouTube, etc.) for entity resolution.

12. **No question-based headings.** No "What is...?", "How does...?" H2/H3 headings that align with AI Overview snippet extraction patterns.

13. **Missing Content-Security-Policy header.** The only absent security header.

14. **Template-generated meta descriptions are non-unique.** 300+ articles share near-identical descriptions from a fallback template.

15. **No IndexNow protocol support.** Missing for Bing Copilot optimization.

16. **Bangla TechArticle descriptions fall back to English.** Language mismatch in schema for `/bn/` pages.

17. **No Course/LearningResource schema for section pages.** Educational content site should use educational schemas.

18. **MathJax loaded on every page.** ~1MB JS library parsed even on pages without math content.

### Low Priority Issues

19. **No RSS feed configured.** Hugo outputs restricted to HTML only.
20. **No resource hints** (`preconnect`, `preload`) for critical assets.
21. **4 render-blocking CSS files** without media attributes.
22. **SVG icons lack explicit dimensions** (minor CLS risk).
23. **No self-referencing hreflang tags.**
24. **GitHub sameAs URL still points to old `joynahid/algobangla`** (repo was transferred to `wirestaq/algobangla`).

---

## E-E-A-T Assessment: 30/100

| Dimension | Score | Key Issue |
|-----------|-------|-----------|
| Experience | 3/25 | No original research, case studies, or first-hand accounts |
| Expertise | 10/25 | Accurate content but no named authors or credentials |
| Authoritativeness | 5/25 | New domain, no external recognition, derivative content |
| Trustworthiness | 12/25 | HTTPS + CC license present, but no privacy policy or contact info |

---

## Citability Analysis: 61/100

Top citation-ready passages:

| Passage | Score |
|---------|-------|
| Binary Exponentiation opening definition | 78 |
| Binary Exponentiation recursive formulation | 74 |
| Z-Function definition with examples | 73 |
| Dijkstra relaxation formula block | 72 |
| Z-Function substring search application | 71 |

**Biggest citability weakness:** Content uniqueness. All English content closely mirrors cp-algorithms.com, which AI models already know well. The Bangla content is the genuine differentiator -- very few rigorous Bangla-language algorithm references exist.

---

## Schema Markup: 62/100

**Detected Schemas:**

| Schema | Pages | Status |
|--------|-------|--------|
| Organization | Homepage | Valid (gaps in sameAs) |
| WebSite + SearchAction | Homepage | Valid |
| TechArticle | All articles | Errors (datePublished invalid, missing image) |
| BreadcrumbList | All non-home | Valid |
| SpeakableSpecification | All articles | Valid |

**Missing Schemas:**
- Person (for authors/founder)
- Course/LearningResource (for section pages)
- FAQPage (for Q&A content opportunities)

**Critical Schema Fixes:**

### Fix datePublished (in `head.html` ~line 189)
```
{{- if not .Date.IsZero }}
"datePublished": {{ .Date.Format "2006-01-02T15:04:05Z07:00" | jsonify }},
{{- end }}
```

### Add image to TechArticle
```json
"image": {
  "@type": "ImageObject",
  "url": "https://algobangla.com/algobangla-social.png",
  "width": 1200,
  "height": 630
}
```

### Fix hreflang x-default (~line 128)
Change `href="https://algobangla.com/bn/"` to `href="https://algobangla.com/en/"`

### Update Organization sameAs
Update GitHub URL from `joynahid/algobangla` to `wirestaq/algobangla` and add additional platform links.

---

## Technical Foundations: 86/100

**Strengths:**
- Hugo SSG = perfect server-side rendering (100/100)
- Clean URL structure: `/{lang}/{section}/{topic}/`
- Comprehensive sitemap with i18n separation (658 URLs)
- Strong security headers (HSTS, X-Frame-Options, Referrer-Policy, Permissions-Policy)
- Proper canonical tags (self-referencing)
- Mobile-responsive design with dark mode support
- All scripts `defer`/`async` -- no render-blocking JS

**Weaknesses:**
- Missing Content-Security-Policy header (-10)
- MathJax causes CLS risk on math-heavy pages
- 4 render-blocking CSS files without media attributes
- No resource hints for critical assets
- Cloudflare edge caching not enabled (cf-cache-status: DYNAMIC)

---

## Prioritized Action Plan

### Quick Wins (Low Effort, High Impact)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Submit sitemap to Google Search Console & Bing Webmaster Tools | Critical | 30 min |
| 2 | Fix `datePublished` zero-value in schema template | Critical | 10 min |
| 3 | Create and deploy `/llms.txt` | High | 30 min |
| 4 | Add privacy policy page | High | 1 hr |
| 5 | Create Wikidata entry for AlgoBangla | High | 1 hr |
| 6 | Fix hreflang x-default to point to `/en/` | Medium | 5 min |
| 7 | Add `image` property to TechArticle schema | High | 15 min |
| 8 | Update Organization sameAs (fix GitHub URL to wirestaq) | Medium | 10 min |
| 9 | Create LinkedIn company page | Medium | 30 min |
| 10 | Implement IndexNow for Bing | Medium | 1 hr |

### Medium-Term (Medium Effort, High Impact)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 11 | Add algorithm visualization diagrams (SVG) to top 20 articles | High | 2-3 weeks |
| 12 | Add question-based H2 headings + 40-60 word answer blocks | High | 1 week |
| 13 | Create author profiles with CP credentials + Person schema | High | 1-2 days |
| 14 | Add Course schema for section pages | Medium | 2 hrs |
| 15 | Seed Reddit/Codeforces community discussions | High | Ongoing |
| 16 | Add contextual internal links within article body text | Medium | 1 week |
| 17 | Write unique meta descriptions for top 50 pages | Medium | 1 day |
| 18 | Add CSP header via Cloudflare | Medium | 1 hr |
| 19 | Enable Cloudflare edge caching | Medium | 30 min |
| 20 | Add visible "Last updated" dates to article templates | Medium | 1 hr |

### Strategic (High Effort, Transformative Impact)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 21 | Create original Bangla-first content (BdOI problems, common mistakes, intuition sections) | Transformative | Ongoing |
| 22 | Create YouTube channel with Bangla algorithm explanations | Transformative | Ongoing |
| 23 | Write original problem editorials (3-5 per article) | High | Ongoing |
| 24 | Add comparison tables (Dijkstra vs Bellman-Ford vs Floyd-Warshall, etc.) | High | 1-2 weeks |
| 25 | Investigate server-side math rendering (KaTeX SSR) | Medium | 1 week |
| 26 | Pursue Wikipedia article for AlgoBangla | High | Long-term |

---

## Recommended llms.txt

```
# AlgoBangla

> Bilingual (English + Bangla) competitive programming algorithms reference. 150+ algorithms with complexity analysis, mathematical proofs, C++ implementations, and practice problems. Based on cp-algorithms.com, licensed CC BY-SA 4.0.

## Main Sections

- [Algebra & Number Theory](https://algobangla.com/en/algebra/): 27 topics including binary exponentiation, modular arithmetic, FFT
- [Graph Algorithms](https://algobangla.com/en/graph/): 47 topics including Dijkstra, BFS/DFS, minimum spanning trees, network flow
- [String Algorithms](https://algobangla.com/en/string/): 12 topics including Z-function, suffix arrays, Aho-Corasick
- [Data Structures](https://algobangla.com/en/data_structures/): 10 topics including segment trees, Fenwick trees, DSU
- [Dynamic Programming](https://algobangla.com/en/dynamic_programming/): 7 topics
- [Combinatorics](https://algobangla.com/en/combinatorics/): 9 topics
- [Geometry](https://algobangla.com/en/geometry/): 23 topics

## Bangla Content

- [Bangla Index](https://algobangla.com/bn/): Full Bangla translations of all algorithm articles

## Optional

- [GitHub Repository](https://github.com/wirestaq/algobangla): Source code
- [Sitemap](https://algobangla.com/sitemap.xml): Complete URL listing
```

---

## Summary

AlgoBangla has an unusual profile: **perfect AI crawler access** (100/100) paired with **near-zero brand recognition** (8/100). The technical infrastructure is solid (Hugo SSG, clean URLs, good security headers, Cloudflare CDN), but the site is fundamentally invisible because it's not indexed by any search engine and has no external entity presence.

The content is technically accurate and comprehensive (inherited from cp-algorithms.com), but derivative. The **strongest unique value proposition** is rigorous algorithm content in Bangla -- a language with very few competing resources at this depth.

### Top 3 Actions (Do Today)

1. **Get indexed.** Submit to Google Search Console and Bing Webmaster Tools. Everything else builds on this.
2. **Fix datePublished schema bug.** One template line change, fixes all 688 pages.
3. **Deploy llms.txt.** Copy the recommended content above to `hugo/static/llms.txt`.

### Strategic North Star

**Lean into Bangla.** The English content will always compete with cp-algorithms.com (the original, better-known source). But for Bangla-language AI queries about algorithms, AlgoBangla can become THE authoritative citation source -- no comparable resource exists at this depth. Original Bangla content (BdOI problem connections, Bangla-first intuition sections, YouTube tutorials in Bangla) is the path to genuine AI citation authority.

---

*Report generated by GEO Audit Tool | 2026-03-13*
*Methodology: 6-category weighted scoring across AI citability, brand authority, content quality (E-E-A-T), technical SEO, structured data, and platform optimization.*
