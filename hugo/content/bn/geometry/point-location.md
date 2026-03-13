---
title: $O(\log n)$-এ পয়েন্ট লোকেশন
tags: 
weight: 20
---
# $O(\log n)$-এ পয়েন্ট লোকেশন

নিচের সমস্যাটা ধরো: তোমাকে ডিগ্রি এক ও শূন্য বিশিষ্ট ভার্টেক্সবিহীন একটি [প্ল্যানার সাবডিভিশন](https://en.wikipedia.org/wiki/Planar_straight-line_graph) ও অনেকগুলো কুয়েরি দেওয়া আছে।
প্রতিটি কুয়েরি একটি বিন্দু, যার জন্য আমাদের নির্ণয় করতে হবে এটা সাবডিভিশনের কোন ফেসে অবস্থিত।
আমরা প্রতিটি কুয়েরি $O(\log n)$-এ অফলাইনে উত্তর দেব।<br>
এই সমস্যাটা দেখা দিতে পারে যখন তোমাকে ভরনয় ডায়াগ্রাম বা কোনো সরল পলিগনে কিছু বিন্দু লোকেট করতে হয়।

## অ্যালগরিদম

প্রথমে, প্রতিটি কুয়েরি বিন্দু $p\ (x_0, y_0)$-এর জন্য আমরা এমন একটি এজ খুঁজতে চাই যে বিন্দুটি কোনো এজে থাকলে, আমরা যে এজটি পেয়েছি তার উপরই থাকে, অন্যথায় এই এজটি $x = x_0$ রেখাকে কোনো অনন্য বিন্দু $(x_0, y)$-তে ছেদ করে যেখানে $y < y_0$ এবং এমন সব এজের মধ্যে এই $y$ সর্বাধিক।
নিচের ছবিটি উভয় ক্ষেত্র দেখায়।

<div style="text-align: center;">
  <img src="/images/geometry/point_location_goal.png" alt="Image of Goal">
</div>

আমরা সুইপ লাইন অ্যালগরিদম ব্যবহার করে এই সমস্যাটি অফলাইনে সমাধান করব। চলুন কুয়েরি বিন্দু ও এজগুলোর প্রান্তবিন্দুর x-স্থানাঙ্কগুলো ক্রমবর্ধমান ক্রমে ইটারেট করি এবং এজগুলোর একটি সেট $s$ বজায় রাখি। প্রতিটি x-স্থানাঙ্কের জন্য আমরা আগে থেকে কিছু ইভেন্ট যোগ করব।

ইভেন্টগুলো চার ধরনের হবে: _add_, _remove_, _vertical_, _get_।
প্রতিটি উল্লম্ব এজের (উভয় প্রান্তবিন্দুর x-স্থানাঙ্ক একই) জন্য আমরা সংশ্লিষ্ট x-স্থানাঙ্কের জন্য একটি _vertical_ ইভেন্ট যোগ করব।
অন্য প্রতিটি এজের জন্য প্রান্তবিন্দুগুলোর x-স্থানাঙ্কের সর্বনিম্নে একটি _add_ ইভেন্ট এবং সর্বাধিকে একটি _remove_ ইভেন্ট যোগ করব।
সবশেষে, প্রতিটি কুয়েরি বিন্দুর জন্য এর x-স্থানাঙ্কে একটি _get_ ইভেন্ট যোগ করব।

প্রতিটি x-স্থানাঙ্কের জন্য আমরা ইভেন্টগুলো তাদের ধরন অনুযায়ী (_vertical_, _get_, _remove_, _add_) ক্রমে সাজাব।
নিচের ছবিটি প্রতিটি x-স্থানাঙ্কের জন্য সাজানো ক্রমে সব ইভেন্ট দেখায়।

<div style="text-align: center;">
  <img src="/images/geometry/point_location_events.png" alt="Image of Events">
</div>

সুইপ-লাইন প্রক্রিয়ার সময় আমরা দুটি সেট বজায় রাখব।
সব অ-উল্লম্ব এজের জন্য একটি সেট $t$, এবং উল্লম্ব এজগুলোর জন্য বিশেষভাবে একটি সেট $vert$।
প্রতিটি x-স্থানাঙ্ক প্রক্রিয়া শুরুতে আমরা $vert$ সেটটি পরিষ্কার করব।

এখন একটি নির্দিষ্ট x-স্থানাঙ্কের জন্য ইভেন্টগুলো প্রক্রিয়া করি।

 - _vertical_ ইভেন্ট পেলে, আমরা সংশ্লিষ্ট এজের প্রান্তবিন্দুগুলোর সর্বনিম্ন y-স্থানাঙ্ক $vert$-এ ইনসার্ট করব।
 - _remove_ বা _add_ ইভেন্ট পেলে, আমরা $t$ থেকে সংশ্লিষ্ট এজ সরাব বা $t$-তে যোগ করব।
 - সবশেষে, প্রতিটি _get_ ইভেন্টের জন্য আমাদের $vert$-এ বাইনারি সার্চ করে পরীক্ষা করতে হবে বিন্দুটি কোনো উল্লম্ব এজের উপর আছে কি না।
বিন্দুটি কোনো উল্লম্ব এজে না থাকলে, আমাদের $t$-তে এই কুয়েরির উত্তর খুঁজতে হবে।
এটা করতে, আমরা আবার বাইনারি সার্চ করি।
কিছু বিশেষ ক্ষেত্র সামলাতে (যেমন ত্রিভুজ $(0,~0)$, $(0,~2)$, $(1, 1)$-এর ক্ষেত্রে $(0,~0)$ বিন্দু কুয়েরি করলে), এই x-স্থানাঙ্কের সব ইভেন্ট প্রক্রিয়া করার পর আমাদের সব _get_ ইভেন্টের উত্তর আবার দিতে হবে এবং দুটি উত্তরের মধ্যে সেরাটি বেছে নিতে হবে।

এখন $t$ সেটের জন্য একটি কম্প্যারেটর বেছে নিই।
এই কম্প্যারেটরকে পরীক্ষা করতে হবে একটি এজ অন্যটির উপরে নেই এমন প্রতিটি x-স্থানাঙ্কের জন্য যা উভয়ই কভার করে। ধরো আমাদের দুটো এজ $(a, b)$ ও $(c, d)$ আছে। তখন কম্প্যারেটরটি হলো (সিউডোকোডে):<br>

$val = sgn((b - a)\times(c - a)) + sgn((b - a)\times(d - a))$<br>
<b>if</b> $val \neq 0$<br>
<b>then return</b> $val > 0$<br>
$val = sgn((d - c)\times(a - c)) + sgn((d - c)\times(b - c))$<br>
<b>return</b> $val < 0$<br>

এখন প্রতিটি কুয়েরির জন্য আমাদের সংশ্লিষ্ট এজ আছে।
ফেস কীভাবে খুঁজব?
যদি এজ খুঁজে না পাই তার মানে বিন্দুটি বাইরের ফেসে।
বিন্দুটি পাওয়া এজের উপর থাকলে, ফেস অনন্য নয়।
অন্যথায়, দুটি প্রার্থী আছে — এই এজ দ্বারা সীমাবদ্ধ ফেসগুলো।
কোনটা উত্তর তা কীভাবে পরীক্ষা করব? লক্ষ্য কর এজটি উল্লম্ব নয়।
তখন উত্তর হলো এই এজের উপরে থাকা ফেস।
প্রতিটি অ-উল্লম্ব এজের জন্য এমন ফেস খুঁজি।
প্রতিটি ফেসের ঘড়ির কাঁটার বিপরীত দিকে ট্রাভার্সাল ধরো।
যদি এই ট্রাভার্সালের সময় এজ অতিক্রম করতে গিয়ে x-স্থানাঙ্ক বৃদ্ধি পায়, তাহলে এই ফেসটিই আমাদের এই এজের জন্য খুঁজতে হবে।

## দ্রষ্টব্য

আসলে, পার্সিস্টেন্ট ট্রি ব্যবহার করে এই পদ্ধতিতে কুয়েরিগুলো অনলাইনেও উত্তর দেওয়া যায়।

## ইমপ্লিমেন্টেশন

নিচের কোড পূর্ণসংখ্যার জন্য ইমপ্লিমেন্ট করা হয়েছে, তবে তুলনা পদ্ধতি ও পয়েন্ট টাইপ পরিবর্তন করে সহজেই ডাবলের জন্য কাজ করবে।
এই ইমপ্লিমেন্টেশন ধরে নেয় সাবডিভিশন সঠিকভাবে একটি [DCEL](https://en.wikipedia.org/wiki/Doubly_connected_edge_list)-এ স্টোর করা এবং বাইরের ফেসের নম্বর $-1$।<br>
প্রতিটি কুয়েরির জন্য একটি জোড়া $(1, i)$ ফেরত দেওয়া হয় যদি বিন্দুটি $i$ নম্বর ফেসের সম্পূর্ণ ভেতরে থাকে, এবং $(0, i)$ ফেরত দেওয়া হয় যদি বিন্দুটি $i$ নম্বর এজের উপর থাকে।

```cpp
typedef long long ll;

bool ge(const ll& a, const ll& b) { return a >= b; }
bool le(const ll& a, const ll& b) { return a <= b; }
bool eq(const ll& a, const ll& b) { return a == b; }
bool gt(const ll& a, const ll& b) { return a > b; }
bool lt(const ll& a, const ll& b) { return a < b; }
int sgn(const ll& x) { return le(x, 0) ? eq(x, 0) ? 0 : -1 : 1; }

struct pt {
    ll x, y;
    pt() {}
    pt(ll _x, ll _y) : x(_x), y(_y) {}
    pt operator-(const pt& a) const { return pt(x - a.x, y - a.y); }
    ll dot(const pt& a) const { return x * a.x + y * a.y; }
    ll dot(const pt& a, const pt& b) const { return (a - *this).dot(b - *this); }
    ll cross(const pt& a) const { return x * a.y - y * a.x; }
    ll cross(const pt& a, const pt& b) const { return (a - *this).cross(b - *this); }
    bool operator==(const pt& a) const { return a.x == x && a.y == y; }
};

struct Edge {
    pt l, r;
};

bool edge_cmp(Edge* edge1, Edge* edge2)
{
    const pt a = edge1->l, b = edge1->r;
    const pt c = edge2->l, d = edge2->r;
    int val = sgn(a.cross(b, c)) + sgn(a.cross(b, d));
    if (val != 0)
        return val > 0;
    val = sgn(c.cross(d, a)) + sgn(c.cross(d, b));
    return val < 0;
}

enum EventType { DEL = 2, ADD = 3, GET = 1, VERT = 0 };

struct Event {
    EventType type;
    int pos;
    bool operator<(const Event& event) const { return type < event.type; }
};

vector<Edge*> sweepline(vector<Edge*> planar, vector<pt> queries)
{
    using pt_type = decltype(pt::x);

    // collect all x-coordinates
    auto s =
        set<pt_type, std::function<bool(const pt_type&, const pt_type&)>>(lt);
    for (pt p : queries)
        s.insert(p.x);
    for (Edge* e : planar) {
        s.insert(e->l.x);
        s.insert(e->r.x);
    }

    // map all x-coordinates to ids
    int cid = 0;
    auto id =
        map<pt_type, int, std::function<bool(const pt_type&, const pt_type&)>>(
            lt);
    for (auto x : s)
        id[x] = cid++;

    // create events
    auto t = set<Edge*, decltype(*edge_cmp)>(edge_cmp);
    auto vert_cmp = [](const pair<pt_type, int>& l,
                       const pair<pt_type, int>& r) {
        if (!eq(l.first, r.first))
            return lt(l.first, r.first);
        return l.second < r.second;
    };
    auto vert = set<pair<pt_type, int>, decltype(vert_cmp)>(vert_cmp);
    vector<vector<Event>> events(cid);
    for (int i = 0; i < (int)queries.size(); i++) {
        int x = id[queries[i].x];
        events[x].push_back(Event{GET, i});
    }
    for (int i = 0; i < (int)planar.size(); i++) {
        int lx = id[planar[i]->l.x], rx = id[planar[i]->r.x];
        if (lx > rx) {
            swap(lx, rx);
            swap(planar[i]->l, planar[i]->r);
        }
        if (lx == rx) {
            events[lx].push_back(Event{VERT, i});
        } else {
            events[lx].push_back(Event{ADD, i});
            events[rx].push_back(Event{DEL, i});
        }
    }

    // perform sweep line algorithm
    vector<Edge*> ans(queries.size(), nullptr);
    for (int x = 0; x < cid; x++) {
        sort(events[x].begin(), events[x].end());
        vert.clear();
        for (Event event : events[x]) {
            if (event.type == DEL) {
                t.erase(planar[event.pos]);
            }
            if (event.type == VERT) {
                vert.insert(make_pair(
                    min(planar[event.pos]->l.y, planar[event.pos]->r.y),
                    event.pos));
            }
            if (event.type == ADD) {
                t.insert(planar[event.pos]);
            }
            if (event.type == GET) {
                auto jt = vert.upper_bound(
                    make_pair(queries[event.pos].y, planar.size()));
                if (jt != vert.begin()) {
                    --jt;
                    int i = jt->second;
                    if (ge(max(planar[i]->l.y, planar[i]->r.y),
                           queries[event.pos].y)) {
                        ans[event.pos] = planar[i];
                        continue;
                    }
                }
                Edge* e = new Edge;
                e->l = e->r = queries[event.pos];
                auto it = t.upper_bound(e);
                if (it != t.begin())
                    ans[event.pos] = *(--it);
                delete e;
            }
        }

        for (Event event : events[x]) {
            if (event.type != GET)
                continue;
            if (ans[event.pos] != nullptr &&
                eq(ans[event.pos]->l.x, ans[event.pos]->r.x))
                continue;

            Edge* e = new Edge;
            e->l = e->r = queries[event.pos];
            auto it = t.upper_bound(e);
            delete e;
            if (it == t.begin())
                e = nullptr;
            else
                e = *(--it);
            if (ans[event.pos] == nullptr) {
                ans[event.pos] = e;
                continue;
            }
            if (e == nullptr)
                continue;
            if (e == ans[event.pos])
                continue;
            if (id[ans[event.pos]->r.x] == x) {
                if (id[e->l.x] == x) {
                    if (gt(e->l.y, ans[event.pos]->r.y))
                        ans[event.pos] = e;
                }
            } else {
                ans[event.pos] = e;
            }
        }
    }
    return ans;
}

struct DCEL {
    struct Edge {
        pt origin;
        Edge* nxt = nullptr;
        Edge* twin = nullptr;
        int face;
    };
    vector<Edge*> body;
};

vector<pair<int, int>> point_location(DCEL planar, vector<pt> queries)
{
    vector<pair<int, int>> ans(queries.size());
    vector<Edge*> planar2;
    map<intptr_t, int> pos;
    map<intptr_t, int> added_on;
    int n = planar.body.size();
    for (int i = 0; i < n; i++) {
        if (planar.body[i]->face > planar.body[i]->twin->face)
            continue;
        Edge* e = new Edge;
        e->l = planar.body[i]->origin;
        e->r = planar.body[i]->twin->origin;
        added_on[(intptr_t)e] = i;
        pos[(intptr_t)e] =
            lt(planar.body[i]->origin.x, planar.body[i]->twin->origin.x)
                ? planar.body[i]->face
                : planar.body[i]->twin->face;
        planar2.push_back(e);
    }
    auto res = sweepline(planar2, queries);
    for (int i = 0; i < (int)queries.size(); i++) {
        if (res[i] == nullptr) {
            ans[i] = make_pair(1, -1);
            continue;
        }
        pt p = queries[i];
        pt l = res[i]->l, r = res[i]->r;
        if (eq(p.cross(l, r), 0) && le(p.dot(l, r), 0)) {
            ans[i] = make_pair(0, added_on[(intptr_t)res[i]]);
            continue;
        }
        ans[i] = make_pair(1, pos[(intptr_t)res[i]]);
    }
    for (auto e : planar2)
        delete e;
    return ans;
}
```

## অনুশীলন সমস্যা
 * [TIMUS 1848 Fly Hunt](http://acm.timus.ru/problem.aspx?space=1&num=1848&locale=en)
 * [UVA 12310 Point Location](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=297&page=show_problem&problem=3732)
