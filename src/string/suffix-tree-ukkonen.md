---
tags:
  - Translated
e_maxx_link: ukkonen
---

# সাফিক্স ট্রি। উক্কোনেনের অ্যালগরিদম

*এই নিবন্ধটি একটি স্টাব এবং এতে কোনো বিবরণ নেই। অ্যালগরিদমের বিবরণের জন্য, অন্যান্য উৎস দেখুন, যেমন Dan Gusfield রচিত [Algorithms on Strings, Trees, and Sequences](https://www.cs.cmu.edu/afs/cs/project/pscico-guyb/realworld/www/slidesF06/cmuonly/gusfield.pdf)।*

এই অ্যালগরিদমটি $n$ দৈর্ঘ্যের একটি প্রদত্ত স্ট্রিং $s$-এর জন্য $O(n\log(k))$) সময়ে একটি সাফিক্স ট্রি তৈরি করে, যেখানে $k$ হলো বর্ণমালার আকার (যদি $k$-কে ধ্রুবক ধরা হয়, তাহলে অ্যাসিম্পটোটিক আচরণ লিনিয়ার)।

অ্যালগরিদমে ইনপুট হলো স্ট্রিং $s$ এবং এর দৈর্ঘ্য $n$, যেগুলো গ্লোবাল ভেরিয়েবল হিসেবে পাস করা হয়।

মূল ফাংশন `build_tree` একটি সাফিক্স ট্রি তৈরি করে। এটি `node` স্ট্রাকচারের একটি অ্যারে হিসেবে সংরক্ষিত হয়, যেখানে `node[0]` হলো ট্রির রুট।

কোড সরলীকরণের জন্য, এজগুলো একই স্ট্রাকচারে সংরক্ষিত হয়: প্রতিটি ভার্টেক্সের জন্য এর `node` স্ট্রাকচারে এটি এবং এর প্যারেন্টের মধ্যের এজ সম্পর্কিত তথ্য সংরক্ষিত থাকে। সামগ্রিকভাবে প্রতিটি `node` নিম্নলিখিত তথ্য সংরক্ষণ করে:

* `(l, r)` - সাবস্ট্রিং `s[l..r-1]`-এর বাম ও ডান সীমানা যা এই নোডে যাওয়ার এজের সাথে সম্পর্কিত,
* `par` - প্যারেন্ট নোড,
* `link` - সাফিক্স লিংক,
* `next` - এই নোড থেকে বের হওয়া এজগুলোর তালিকা।

```cpp
string s;
int n;

struct node {
	int l, r, par, link;
	map<char,int> next;

	node (int l=0, int r=0, int par=-1)
		: l(l), r(r), par(par), link(-1) {}
	int len()  {  return r - l;  }
	int &get (char c) {
		if (!next.count(c))  next[c] = -1;
		return next[c];
	}
};
node t[MAXN];
int sz;

struct state {
	int v, pos;
	state (int v, int pos) : v(v), pos(pos)  {}
};
state ptr (0, 0);

state go (state st, int l, int r) {
	while (l < r)
		if (st.pos == t[st.v].len()) {
			st = state (t[st.v].get( s[l] ), 0);
			if (st.v == -1)  return st;
		}
		else {
			if (s[ t[st.v].l + st.pos ] != s[l])
				return state (-1, -1);
			if (r-l < t[st.v].len() - st.pos)
				return state (st.v, st.pos + r-l);
			l += t[st.v].len() - st.pos;
			st.pos = t[st.v].len();
		}
	return st;
}

int split (state st) {
	if (st.pos == t[st.v].len())
		return st.v;
	if (st.pos == 0)
		return t[st.v].par;
	node v = t[st.v];
	int id = sz++;
	t[id] = node (v.l, v.l+st.pos, v.par);
	t[v.par].get( s[v.l] ) = id;
	t[id].get( s[v.l+st.pos] ) = st.v;
	t[st.v].par = id;
	t[st.v].l += st.pos;
	return id;
}

int get_link (int v) {
	if (t[v].link != -1)  return t[v].link;
	if (t[v].par == -1)  return 0;
	int to = get_link (t[v].par);
	return t[v].link = split (go (state(to,t[to].len()), t[v].l + (t[v].par==0), t[v].r));
}

void tree_extend (int pos) {
	for(;;) {
		state nptr = go (ptr, pos, pos+1);
		if (nptr.v != -1) {
			ptr = nptr;
			return;
		}

		int mid = split (ptr);
		int leaf = sz++;
		t[leaf] = node (pos, n, mid);
		t[mid].get( s[pos] ) = leaf;

		ptr.v = get_link (mid);
		ptr.pos = t[ptr.v].len();
		if (!mid)  break;
	}
}

void build_tree() {
	sz = 1;
	for (int i=0; i<n; ++i)
		tree_extend (i);
}
```

## সংকুচিত ইমপ্লিমেন্টেশন

এই সংকুচিত ইমপ্লিমেন্টেশনটি [freopen](http://codeforces.com/profile/freopen) প্রস্তাব করেছেন।

```cpp
const int N=1000000,INF=1000000000;
string a;
int t[N][26],l[N],r[N],p[N],s[N],tv,tp,ts,la;

void ukkadd (int c) {
	suff:;
	if (r[tv]<tp) {
		if (t[tv][c]==-1) { t[tv][c]=ts;  l[ts]=la;
			p[ts++]=tv;  tv=s[tv];  tp=r[tv]+1;  goto suff; }
		tv=t[tv][c]; tp=l[tv];
	}
	if (tp==-1 || c==a[tp]-'a') tp++; else {
		l[ts+1]=la;  p[ts+1]=ts;
		l[ts]=l[tv];  r[ts]=tp-1;  p[ts]=p[tv];  t[ts][c]=ts+1;  t[ts][a[tp]-'a']=tv;
		l[tv]=tp;  p[tv]=ts;  t[p[ts]][a[l[ts]]-'a']=ts;  ts+=2;
		tv=s[p[ts-2]];  tp=l[ts-2];
		while (tp<=r[ts-2]) {  tv=t[tv][a[tp]-'a'];  tp+=r[tv]-l[tv]+1;}
		if (tp==r[ts-2]+1)  s[ts-2]=tv;  else s[ts-2]=ts;
		tp=r[tv]-(tp-r[ts-2])+2;  goto suff;
	}
}

void build() {
	ts=2;
	tv=0;
	tp=0;
	fill(r,r+N,(int)a.size()-1);
	s[0]=1;
	l[0]=-1;
	r[0]=-1;
	l[1]=-1;
	r[1]=-1;
	memset (t, -1, sizeof t);
	fill(t[1],t[1]+26,0);
	for (la=0; la<(int)a.size(); ++la)
		ukkadd (a[la]-'a');
}
```

কমেন্টসহ একই কোড:

```cpp
const int N=1000000,    // সাফিক্স ট্রিতে সর্বোচ্চ সম্ভাব্য নোড সংখ্যা
	INF=1000000000; // অসীম ধ্রুবক
string a;       // ইনপুট স্ট্রিং যার জন্য সাফিক্স ট্রি তৈরি হচ্ছে
int t[N][26],   // ট্রানজিশনের অ্যারে (স্টেট, অক্ষর)
	l[N],   // বাম...
	r[N],   // ...এবং ডান সীমানা, a-এর সাবস্ট্রিং-এর যা ইনকামিং এজের সাথে সম্পর্কিত
	p[N],   // নোডের প্যারেন্ট
	s[N],   // সাফিক্স লিংক
	tv,     // বর্তমান সাফিক্সের নোড (যদি আমরা এজের মাঝে থাকি, এজের নিচের নোড)
	tp,     // স্ট্রিং-এ অবস্থান যা এজের উপর অবস্থানের সাথে সম্পর্কিত (l[tv] এবং r[tv]-এর মধ্যে, সহ)
	ts,     // নোডের সংখ্যা
	la;     // স্ট্রিং-এ বর্তমান অক্ষর

void ukkadd(int c) { // ট্রিতে অক্ষর s যোগ করুন
	suff:;      // প্রতিটি সাফিক্সে ট্রানজিশনের পর আমরা এখানে ফিরে আসব (এবং আবার অক্ষর যোগ করব)
	if (r[tv]<tp) { // আমরা এখনও বর্তমান এজের সীমানার মধ্যে আছি কিনা পরীক্ষা করুন
		// যদি না থাকি, পরবর্তী এজ খুঁজুন। যদি এটি না থাকে, একটি লিফ তৈরি করুন এবং ট্রিতে যোগ করুন
		if (t[tv][c]==-1) {t[tv][c]=ts;l[ts]=la;p[ts++]=tv;tv=s[tv];tp=r[tv]+1;goto suff;}
		tv=t[tv][c];tp=l[tv];
	} // অন্যথায় শুধু পরবর্তী এজে এগিয়ে যান
	if (tp==-1 || c==a[tp]-'a')
		tp++; // যদি এজের অক্ষর c-এর সমান হয়, সেই এজে নেমে যান
	else {
		// অন্যথায় এজটিকে দুইভাগে ভাগ করুন, মাঝে ts নোড রেখে
		l[ts]=l[tv];r[ts]=tp-1;p[ts]=p[tv];t[ts][a[tp]-'a']=tv;
		// লিফ ts+1 যোগ করুন। এটি c-এর মাধ্যমে ট্রানজিশনের সাথে সম্পর্কিত।
		t[ts][c]=ts+1;l[ts+1]=la;p[ts+1]=ts;
		// বর্তমান নোডের তথ্য আপডেট করুন - ts-কে tv-এর প্যারেন্ট হিসেবে চিহ্নিত করতে ভুলবেন না
		l[tv]=tp;p[tv]=ts;t[p[ts]][a[l[ts]]-'a']=ts;ts+=2;
		// নামার জন্য প্রস্তুতি
		// tp চিহ্নিত করবে আমরা বর্তমান সাফিক্সে কোথায় আছি
		tv=s[p[ts-2]];tp=l[ts-2];
		// যতক্ষণ বর্তমান সাফিক্স শেষ না হয়, নামতে থাকুন
		while (tp<=r[ts-2]) {tv=t[tv][a[tp]-'a'];tp+=r[tv]-l[tv]+1;}
		// যদি আমরা একটি নোডে থাকি, এতে একটি সাফিক্স লিংক যোগ করুন, অন্যথায় ts-এ লিংক যোগ করুন
		// (আমরা পরবর্তী ইটারেশনে ts তৈরি করব)।
		if (tp==r[ts-2]+1) s[ts-2]=tv; else s[ts-2]=ts;
		// নতুন এজে tp যোগ করুন এবং সাফিক্সে অক্ষর যোগ করতে ফিরে যান
		tp=r[tv]-(tp-r[ts-2])+2;goto suff;
	}
}

void build() {
	ts=2;
	tv=0;
	tp=0;
	fill(r,r+N,(int)a.size()-1);
	// ট্রির রুটের জন্য ডেটা ইনিশিয়ালাইজ করুন
	s[0]=1;
	l[0]=-1;
	r[0]=-1;
	l[1]=-1;
	r[1]=-1;
	memset (t, -1, sizeof t);
	fill(t[1],t[1]+26,0);
	// ট্রিতে টেক্সট যোগ করুন, অক্ষরে অক্ষরে
	for (la=0; la<(int)a.size(); ++la)
		ukkadd (a[la]-'a');
}
```

## অনুশীলন সমস্যা

* [UVA 10679 - I Love Strings!!!](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1620)
