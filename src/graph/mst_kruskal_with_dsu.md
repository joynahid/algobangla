---
tags:
  - Translated
e_maxx_link: mst_kruskal_with_dsu
---

# মিনিমাম স্প্যানিং ট্রি - ডিসজয়েন্ট সেট ইউনিয়নসহ ক্রুস্কাল

এমএসটি সমস্যা ও ক্রুস্কাল অ্যালগরিদমের ব্যাখ্যার জন্য, প্রথমে [ক্রুস্কালের অ্যালগরিদমের মূল নিবন্ধ](mst_kruskal.md) দেখুন।

এই নিবন্ধে আমরা ক্রুস্কালের অ্যালগরিদম ইমপ্লিমেন্ট করার জন্য ["ডিসজয়েন্ট সেট ইউনিয়ন"](../data_structures/disjoint_set_union.md) ডেটা স্ট্রাকচার বিবেচনা করব, যা অ্যালগরিদমটিকে $O(M \log N)$ টাইম কমপ্লেক্সিটি অর্জন করতে দেবে।

## বর্ণনা

ক্রুস্কাল অ্যালগরিদমের সরল ভার্সনের মতোই, আমরা গ্রাফের সকল এজ ওয়েটের অ-হ্রাসমান ক্রমে সর্ট করি।
তারপর প্রতিটি ভার্টেক্সকে `make_set` ফাংশনের কল দ্বারা তার নিজস্ব ট্রিতে (অর্থাৎ তার সেটে) রাখি - এতে মোট $O(N)$ সময় লাগবে।
আমরা সকল এজ (সর্টেড ক্রমে) ইটারেট করি এবং প্রতিটি এজের জন্য নির্ধারণ করি প্রান্তগুলো ভিন্ন ট্রিতে আছে কিনা (দুটি `find_set` কল দিয়ে, প্রতিটি $O(1)$-এ)।
সবশেষে, আমাদের দুটি ট্রির (সেটের) ইউনিয়ন করতে হবে, যার জন্য ডিএসইউ-এর `union_sets` ফাংশন কল করা হবে - এটিও $O(1)$-এ।
সুতরাং আমরা মোট টাইম কমপ্লেক্সিটি পাই $O(M \log N + N + M)$ = $O(M \log N)$।

## ইমপ্লিমেন্টেশন

এখানে ইউনিয়ন বাই র‍্যাংকসহ ক্রুস্কালের অ্যালগরিদমের একটি ইমপ্লিমেন্টেশন দেওয়া হলো।

```cpp
vector<int> parent, rank;

void make_set(int v) {
    parent[v] = v;
    rank[v] = 0;
}

int find_set(int v) {
    if (v == parent[v])
        return v;
    return parent[v] = find_set(parent[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (rank[a] < rank[b])
            swap(a, b);
        parent[b] = a;
        if (rank[a] == rank[b])
            rank[a]++;
    }
}

struct Edge {
    int u, v, weight;
    bool operator<(Edge const& other) {
        return weight < other.weight;
    }
};

int n;
vector<Edge> edges;

int cost = 0;
vector<Edge> result;
parent.resize(n);
rank.resize(n);
for (int i = 0; i < n; i++)
    make_set(i);

sort(edges.begin(), edges.end());

for (Edge e : edges) {
    if (find_set(e.u) != find_set(e.v)) {
        cost += e.weight;
        result.push_back(e);
        union_sets(e.u, e.v);
    }
}
```

লক্ষ্য করুন: যেহেতু এমএসটি-তে ঠিক $N-1$টি এজ থাকবে, আমরা সেই সংখ্যক এজ পেলে for লুপ বন্ধ করতে পারি।

## অনুশীলন সমস্যা

এই বিষয়ে অনুশীলন সমস্যার তালিকার জন্য [ক্রুস্কালের অ্যালগরিদমের মূল নিবন্ধ](mst_kruskal.md) দেখুন।
