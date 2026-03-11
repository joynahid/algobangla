---
tags:
  - Translated
e_maxx_link: voronoi_diagram_2d_n4
---

# ডেলোনে ট্রায়াঙ্গুলেশন এবং ভরোনয় ডায়াগ্রাম

সমতলে বিন্দুর একটি সেট $\{p_i\}$ বিবেচনা করুন।
$\{p_i\}$-র একটি **ভরোনয় ডায়াগ্রাম** $V(\{p_i\})$ হলো সমতলের $n$ টি অঞ্চল $V_i$-তে বিভাজন, যেখানে $V_i = \{p\in\mathbb{R}^2;\ \rho(p, p_i) = \min\ \rho(p, p_k)\}$।
ভরোনয় ডায়াগ্রামের ঘরগুলো পলিগন (সম্ভবত অসীম)।
$\{p_i\}$-র একটি **ডেলোনে ট্রায়াঙ্গুলেশন** $D(\{p_i\})$ হলো এমন একটি ট্রায়াঙ্গুলেশন যেখানে প্রতিটি বিন্দু $p_i$ প্রতিটি ত্রিভুজ $T \in D(\{p_i\})$-র পরিবৃত্তের বাইরে বা সীমানায় থাকে।

একটি বিরক্তিকর অবক্ষয়িত ক্ষেত্র আছে যখন ভরোনয় ডায়াগ্রাম সংযুক্ত নয় এবং ডেলোনে ট্রায়াঙ্গুলেশন বিদ্যমান নেই। এই ক্ষেত্রটি হলো যখন সব বিন্দু সমরেখ।

## ধর্মসমূহ

ডেলোনে ট্রায়াঙ্গুলেশন সব সম্ভাব্য ট্রায়াঙ্গুলেশনের মধ্যে ন্যূনতম কোণকে সর্বাধিক করে।

একটি বিন্দু সেটের মিনিমাম ইউক্লিডীয় স্প্যানিং ট্রি এর ডেলোনে ট্রায়াঙ্গুলেশনের এজের একটি সাবসেট।

## দ্বৈততা

ধরুন $\{p_i\}$ সমরেখ নয় এবং $\{p_i\}$-র মধ্যে কোনো চারটি বিন্দু একটি বৃত্তে নেই। তাহলে $V(\{p_i\})$ ও $D(\{p_i\})$ দ্বৈত, তাই যদি আমরা একটি পাই, অন্যটি $O(n)$-এ পেতে পারি। এমন না হলে কী করতে হবে? সমরেখ ক্ষেত্র সহজেই প্রসেস করা যায়। অন্যথায়, $V$ ও $D'$ দ্বৈত, যেখানে $D'$ হলো $D$ থেকে সেই সব এজ সরিয়ে পাওয়া যায় যেখানে এজের দুই পাশের ত্রিভুজ পরিবৃত্ত ভাগ করে।

## ডেলোনে ও ভরোনয় নির্মাণ

দ্বৈততার কারণে, আমাদের কেবল $V$ ও $D$-র একটি দ্রুত হিসাব করার অ্যালগরিদম প্রয়োজন। আমরা বর্ণনা করব কীভাবে $D(\{p_i\})$ $O(n\log n)$-এ তৈরি করা যায়। ট্রায়াঙ্গুলেশন Guibas ও Stolfi-র ডিভাইড অ্যান্ড কনকার অ্যালগরিদম দিয়ে তৈরি হবে।

## কোয়াড-এজ ডেটা স্ট্রাকচার

অ্যালগরিদম চলাকালীন $D$ কোয়াড-এজ ডেটা স্ট্রাকচারে সংরক্ষিত থাকবে। এই স্ট্রাকচার চিত্রে বর্ণিত:
<div style="text-align: center;">
  <img src="quad-edge.png" alt="Quad-Edge">
</div>

অ্যালগরিদমে আমরা এজের উপর নিম্নলিখিত ফাংশনগুলো ব্যবহার করব:

  ১. `make_edge(a, b)`<br>
    এই ফাংশনটি বিন্দু `a` থেকে বিন্দু `b`-তে একটি বিচ্ছিন্ন এজ তৈরি করে এর বিপরীত এজ এবং উভয় ডুয়াল এজসহ।
  ২. `splice(a, b)`<br>
    এটি অ্যালগরিদমের একটি মূল ফাংশন। এটি `a->Onext`-কে `b->Onext` এবং `a->Onext->Rot->Onext`-কে `b->Onext->Rot->Onext`-এর সাথে অদলবদল করে।
  ৩. `delete_edge(e)`<br>
    এই ফাংশনটি ট্রায়াঙ্গুলেশন থেকে e মুছে দেয়। `e` মুছতে, আমরা কেবল `splice(e, e->Oprev)` এবং `splice(e->Rev, e->Rev->Oprev)` কল করি।
  ৪. `connect(a, b)`<br>
    এই ফাংশনটি `a->Dest` থেকে `b->Org`-তে একটি নতুন এজ `e` তৈরি করে এমনভাবে যে `a`, `b`, `e` সবার একই বাম ফেস থাকে। এটি করতে, আমরা `e = make_edge(a->Dest, b->Org)`, `splice(e, a->Lnext)` এবং `splice(e->Rev, b)` কল করি।

## অ্যালগরিদম

অ্যালগরিদমটি ট্রায়াঙ্গুলেশন হিসাব করবে এবং দুটি কোয়াড-এজ রিটার্ন করবে: সবচেয়ে বামের ভার্টেক্স থেকে ঘড়ির কাঁটার বিপরীত কনভেক্স হাল এজ এবং সবচেয়ে ডানের ভার্টেক্স থেকে ঘড়ির কাঁটার দিকে কনভেক্স হাল এজ।

আসুন সব বিন্দু x অনুসারে সাজাই, এবং যদি $x_1 = x_2$ তাহলে y অনুসারে। আসুন কোনো সেগমেন্ট $(l, r)$-র জন্য সমস্যা সমাধান করি (প্রাথমিকভাবে $(l, r) = (0, n - 1)$)। যদি $r - l + 1 = 2$ হয়, আমরা একটি এজ $(p[l], p[r])$ যোগ করব এবং রিটার্ন করব। যদি $r - l + 1 = 3$ হয়, আমরা প্রথমে এজ $(p[l], p[l + 1])$ এবং $(p[l + 1], p[r])$ যোগ করব। এগুলো `splice(a->Rev, b)` ব্যবহার করে সংযুক্ত করতে হবে। এখন আমাদের ত্রিভুজ বন্ধ করতে হবে। পরবর্তী ক্রিয়া $p[l], p[l + 1], p[r]$-র অরিয়েন্টেশনের উপর নির্ভর করবে। সমরেখ হলে ত্রিভুজ তৈরি করা যায় না, তাই কেবল `(a, b->Rev)` রিটার্ন করি। অন্যথায়, `connect(b, a)` কল করে একটি নতুন এজ `c` তৈরি করি। বিন্দুগুলো ঘড়ির কাঁটার বিপরীতে থাকলে, `(a, b->Rev)` রিটার্ন করি। অন্যথায় `(c->Rev, c)` রিটার্ন করি।

এখন ধরি $r - l + 1 \ge 4$। প্রথমে, আসুন $L = (l, \frac{l + r}{2})$ এবং $R = (\frac{l + r}{2} + 1, r)$ রিকার্সিভভাবে সমাধান করি। এখন আমাদের এই ট্রায়াঙ্গুলেশনগুলো একটিতে মার্জ করতে হবে। লক্ষ্য করুন আমাদের বিন্দুগুলো সাজানো, তাই মার্জ করার সময় আমরা L থেকে R-তে এজ যোগ করব (তথাকথিত _ক্রস_ এজ) এবং L থেকে L এবং R থেকে R-তে কিছু এজ সরাব।
ক্রস এজের গঠন কেমন? এই সব এজকে y-অক্ষের সমান্তরাল একটি রেখা অতিক্রম করতে হবে যা স্প্লিটিং x মানে স্থাপিত। এটি ক্রস এজগুলোর একটি লিনিয়ার ক্রম স্থাপন করে, তাই আমরা পরপর ক্রস এজ, সবচেয়ে নিচের ক্রস এজ ইত্যাদি নিয়ে কথা বলতে পারি। অ্যালগরিদম ক্রস এজগুলো ক্রমবর্ধমান ক্রমে যোগ করবে। লক্ষ্য করুন যেকোনো দুটি সংলগ্ন ক্রস এজের একটি সাধারণ প্রান্তবিন্দু থাকবে, এবং তাদের সংজ্ঞায়িত ত্রিভুজের তৃতীয় বাহু L থেকে L-তে বা R থেকে R-তে যায়। আসুন বর্তমান ক্রস এজকে বেস বলি। বেসের পরবর্তী হবে হয় বেসের বাম প্রান্তবিন্দু থেকে ডান প্রান্তবিন্দুর R-প্রতিবেশীদের একটিতে অথবা বিপরীতভাবে।
বেস এবং পূর্ববর্তী ক্রস এজের পরিবৃত্ত বিবেচনা করুন।
ধরুন এই বৃত্তটি অন্য বৃত্তে রূপান্তরিত হয় যার বেস একটি জ্যা কিন্তু Oy দিকে আরো দূরে থাকে।
আমাদের বৃত্ত কিছুক্ষণ উপরে উঠবে, কিন্তু বেস L ও R-এর উপরের স্পর্শক না হলে আমরা L বা R-এর একটি বিন্দু পাব যা পরিবৃত্তে কোনো বিন্দু ছাড়া একটি নতুন ত্রিভুজ দেয়।
এই ত্রিভুজের নতুন L-R এজ হলো পরবর্তী যোগ করা ক্রস এজ।
এটি দক্ষতার সাথে করতে, আমরা দুটি এজ `lcand` ও `rcand` হিসাব করি যেন `lcand` এই প্রক্রিয়ায় পাওয়া প্রথম L বিন্দুতে নির্দেশ করে, এবং `rcand` প্রথম R বিন্দুতে নির্দেশ করে।
তারপর আমরা সেটি বেছে নিই যেটি আগে পাওয়া যাবে। প্রাথমিকভাবে বেস L ও R-এর নিচের স্পর্শকে নির্দেশ করে।

## ইমপ্লিমেন্টেশন

লক্ষ্য করুন in_circle ফাংশনের ইমপ্লিমেন্টেশন GCC-নির্দিষ্ট।

```{.cpp file=delaunay}
typedef long long ll;

bool ge(const ll& a, const ll& b) { return a >= b; }
bool le(const ll& a, const ll& b) { return a <= b; }
bool eq(const ll& a, const ll& b) { return a == b; }
bool gt(const ll& a, const ll& b) { return a > b; }
bool lt(const ll& a, const ll& b) { return a < b; }
int sgn(const ll& a) { return a >= 0 ? a ? 1 : 0 : -1; }

struct pt {
    ll x, y;
    pt() { }
    pt(ll _x, ll _y) : x(_x), y(_y) { }
    pt operator-(const pt& p) const {
        return pt(x - p.x, y - p.y);
    }
    ll cross(const pt& p) const {
        return x * p.y - y * p.x;
    }
    ll cross(const pt& a, const pt& b) const {
        return (a - *this).cross(b - *this);
    }
    ll dot(const pt& p) const {
        return x * p.x + y * p.y;
    }
    ll dot(const pt& a, const pt& b) const {
        return (a - *this).dot(b - *this);
    }
    ll sqrLength() const {
        return this->dot(*this);
    }
    bool operator==(const pt& p) const {
        return eq(x, p.x) && eq(y, p.y);
    }
};

const pt inf_pt = pt(1e18, 1e18);

struct QuadEdge {
    pt origin;
    QuadEdge* rot = nullptr;
    QuadEdge* onext = nullptr;
    bool used = false;
    QuadEdge* rev() const {
        return rot->rot;
    }
    QuadEdge* lnext() const {
        return rot->rev()->onext->rot;
    }
    QuadEdge* oprev() const {
        return rot->onext->rot;
    }
    pt dest() const {
        return rev()->origin;
    }
};

QuadEdge* make_edge(pt from, pt to) {
    QuadEdge* e1 = new QuadEdge;
    QuadEdge* e2 = new QuadEdge;
    QuadEdge* e3 = new QuadEdge;
    QuadEdge* e4 = new QuadEdge;
    e1->origin = from;
    e2->origin = to;
    e3->origin = e4->origin = inf_pt;
    e1->rot = e3;
    e2->rot = e4;
    e3->rot = e2;
    e4->rot = e1;
    e1->onext = e1;
    e2->onext = e2;
    e3->onext = e4;
    e4->onext = e3;
    return e1;
}

void splice(QuadEdge* a, QuadEdge* b) {
    swap(a->onext->rot->onext, b->onext->rot->onext);
    swap(a->onext, b->onext);
}

void delete_edge(QuadEdge* e) {
    splice(e, e->oprev());
    splice(e->rev(), e->rev()->oprev());
    delete e->rev()->rot;
    delete e->rev();
    delete e->rot;
    delete e;
}

QuadEdge* connect(QuadEdge* a, QuadEdge* b) {
    QuadEdge* e = make_edge(a->dest(), b->origin);
    splice(e, a->lnext());
    splice(e->rev(), b);
    return e;
}

bool left_of(pt p, QuadEdge* e) {
    return gt(p.cross(e->origin, e->dest()), 0);
}

bool right_of(pt p, QuadEdge* e) {
    return lt(p.cross(e->origin, e->dest()), 0);
}

template <class T>
T det3(T a1, T a2, T a3, T b1, T b2, T b3, T c1, T c2, T c3) {
    return a1 * (b2 * c3 - c2 * b3) - a2 * (b1 * c3 - c1 * b3) +
           a3 * (b1 * c2 - c1 * b2);
}

bool in_circle(pt a, pt b, pt c, pt d) {
// If there is __int128, calculate directly.
// Otherwise, calculate angles.
#if defined(__LP64__) || defined(_WIN64)
    __int128 det = -det3<__int128>(b.x, b.y, b.sqrLength(), c.x, c.y,
                                   c.sqrLength(), d.x, d.y, d.sqrLength());
    det += det3<__int128>(a.x, a.y, a.sqrLength(), c.x, c.y, c.sqrLength(), d.x,
                          d.y, d.sqrLength());
    det -= det3<__int128>(a.x, a.y, a.sqrLength(), b.x, b.y, b.sqrLength(), d.x,
                          d.y, d.sqrLength());
    det += det3<__int128>(a.x, a.y, a.sqrLength(), b.x, b.y, b.sqrLength(), c.x,
                          c.y, c.sqrLength());
    return det > 0;
#else
    auto ang = [](pt l, pt mid, pt r) {
        ll x = mid.dot(l, r);
        ll y = mid.cross(l, r);
        long double res = atan2((long double)x, (long double)y);
        return res;
    };
    long double kek = ang(a, b, c) + ang(c, d, a) - ang(b, c, d) - ang(d, a, b);
    if (kek > 1e-8)
        return true;
    else
        return false;
#endif
}

pair<QuadEdge*, QuadEdge*> build_tr(int l, int r, vector<pt>& p) {
    if (r - l + 1 == 2) {
        QuadEdge* res = make_edge(p[l], p[r]);
        return make_pair(res, res->rev());
    }
    if (r - l + 1 == 3) {
        QuadEdge *a = make_edge(p[l], p[l + 1]), *b = make_edge(p[l + 1], p[r]);
        splice(a->rev(), b);
        int sg = sgn(p[l].cross(p[l + 1], p[r]));
        if (sg == 0)
            return make_pair(a, b->rev());
        QuadEdge* c = connect(b, a);
        if (sg == 1)
            return make_pair(a, b->rev());
        else
            return make_pair(c->rev(), c);
    }
    int mid = (l + r) / 2;
    QuadEdge *ldo, *ldi, *rdo, *rdi;
    tie(ldo, ldi) = build_tr(l, mid, p);
    tie(rdi, rdo) = build_tr(mid + 1, r, p);
    while (true) {
        if (left_of(rdi->origin, ldi)) {
            ldi = ldi->lnext();
            continue;
        }
        if (right_of(ldi->origin, rdi)) {
            rdi = rdi->rev()->onext;
            continue;
        }
        break;
    }
    QuadEdge* basel = connect(rdi->rev(), ldi);
    auto valid = [&basel](QuadEdge* e) { return right_of(e->dest(), basel); };
    if (ldi->origin == ldo->origin)
        ldo = basel->rev();
    if (rdi->origin == rdo->origin)
        rdo = basel;
    while (true) {
        QuadEdge* lcand = basel->rev()->onext;
        if (valid(lcand)) {
            while (in_circle(basel->dest(), basel->origin, lcand->dest(),
                             lcand->onext->dest())) {
                QuadEdge* t = lcand->onext;
                delete_edge(lcand);
                lcand = t;
            }
        }
        QuadEdge* rcand = basel->oprev();
        if (valid(rcand)) {
            while (in_circle(basel->dest(), basel->origin, rcand->dest(),
                             rcand->oprev()->dest())) {
                QuadEdge* t = rcand->oprev();
                delete_edge(rcand);
                rcand = t;
            }
        }
        if (!valid(lcand) && !valid(rcand))
            break;
        if (!valid(lcand) ||
            (valid(rcand) && in_circle(lcand->dest(), lcand->origin,
                                       rcand->origin, rcand->dest())))
            basel = connect(rcand, basel->rev());
        else
            basel = connect(basel->rev(), lcand->rev());
    }
    return make_pair(ldo, rdo);
}

vector<tuple<pt, pt, pt>> delaunay(vector<pt> p) {
    sort(p.begin(), p.end(), [](const pt& a, const pt& b) {
        return lt(a.x, b.x) || (eq(a.x, b.x) && lt(a.y, b.y));
    });
    auto res = build_tr(0, (int)p.size() - 1, p);
    QuadEdge* e = res.first;
    vector<QuadEdge*> edges = {e};
    while (lt(e->onext->dest().cross(e->dest(), e->origin), 0))
        e = e->onext;
    auto add = [&p, &e, &edges]() {
        QuadEdge* curr = e;
        do {
            curr->used = true;
            p.push_back(curr->origin);
            edges.push_back(curr->rev());
            curr = curr->lnext();
        } while (curr != e);
    };
    add();
    p.clear();
    int kek = 0;
    while (kek < (int)edges.size()) {
        if (!(e = edges[kek++])->used)
            add();
    }
    vector<tuple<pt, pt, pt>> ans;
    for (int i = 0; i < (int)p.size(); i += 3) {
        ans.push_back(make_tuple(p[i], p[i + 1], p[i + 2]));
    }
    return ans;
}
```

## সমস্যাসমূহ
 * [TIMUS 1504 Good Manners](http://acm.timus.ru/problem.aspx?space=1&num=1504)
 * [TIMUS 1520 Empire Strikes Back](http://acm.timus.ru/problem.aspx?space=1&num=1520)
 * [SGU 383 Caravans](https://codeforces.com/problemsets/acmsguru/problem/99999/383)
