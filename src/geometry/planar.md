---
title: প্ল্যানার গ্রাফের ফেস খুঁজে বের করা
tags:
  - Translated
e_maxx_link: facets
---
# প্ল্যানার গ্রাফের ফেস খুঁজে বের করা

একটি গ্রাফ $G$ বিবেচনা করুন যার $n$ টি ভার্টেক্স ও $m$ টি এজ আছে, এবং যেটি সমতলে এমনভাবে আঁকা যায় যে দুটি এজ শুধুমাত্র একটি সাধারণ ভার্টেক্সে (যদি থাকে) ছেদ করে।
এই ধরনের গ্রাফকে **প্ল্যানার** বলা হয়। এখন ধরুন আমাদের একটি প্ল্যানার গ্রাফ তার স্ট্রেট-লাইন এমবেডিং সহ দেওয়া আছে, অর্থাৎ প্রতিটি ভার্টেক্স $v$-এর জন্য আমাদের কাছে একটি বিন্দু $(x, y)$ আছে এবং সব এজ এই বিন্দুগুলোর মধ্যে রেখাখণ্ড হিসেবে ছেদ ছাড়াই আঁকা (এমন এমবেডিং সবসময় বিদ্যমান)। এই রেখাখণ্ডগুলো সমতলকে কয়েকটি অঞ্চলে ভাগ করে, যাদের ফেস বলা হয়। ঠিক একটি ফেস সীমাহীন। এই ফেসকে **বাইরের** ফেস বলা হয়, বাকিগুলোকে **ভেতরের** ফেস বলা হয়।

এই নিবন্ধে আমরা একটি প্ল্যানার গ্রাফের ভেতরের ও বাইরের উভয় ফেস খুঁজে বের করার বিষয়ে আলোচনা করব। আমরা ধরে নেব গ্রাফটি সংযুক্ত।

## প্ল্যানার গ্রাফ সম্পর্কে কিছু তথ্য

এই অংশে আমরা প্ল্যানার গ্রাফ সম্পর্কে কিছু তথ্য প্রমাণ ছাড়া উপস্থাপন করব। যে পাঠকরা প্রমাণে আগ্রহী তাদের [Graph Theory by R. Diestel](https://www.math.uni-hamburg.de/home/diestel/books/graph.theory/preview/Ch4.pdf) (এই বইয়ের উপর ভিত্তি করে [প্ল্যানারিটি সম্পর্কিত ভিডিও লেকচারও](https://www.youtube.com/@DiestelGraphTheory) দেখুন) বা অন্য কোনো বই দেখা উচিত।

### অয়লারের উপপাদ্য
অয়লারের উপপাদ্য বলে যে $n$ টি ভার্টেক্স, $m$ টি এজ ও $f$ টি ফেস বিশিষ্ট একটি সংযুক্ত প্ল্যানার গ্রাফের যেকোনো সঠিক এমবেডিং নিম্নলিখিত শর্ত পূরণ করে:

$$n - m + f = 2$$

এবং আরও সাধারণভাবে, $k$ টি সংযুক্ত উপাদান বিশিষ্ট প্রতিটি প্ল্যানার গ্রাফ নিম্নলিখিত শর্ত পূরণ করে:

$$n - m + f = 1 + k$$

### প্ল্যানার গ্রাফের এজ সংখ্যা
যদি $n \ge 3$ হয় তাহলে $n$ ভার্টেক্স বিশিষ্ট প্ল্যানার গ্রাফের সর্বাধিক এজ সংখ্যা $3n - 6$। এই সংখ্যা যেকোনো সংযুক্ত প্ল্যানার গ্রাফে অর্জিত হয় যেখানে প্রতিটি ফেস একটি ত্রিভুজ দ্বারা সীমাবদ্ধ। কমপ্লেক্সিটির দিক থেকে এই তথ্যের অর্থ হলো যেকোনো প্ল্যানার গ্রাফের জন্য $m = O(n)$।

### প্ল্যানার গ্রাফের ফেস সংখ্যা
উপরের তথ্যের সরাসরি ফলাফল হিসেবে, যদি $n \ge 3$ হয় তাহলে $n$ ভার্টেক্স বিশিষ্ট প্ল্যানার গ্রাফের সর্বাধিক ফেস সংখ্যা $2n - 4$।

### প্ল্যানার গ্রাফে সর্বনিম্ন ভার্টেক্স ডিগ্রি
প্রতিটি প্ল্যানার গ্রাফে ৫ বা তার কম ডিগ্রি বিশিষ্ট একটি ভার্টেক্স থাকে।

## অ্যালগরিদম

প্রথমে, প্রতিটি ভার্টেক্সের জন্য সংলগ্ন এজগুলো পোলার কোণ অনুযায়ী সাজান।
এখন গ্রাফটি নিম্নরূপে ট্রাভার্স করি। ধরুন আমরা $(v, u)$ এজ দিয়ে ভার্টেক্স $u$-তে প্রবেশ করেছি এবং $u$-এর সাজানো অ্যাডজাসেন্সি লিস্টে $(v, u)$-এর পরবর্তী এজ হলো $(u, w)$। তখন পরবর্তী ভার্টেক্স হবে $w$। দেখা যায় যে আমরা যদি কোনো এজ $(v, u)$ থেকে এই ট্রাভার্সাল শুরু করি, আমরা $(v, u)$-র সংলগ্ন ফেসগুলোর ঠিক একটি ট্রাভার্স করব, কোন ফেস তা নির্ভর করবে আমাদের প্রথম পদক্ষেপ $u$ থেকে $v$ নাকি $v$ থেকে $u$।

এখন অ্যালগরিদমটি বেশ স্পষ্ট। আমাদের গ্রাফের সব এজের উপর ইটারেট করতে হবে এবং প্রতিটি এজের জন্য ট্রাভার্সাল শুরু করতে হবে যেটি পূর্ববর্তী কোনো ট্রাভার্সালে ভিজিট হয়নি। এভাবে আমরা প্রতিটি ফেস ঠিক একবার পাব, এবং প্রতিটি এজ দুবার ট্রাভার্স হবে (প্রতিটি দিকে একবার)।

### পরবর্তী এজ খুঁজে বের করা
ট্রাভার্সালের সময় আমাদের ঘড়ির কাঁটার বিপরীত ক্রমে পরবর্তী এজ খুঁজতে হবে। পরবর্তী এজ খোঁজার সবচেয়ে সুস্পষ্ট উপায় হলো কোণ দিয়ে বাইনারি সার্চ। তবে, প্রতিটি ভার্টেক্সের সংলগ্ন এজগুলোর ঘড়ির কাঁটার বিপরীত ক্রম দেওয়া থাকলে, আমরা পরবর্তী এজগুলো আগে থেকে গণনা করে একটি হ্যাশ টেবিলে সংরক্ষণ করতে পারি। এজগুলো ইতিমধ্যে কোণ অনুযায়ী সাজানো থাকলে, এই ক্ষেত্রে সব ফেস খোঁজার কমপ্লেক্সিটি লিনিয়ার হয়ে যায়।

### বাইরের ফেস খুঁজে বের করা
দেখা সহজ যে অ্যালগরিদম প্রতিটি ভেতরের ফেস ঘড়ির কাঁটার দিকে এবং বাইরের ফেস ঘড়ির কাঁটার বিপরীত দিকে ট্রাভার্স করে, তাই বাইরের ফেস প্রতিটি ফেসের ক্রম পরীক্ষা করে পাওয়া যায়।

### কমপ্লেক্সিটি
এটা বেশ স্পষ্ট যে অ্যালগরিদমের কমপ্লেক্সিটি সাজানোর কারণে $O(m \log m)$, এবং যেহেতু $m = O(n)$, এটি আসলে $O(n \log n)$। আগে উল্লেখ করা হয়েছে, সাজানো ছাড়া কমপ্লেক্সিটি $O(n)$ হয়ে যায়।

## গ্রাফ সংযুক্ত না হলে কী হবে?

প্রথম দৃষ্টিতে মনে হতে পারে যে বিচ্ছিন্ন গ্রাফের ফেস খোঁজা খুব কঠিন নয় কারণ আমরা প্রতিটি সংযুক্ত উপাদানের জন্য একই অ্যালগরিদম চালাতে পারি। তবে, উপাদানগুলো নেস্টেড পদ্ধতিতে আঁকা হতে পারে, **ছিদ্র** (holes) তৈরি করে (নিচের ছবি দেখুন)। এই ক্ষেত্রে কোনো উপাদানের ভেতরের ফেস অন্য কোনো উপাদানের বাইরের ফেস হয়ে যায় এবং এর একটি জটিল বিচ্ছিন্ন সীমানা থাকে। এমন ক্ষেত্র সামলানো বেশ কঠিন, একটি সম্ভাব্য পদ্ধতি হলো [পয়েন্ট লোকেশন](point-location.md) অ্যালগরিদম দিয়ে নেস্টেড উপাদান চিহ্নিত করা।

<div style="text-align: center;">
  <img src="planar_hole.png" alt="Planar graph with holes">
</div>

## ইমপ্লিমেন্টেশন
নিম্নলিখিত ইমপ্লিমেন্টেশন প্রতিটি ফেসের জন্য ভার্টেক্সের একটি ভেক্টর ফেরত দেয়, বাইরের ফেস প্রথমে আসে।
ভেতরের ফেসগুলো ঘড়ির কাঁটার বিপরীত ক্রমে এবং বাইরের ফেস ঘড়ির কাঁটার ক্রমে ফেরত দেওয়া হয়।

সরলতার জন্য আমরা কোণ দিয়ে বাইনারি সার্চ করে পরবর্তী এজ খুঁজি।
```{.cpp file=planar}
struct Point {
    int64_t x, y;

    Point(int64_t x_, int64_t y_): x(x_), y(y_) {}

    Point operator - (const Point & p) const {
        return Point(x - p.x, y - p.y);
    }

    int64_t cross (const Point & p) const {
        return x * p.y - y * p.x;
    }

    int64_t cross (const Point & p, const Point & q) const {
        return (p - *this).cross(q - *this);
    }

    int half () const {
        return int(y < 0 || (y == 0 && x < 0));
    }
};

std::vector<std::vector<size_t>> find_faces(std::vector<Point> vertices, std::vector<std::vector<size_t>> adj) {
    size_t n = vertices.size();
    std::vector<std::vector<char>> used(n);
    for (size_t i = 0; i < n; i++) {
        used[i].resize(adj[i].size());
        used[i].assign(adj[i].size(), 0);
        auto compare = [&](size_t l, size_t r) {
            Point pl = vertices[l] - vertices[i];
            Point pr = vertices[r] - vertices[i];
            if (pl.half() != pr.half())
                return pl.half() < pr.half();
            return pl.cross(pr) > 0;
        };
        std::sort(adj[i].begin(), adj[i].end(), compare);
    }
    std::vector<std::vector<size_t>> faces;
    for (size_t i = 0; i < n; i++) {
        for (size_t edge_id = 0; edge_id < adj[i].size(); edge_id++) {
            if (used[i][edge_id]) {
                continue;
            }
            std::vector<size_t> face;
            size_t v = i;
            size_t e = edge_id;
            while (!used[v][e]) {
                used[v][e] = true;
                face.push_back(v);
                size_t u = adj[v][e];
                size_t e1 = std::lower_bound(adj[u].begin(), adj[u].end(), v, [&](size_t l, size_t r) {
                    Point pl = vertices[l] - vertices[u];
                    Point pr = vertices[r] - vertices[u];
                    if (pl.half() != pr.half())
                        return pl.half() < pr.half();
                    return pl.cross(pr) > 0;
                }) - adj[u].begin() + 1;
                if (e1 == adj[u].size()) {
                    e1 = 0;
                }
                v = u;
                e = e1;
            }
            std::reverse(face.begin(), face.end());
            Point p1 = vertices[face[0]];
            __int128 sum = 0;
            for (int j = 0; j < face.size(); ++j) {
                Point p2 = vertices[face[j]];
                Point p3 = vertices[face[(j + 1) % face.size()]];
                sum += (p2 - p1).cross(p3 - p2);
            }
            if (sum <= 0) {
                faces.insert(faces.begin(), face);
            } else {
                faces.emplace_back(face);
            }
        }
    }
    return faces;
}
```

## রেখাখণ্ড থেকে প্ল্যানার গ্রাফ তৈরি

কখনো কখনো আপনাকে সরাসরি গ্রাফ দেওয়া হয় না, বরং সমতলে রেখাখণ্ডের একটি সেট দেওয়া হয়, এবং প্রকৃত গ্রাফটি সেই রেখাখণ্ডগুলোর ছেদ থেকে তৈরি হয়, নিচের ছবিতে যেমন দেখানো হয়েছে। এই ক্ষেত্রে আপনাকে ম্যানুয়ালি গ্রাফটি তৈরি করতে হবে। সবচেয়ে সহজ উপায় নিম্নরূপ। একটি রেখাখণ্ড ধরুন এবং এটিকে অন্য সব রেখাখণ্ডের সাথে ছেদ করুন। তারপর সব ছেদবিন্দু ও রেখাখণ্ডের দুই প্রান্তবিন্দু অভিধানক্রমে সাজান এবং গ্রাফে ভার্টেক্স হিসেবে যোগ করুন। এছাড়াও অভিধানক্রমে প্রতিটি দুটি পরপর ভার্টেক্সকে একটি এজ দিয়ে সংযুক্ত করুন। সব এজের জন্য এই প্রক্রিয়া সম্পন্ন করলে আমরা গ্রাফটি পাব। অবশ্যই, আমাদের নিশ্চিত করতে হবে যে দুটি সমান ছেদবিন্দু সবসময় একই ভার্টেক্সের সাথে সম্পর্কিত হবে। সবচেয়ে সহজ উপায় হলো বিন্দুগুলো তাদের স্থানাঙ্ক অনুযায়ী একটি ম্যাপে সংরক্ষণ করা, যেসব বিন্দুর স্থানাঙ্ক একটি ছোট সংখ্যার (ধরি, $10^{-9}$-এর কম) চেয়ে কম পার্থক্য বিশিষ্ট তাদের সমান ধরে। এই অ্যালগরিদম $O(n^2 \log n)$-এ কাজ করে।

<div style="text-align: center;">
  <img src="planar_implicit.png" alt="Implicitly defined graph">
</div>

## ইমপ্লিমেন্টেশন
```{.cpp file=planar_implicit}
using dbl = long double;

const dbl eps = 1e-9;

struct Point {
    dbl x, y;

    Point(){}
    Point(dbl x_, dbl y_): x(x_), y(y_) {}

    Point operator * (dbl d) const {
        return Point(x * d, y * d);
    }

    Point operator + (const Point & p) const {
        return Point(x + p.x, y + p.y);
    }

    Point operator - (const Point & p) const {
        return Point(x - p.x, y - p.y);
    }

    dbl cross (const Point & p) const {
        return x * p.y - y * p.x;
    }

    dbl cross (const Point & p, const Point & q) const {
        return (p - *this).cross(q - *this);
    }

    dbl dot (const Point & p) const {
        return x * p.x + y * p.y;
    }

    dbl dot (const Point & p, const Point & q) const {
        return (p - *this).dot(q - *this);
    }

    bool operator < (const Point & p) const {
        if (fabs(x - p.x) < eps) {
            if (fabs(y - p.y) < eps) {
                return false;
            } else {
                return y < p.y;
            }
        } else {
            return x < p.x;
        }
    }

    bool operator == (const Point & p) const {
        return fabs(x - p.x) < eps && fabs(y - p.y) < eps;
    }

    bool operator >= (const Point & p) const {
        return !(*this < p);
    }
};

struct Line{
	Point p[2];

	Line(Point l, Point r){p[0] = l; p[1] = r;}
	Point& operator [](const int & i){return p[i];}
	const Point& operator[](const int & i)const{return p[i];}
	Line(const Line & l){
		p[0] = l.p[0]; p[1] = l.p[1];
	}
	Point getOrth()const{
		return Point(p[1].y - p[0].y, p[0].x - p[1].x);
	}
	bool hasPointLine(const Point & t)const{
		return std::fabs(p[0].cross(p[1], t)) < eps;
	}
	bool hasPointSeg(const Point & t)const{
		return hasPointLine(t) && t.dot(p[0], p[1]) < eps;
	}
};

std::vector<Point> interLineLine(Line l1, Line l2){
	if(std::fabs(l1.getOrth().cross(l2.getOrth())) < eps){
		if(l1.hasPointLine(l2[0]))return {l1[0], l1[1]};
		else return {};
	}
	Point u = l2[1] - l2[0];
	Point v = l1[1] - l1[0];
	dbl s = u.cross(l2[0] - l1[0])/u.cross(v);
	return {Point(l1[0] + v * s)};
}

std::vector<Point> interSegSeg(Line l1, Line l2){
	if (l1[0] == l1[1]) {
		if (l2[0] == l2[1]) {
			if (l1[0] == l2[0])
                return {l1[0]};
			else
                return {};
		} else {
			if (l2.hasPointSeg(l1[0]))
                return {l1[0]};
			else
                return {};
		}
	}
	if (l2[0] == l2[1]) {
		if (l1.hasPointSeg(l2[0]))
            return {l2[0]};
		else
            return {};
	}
	auto li = interLineLine(l1, l2);
	if (li.empty())
        return li;
	if (li.size() == 2) {
		if (l1[0] >= l1[1])
            std::swap(l1[0], l1[1]);
		if (l2[0] >= l2[1])
            std::swap(l2[0], l2[1]);
        std::vector<Point> res(2);
		if (l1[0] < l2[0])
            res[0] = l2[0];
        else
            res[0] = l1[0];
		if (l1[1] < l2[1])
            res[1] = l1[1];
        else
            res[1] = l2[1];
		if (res[0] == res[1])
            res.pop_back();
		if (res.size() == 2u && res[1] < res[0])
            return {};
		else
            return res;
	}
	Point cand = li[0];
	if (l1.hasPointSeg(cand) && l2.hasPointSeg(cand))
        return {cand};
	else
        return {};
}

std::pair<std::vector<Point>, std::vector<std::vector<size_t>>> build_graph(std::vector<Line> segments) {
    std::vector<Point> p;
    std::vector<std::vector<size_t>> adj;
    std::map<std::pair<int64_t, int64_t>, size_t> point_id;
    auto get_point_id = [&](Point pt) {
        auto repr = std::make_pair(
            int64_t(std::round(pt.x * 1000000000) + 1e-6),
            int64_t(std::round(pt.y * 1000000000) + 1e-6)
        );
        if (!point_id.count(repr)) {
            adj.emplace_back();
            size_t id = point_id.size();
            point_id[repr] = id;
            p.push_back(pt);
            return id;
        } else {
            return point_id[repr];
        }
    };
    for (size_t i = 0; i < segments.size(); i++) {
        std::vector<size_t> curr = {
            get_point_id(segments[i][0]),
            get_point_id(segments[i][1])
        };
        for (size_t j = 0; j < segments.size(); j++) {
            if (i == j)
                continue;
            auto inter = interSegSeg(segments[i], segments[j]);
            for (auto pt: inter) {
                curr.push_back(get_point_id(pt));
            }
        }
        std::sort(curr.begin(), curr.end(), [&](size_t l, size_t r) { return p[l] < p[r]; });
        curr.erase(std::unique(curr.begin(), curr.end()), curr.end());
        for (size_t j = 0; j + 1 < curr.size(); j++) {
            adj[curr[j]].push_back(curr[j + 1]);
            adj[curr[j + 1]].push_back(curr[j]);
        }
    }
    for (size_t i = 0; i < adj.size(); i++) {
        std::sort(adj[i].begin(), adj[i].end());
        // removing edges that were added multiple times
        adj[i].erase(std::unique(adj[i].begin(), adj[i].end()), adj[i].end());
    }
    return {p, adj};
}
```

## অনুশীলন সমস্যা
 * [TIMUS 1664 Pipeline Transportation](https://acm.timus.ru/problem.aspx?space=1&num=1664)
 * [TIMUS 1681 Brother Bear's Garden](https://acm.timus.ru/problem.aspx?space=1&num=1681)
