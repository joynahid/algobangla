---
tags:
  - Translated
e_maxx_link: triangles_union
---

# ভার্টিক্যাল ডিকম্পোজিশন

## সারসংক্ষেপ
ভার্টিক্যাল ডিকম্পোজিশন হলো একটি শক্তিশালী কৌশল যা বিভিন্ন জ্যামিতিক সমস্যায় ব্যবহৃত হয়। মূল ধারণা হলো সমতলকে কিছু "ভালো" বৈশিষ্ট্যসম্পন্ন উল্লম্ব ফিতায় কাটা এবং এই ফিতাগুলোর জন্য স্বাধীনভাবে সমস্যা সমাধান করা। আমরা কিছু উদাহরণের মাধ্যমে এই ধারণাটি ব্যাখ্যা করব।

## ত্রিভুজসমূহের ইউনিয়নের ক্ষেত্রফল
ধরুন, একটি সমতলে $n$ টি ত্রিভুজ আছে এবং আমাদের তাদের ইউনিয়নের ক্ষেত্রফল বের করতে হবে। ত্রিভুজগুলো যদি পরস্পরকে ছেদ না করত তাহলে সমস্যাটি সহজ হতো, তাই আসুন এই ছেদগুলো থেকে মুক্তি পাই — সমতলকে উল্লম্ব ফিতায় ভাগ করি: সকল শীর্ষবিন্দু এবং বিভিন্ন ত্রিভুজের বাহুগুলোর সকল ছেদবিন্দু দিয়ে উল্লম্ব রেখা আঁকি। এরকম $O(n^2)$ টি রেখা থাকতে পারে তাই আমরা $O(n^2)$ টি ফিতা পাই। এখন একটি উল্লম্ব ফিতা বিবেচনা করুন। প্রতিটি অ-উল্লম্ব রেখাংশ হয় এটিকে বাম থেকে ডানে অতিক্রম করে অথবা মোটেও অতিক্রম করে না।
এছাড়াও, ফিতার ভিতরে কোনো দুটি রেখাংশ কঠোরভাবে ছেদ করে না। এর মানে ত্রিভুজসমূহের ইউনিয়নের যে অংশ এই ফিতার ভিতরে পড়ে তা বিচ্ছিন্ন ট্রাপিজিয়ামগুলো দিয়ে গঠিত যাদের ভূমি ফিতার পাশে অবস্থিত।
এই বৈশিষ্ট্য আমাদের নিম্নলিখিত স্ক্যানলাইন অ্যালগরিদম দিয়ে প্রতিটি ফিতার ভিতরের ক্ষেত্রফল গণনা করতে দেয়। ফিতাকে অতিক্রমকারী প্রতিটি রেখাংশ হয় ঊর্ধ্ব বা নিম্ন, সংশ্লিষ্ট ত্রিভুজের অভ্যন্তর রেখাংশের উপরে না নিচে তার উপর নির্ভর করে। আমরা প্রতিটি ঊর্ধ্ব রেখাংশকে একটি উদ্বোধনী বন্ধনী এবং প্রতিটি নিম্ন রেখাংশকে একটি সমাপনী বন্ধনী হিসেবে কল্পনা করতে পারি এবং বন্ধনী ক্রমকে ছোট সঠিক বন্ধনী ক্রমে ভেঙে ফিতাকে ট্রাপিজিয়ামে বিভক্ত করতে পারি। এই অ্যালগরিদমে $O(n^3\log n)$ সময় এবং $O(n^2)$ মেমোরি লাগে।
### অপটিমাইজেশন ১
প্রথমে আমরা রানটাইম $O(n^2\log n)$-এ কমাব। প্রতিটি ফিতার জন্য ট্রাপিজিয়াম তৈরি করার বদলে আমরা একটি ত্রিভুজের বাহু (রেখাংশ $s = (s_0, s_1)$) নির্দিষ্ট করি এবং সেই ফিতাগুলোর সেট খুঁজি যেখানে এই রেখাংশটি কোনো ট্রাপিজিয়ামের একটি বাহু। লক্ষ্য করি এক্ষেত্রে আমাদের শুধু সেই ফিতাগুলো খুঁজতে হবে যেখানে $s$-এর নিচে (বা উপরে, নিম্ন রেখাংশের ক্ষেত্রে) বন্ধনীর ব্যালেন্স শূন্য। এর মানে প্রতিটি ফিতার জন্য উল্লম্ব স্ক্যানলাইন চালানোর বদলে আমরা অন্যান্য রেখাংশের সেই অংশগুলোর জন্য একটি অনুভূমিক স্ক্যানলাইন চালাতে পারি যেগুলো $s$-এর সাপেক্ষে বন্ধনী ব্যালেন্সকে প্রভাবিত করে।
সরলতার জন্য আমরা দেখাব কীভাবে একটি ঊর্ধ্ব রেখাংশের জন্য এটি করা যায়, নিম্ন রেখাংশের জন্য অ্যালগরিদম অনুরূপ। অন্য একটি অ-উল্লম্ব রেখাংশ $t = (t_0, t_1)$ বিবেচনা করি এবং $s$ ও $t$-এর $Ox$-এর উপর অভিক্ষেপের ছেদ $[x_1, x_2]$ নির্ণয় করি। যদি এই ছেদ শূন্য হয় বা একটি বিন্দু নিয়ে গঠিত হয়, $t$-কে বাদ দেওয়া যায় কারণ $s$ ও $t$ একই ফিতার অভ্যন্তরে ছেদ করে না। অন্যথায় $s$ ও $t$-এর ছেদ $I$ বিবেচনা করি। তিনটি ক্ষেত্র আছে।

১.  $I = \varnothing$

    এক্ষেত্রে $t$, $[x_1, x_2]$-এ $s$-এর উপরে বা নিচে। যদি $t$, $s$-এর উপরে হয়, তাহলে $s$ কোনো ট্রাপিজিয়ামের বাহু কিনা তা $t$ প্রভাবিত করে না।
    যদি $t$, $s$-এর নিচে হয়, তাহলে $[x_1, x_2]$-এর সকল ফিতার বন্ধনী ক্রমের ব্যালেন্সে $1$ বা $-1$ যোগ করতে হবে, $t$ ঊর্ধ্ব না নিম্ন তার উপর নির্ভর করে।

২.  $I$ একটি মাত্র বিন্দু $p$ নিয়ে গঠিত

    এই ক্ষেত্রটি $[x_1, x_2]$-কে $[x_1, p_x]$ ও $[p_x, x_2]$-এ ভাগ করে আগের ক্ষেত্রে নিয়ে আসা যায়।

৩.  $I$ একটি রেখাংশ $l$

    এই ক্ষেত্রের মানে $x\in[x_1, x_2]$-এর জন্য $s$ ও $t$-এর অংশ সমপাতিত। যদি $t$ নিম্ন হয়, $s$ স্পষ্টতই ট্রাপিজিয়ামের বাহু নয়।
    অন্যথায়, এমন হতে পারে যে $s$ ও $t$ উভয়ই কোনো ট্রাপিজিয়ামের বাহু হিসেবে বিবেচিত হতে পারে। এই দ্ব্যর্থতা সমাধানের জন্য আমরা সিদ্ধান্ত নিতে পারি যে শুধুমাত্র সবচেয়ে কম ইনডেক্সের রেখাংশটিই বাহু হিসেবে বিবেচিত হবে (এখানে আমরা ধরে নিচ্ছি ত্রিভুজের বাহুগুলো কোনো একটি উপায়ে সংখ্যায়িত)। সুতরাং, যদি $index(s) < index(t)$ হয়, আমরা এই ক্ষেত্রটি উপেক্ষা করব,
    অন্যথায় আমরা চিহ্নিত করব যে $s$ কখনোই $[x_1, x_2]$-এ বাহু হতে পারে না (উদাহরণস্বরূপ, ব্যালেন্স $-2$ সহ একটি সংশ্লিষ্ট ইভেন্ট যোগ করে)।

এখানে তিনটি ক্ষেত্রের একটি চিত্রিত উপস্থাপনা দেওয়া হলো।

<div style="text-align: center;">
  <img src="triangle_union.png" alt="Visual">
</div>

পরিশেষে, $[x_1, x_2]$-এর সকল ফিতায় $1$ বা $-1$ এর সকল যোজন প্রক্রিয়াকরণ সম্পর্কে মন্তব্য করা উচিত। $[x_1, x_2]$-এ $w$-এর প্রতিটি যোজনের জন্য আমরা $(x_1, w),\ (x_2, -w)$ ইভেন্ট তৈরি করতে পারি
এবং একটি সুইপ লাইন দিয়ে সকল ইভেন্ট প্রক্রিয়া করতে পারি।

### অপটিমাইজেশন ২
লক্ষ্য করুন, আগের অপটিমাইজেশন প্রয়োগ করলে আমাদের আর সকল ফিতা স্পষ্টভাবে খুঁজতে হয় না। এতে মেমোরি খরচ $O(n)$-এ কমে যায়।

## কনভেক্স পলিগনের ছেদ
ভার্টিক্যাল ডিকম্পোজিশনের আরেকটি ব্যবহার হলো দুটি কনভেক্স পলিগনের ছেদ রৈখিক সময়ে গণনা করা। ধরুন প্রতিটি পলিগনের প্রতিটি শীর্ষবিন্দু দিয়ে উল্লম্ব রেখা টেনে সমতলকে উল্লম্ব ফিতায় ভাগ করা হয়েছে। তাহলে কোনো ইনপুট পলিগন এবং কোনো ফিতার ছেদ হয় একটি ট্রাপিজিয়াম, একটি ত্রিভুজ অথবা একটি বিন্দু। সুতরাং আমরা প্রতিটি উল্লম্ব ফিতার জন্য এই আকৃতিগুলোকে সরলভাবে ছেদ করতে এবং এই ছেদগুলোকে একটি একক পলিগনে মার্জ করতে পারি।

## ইমপ্লিমেন্টেশন

নিচে এমন কোড দেওয়া হলো যা $O(n^2\log n)$ সময়ে এবং $O(n)$ মেমোরিতে ত্রিভুজসমূহের একটি সেটের ইউনিয়নের ক্ষেত্রফল গণনা করে।

```{.cpp file=triangle_union}
typedef double dbl;

const dbl eps = 1e-9;

inline bool eq(dbl x, dbl y){
    return fabs(x - y) < eps;
}

inline bool lt(dbl x, dbl y){
    return x < y - eps;
}

inline bool gt(dbl x, dbl y){
    return x > y + eps;
}

inline bool le(dbl x, dbl y){
    return x < y + eps;
}

inline bool ge(dbl x, dbl y){
    return x > y - eps;
}

struct pt{
    dbl x, y;
    inline pt operator - (const pt & p)const{
        return pt{x - p.x, y - p.y};
    }
    inline pt operator + (const pt & p)const{
        return pt{x + p.x, y + p.y};
    }
    inline pt operator * (dbl a)const{
        return pt{x * a, y * a};
    }
    inline dbl cross(const pt & p)const{
        return x * p.y - y * p.x;
    }
    inline dbl dot(const pt & p)const{
        return x * p.x + y * p.y;
    }
    inline bool operator == (const pt & p)const{
        return eq(x, p.x) && eq(y, p.y);
    }
};

struct Line{
    pt p[2];
    Line(){}
    Line(pt a, pt b):p{a, b}{}
    pt vec()const{
        return p[1] - p[0];
    }
    pt& operator [](size_t i){
        return p[i];
    }
};

inline bool lexComp(const pt & l, const pt & r){
	if(fabs(l.x - r.x) > eps){
		return l.x < r.x;
	}
	else return l.y < r.y;
}

vector<pt> interSegSeg(Line l1, Line l2){
    if(eq(l1.vec().cross(l2.vec()), 0)){
        if(!eq(l1.vec().cross(l2[0] - l1[0]), 0))
            return {};
        if(!lexComp(l1[0], l1[1]))
            swap(l1[0], l1[1]);
        if(!lexComp(l2[0], l2[1]))
            swap(l2[0], l2[1]);
        pt l = lexComp(l1[0], l2[0]) ? l2[0] : l1[0];
        pt r = lexComp(l1[1], l2[1]) ? l1[1] : l2[1];
        if(l == r)
            return {l};
        else return lexComp(l, r) ? vector<pt>{l, r} : vector<pt>();
    }
    else{
        dbl s = (l2[0] - l1[0]).cross(l2.vec()) / l1.vec().cross(l2.vec());
        pt inter = l1[0] + l1.vec() * s;
        if(ge(s, 0) && le(s, 1) && le((l2[0] - inter).dot(l2[1] - inter), 0))
            return {inter};
        else
            return {};
    }
}
inline char get_segtype(Line segment, pt other_point){
    if(eq(segment[0].x, segment[1].x))
        return 0;
    if(!lexComp(segment[0], segment[1]))
        swap(segment[0], segment[1]);
    return (segment[1] - segment[0]).cross(other_point - segment[0]) > 0 ? 1 : -1;
}

dbl union_area(vector<tuple<pt, pt, pt> > triangles){
    vector<Line> segments(3 * triangles.size());
    vector<char> segtype(segments.size());
    for(size_t i = 0; i < triangles.size(); i++){
        pt a, b, c;
        tie(a, b, c) = triangles[i];
        segments[3 * i] = lexComp(a, b) ? Line(a, b) : Line(b, a);
        segtype[3 * i] = get_segtype(segments[3 * i], c);
        segments[3 * i + 1] = lexComp(b, c) ? Line(b, c) : Line(c, b);
        segtype[3 * i + 1] = get_segtype(segments[3 * i + 1], a);
        segments[3 * i + 2] = lexComp(c, a) ? Line(c, a) : Line(a, c);
        segtype[3 * i + 2] = get_segtype(segments[3 * i + 2], b);
    }
    vector<dbl> k(segments.size()), b(segments.size());
    for(size_t i = 0; i < segments.size(); i++){
        if(segtype[i]){
            k[i] = (segments[i][1].y - segments[i][0].y) / (segments[i][1].x - segments[i][0].x);
            b[i] = segments[i][0].y - k[i] * segments[i][0].x;
        }
    }
    dbl ans = 0;
    for(size_t i = 0; i < segments.size(); i++){
        if(!segtype[i])
            continue;
        dbl l = segments[i][0].x, r = segments[i][1].x;
        vector<pair<dbl, int> > evts;
        for(size_t j = 0; j < segments.size(); j++){
            if(!segtype[j] || i == j)
                continue;
            dbl l1 = segments[j][0].x, r1 = segments[j][1].x;
            if(ge(l1, r) || ge(l, r1))
                continue;
            dbl common_l = max(l, l1), common_r = min(r, r1);
            auto pts = interSegSeg(segments[i], segments[j]);
            if(pts.empty()){
                dbl yl1 = k[j] * common_l + b[j];
                dbl yl = k[i] * common_l + b[i];
                if(lt(yl1, yl) == (segtype[i] == 1)){
                    int evt_type = -segtype[i] * segtype[j];
                    evts.emplace_back(common_l, evt_type);
                    evts.emplace_back(common_r, -evt_type);
                }
            }
            else if(pts.size() == 1u){
                dbl yl = k[i] * common_l + b[i], yl1 = k[j] * common_l + b[j];
                int evt_type = -segtype[i] * segtype[j];
                if(lt(yl1, yl) == (segtype[i] == 1)){
                    evts.emplace_back(common_l, evt_type);
                    evts.emplace_back(pts[0].x, -evt_type);
                }
                yl = k[i] * common_r + b[i], yl1 = k[j] * common_r + b[j];
                if(lt(yl1, yl) == (segtype[i] == 1)){
                    evts.emplace_back(pts[0].x, evt_type);
                    evts.emplace_back(common_r, -evt_type);
                }
            }
            else{
                if(segtype[j] != segtype[i] || j > i){
                    evts.emplace_back(common_l, -2);
                    evts.emplace_back(common_r, 2);
                }
            }
        }
        evts.emplace_back(l, 0);
        sort(evts.begin(), evts.end());
        size_t j = 0;
        int balance = 0;
        while(j < evts.size()){
            size_t ptr = j;
            while(ptr < evts.size() && eq(evts[j].first, evts[ptr].first)){
                balance += evts[ptr].second;
                ++ptr;
            }
            if(!balance && !eq(evts[j].first, r)){
                dbl next_x = ptr == evts.size() ? r : evts[ptr].first;
                ans -= segtype[i] * (k[i] * (next_x + evts[j].first) + 2 * b[i]) * (next_x - evts[j].first);
            }
            j = ptr;
        }
    }
    return ans/2;
}

```

## অনুশীলন সমস্যা
 * [Codeforces 62C Inquisition](https://codeforces.com/contest/62/problem/C)
 * [Codeforces 107E Darts](https://codeforces.com/contest/107/problem/E)
