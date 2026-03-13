---
title: "ট্রি-র এজে রং করা"
tags: 
weight: 30
---
# ট্রি-র এজে রং করা

এটি একটি বেশ সাধারণ কাজ। $N$ টি ভার্টেক্স বিশিষ্ট একটি ট্রি $G$ দেওয়া আছে। দুই ধরনের কুয়েরি আছে: প্রথমটি হলো একটি এজ রং করা, দ্বিতীয়টি হলো দুটি ভার্টেক্সের মধ্যে রঙিন এজের সংখ্যা জানতে চাওয়া।

এখানে আমরা একটি মোটামুটি সরল সমাধান বর্ণনা করব ([সেগমেন্ট ট্রি](../data_structures/segment_tree.md) ব্যবহার করে) যেটি প্রতিটি কুয়েরির উত্তর $O(\log N)$ সময়ে দেবে।
প্রিপ্রসেসিং ধাপে $O(N)$ সময় লাগবে।

## অ্যালগরিদম

প্রথমে, দ্বিতীয় ধরনের প্রতিটি কুয়েরি $(i,j)$ দুটি কুয়েরি $(l,i)$ এবং $(l,j)$-তে রিডিউস করতে আমাদের [LCA](lca.md) বের করতে হবে, যেখানে $l$ হলো $i$ এবং $j$-এর LCA।
$(i,j)$ কুয়েরির উত্তর হবে দুটি সাবকুয়েরির যোগফল।
এই দুটি কুয়েরির একটি বিশেষ গঠন আছে, প্রথম ভার্টেক্স দ্বিতীয়টির অ্যানসেস্টর।
আর্টিকেলের বাকি অংশে আমরা শুধু এই বিশেষ ধরনের কুয়েরি নিয়ে কথা বলব।

আমরা **প্রিপ্রসেসিং** ধাপ বর্ণনা দিয়ে শুরু করব।
ট্রি-র রুট থেকে একটি DFS চালান এবং এই DFS-এর অয়লার ট্যুর রেকর্ড করো (প্রতিটি ভার্টেক্স যখন প্রথম ভিজিট হয় তখন তালিকায় যোগ হয় এবং প্রতিবার তার কোনো চাইল্ড থেকে ফিরে আসলেও)।
একই কৌশল LCA প্রিপ্রসেসিং-এও ব্যবহার করা যায়।

এই তালিকায় প্রতিটি এজ থাকবে (এই অর্থে যে $i$ এবং $j$ যদি এজের দুই প্রান্ত হয়, তাহলে তালিকায় এমন একটি জায়গা থাকবে যেখানে $i$ এবং $j$ তালিকায় পাশাপাশি আছে), এবং এটি ঠিক দুইবার দেখা যাবে: ফরওয়ার্ড দিকে ($i$ থেকে $j$, যেখানে ভার্টেক্স $i$ রুটের কাছে $j$-এর চেয়ে) এবং বিপরীত দিকে ($j$ থেকে $i$)।

আমরা এই এজগুলোর জন্য দুটি তালিকা তৈরি করব।
প্রথমটি ফরওয়ার্ড দিকের সব এজের রং সংরক্ষণ করবে, এবং দ্বিতীয়টি বিপরীত দিকের সব এজের রং।
এজ রঙিন হলে $1$ এবং অন্যথায় $0$ ব্যবহার করব।
এই দুটি তালিকার উপর প্রতিটিতে একটি সেগমেন্ট ট্রি তৈরি করব (যোগফলসহ একক পরিবর্তনের জন্য), এদের $T1$ এবং $T2$ বলি।

ধরি আমরা $(i,j)$ আকারের একটি কুয়েরির উত্তর দিচ্ছি, যেখানে $i$ হলো $j$-এর অ্যানসেস্টর।
আমাদের $i$ এবং $j$-এর মধ্যকার পাথে কতগুলো এজ রঙিন তা ডিটারমিন করতে হবে।
অয়লার ট্যুরে প্রথমবারের মতো $i$ এবং $j$ খুঁজি, ধরি সেগুলো $p$ এবং $q$ অবস্থানে (প্রিপ্রসেসিং-এর সময় আগে থেকে গণনা করলে এটি $O(1)$-এ করা যায়)।
তাহলে কুয়েরির **উত্তর** হলো $T1[p..q-1]$-এর যোগফল বিয়োগ $T2[p..q-1]$-এর যোগফল।

**কেন?**
অয়লার ট্যুরে $[p;q]$ সেগমেন্ট কনসিডার করো।
এতে $i$ থেকে $j$ পর্যন্ত আমাদের প্রয়োজনীয় পাথের সব এজ আছে কিন্তু $i$ থেকে অন্য পাথের এজগুলোও আছে।
তবে আমাদের প্রয়োজনীয় এজ এবং বাকি এজগুলোর মধ্যে একটি বড় পার্থক্য আছে: আমাদের প্রয়োজনীয় এজগুলো শুধু একবার ফরওয়ার্ড দিকে তালিকাভুক্ত হবে, এবং অন্য সব এজ দুইবার দেখা যাবে: একবার ফরওয়ার্ড এবং একবার বিপরীত দিকে।
তাই, পার্থক্য $T1[p..q-1] - T2[p..q-1]$ আমাদের সঠিক উত্তর দেবে (মাইনাস ওয়ান প্রয়োজনীয় কারণ অন্যথায়, আমরা ভার্টেক্স $j$ থেকে বের হওয়া একটি অতিরিক্ত এজ ধরে ফেলব)।
সেগমেন্ট ট্রি-তে যোগফল কুয়েরি $O(\log N)$-এ সম্পাদিত হয়।

**প্রথম ধরনের কুয়েরির** (একটি এজ রং করা) উত্তর দেওয়া আরো সহজ - আমাদের শুধু $T1$ এবং $T2$ আপডেট করতে হবে, অর্থাৎ আমাদের এজের সাথে সংশ্লিষ্ট উপাদানের একক আপডেট করতে হবে (তালিকায় এজ খোঁজাও $O(1)$-এ সম্ভব, যদি প্রিপ্রসেসিং-এর সময় এই সার্চ করে রাখো)।
সেগমেন্ট ট্রি-তে একক পরিবর্তন $O(\log N)$-এ সম্পাদিত হয়।

## ইমপ্লিমেন্টেশন

এখানে LCA গণনাসহ সমাধানের সম্পূর্ণ ইমপ্লিমেন্টেশন দেওয়া হলো:

```cpp
const int INF = 1000 * 1000 * 1000;

typedef vector<vector<int>> graph;

vector<int> dfs_list;
vector<int> edges_list;
vector<int> h;

void dfs(int v, const graph& g, const graph& edge_ids, int cur_h = 1) {
    h[v] = cur_h;
    dfs_list.push_back(v);
    for (size_t i = 0; i < g[v].size(); ++i) {
        if (h[g[v][i]] == -1) {
            edges_list.push_back(edge_ids[v][i]);
            dfs(g[v][i], g, edge_ids, cur_h + 1);
            edges_list.push_back(edge_ids[v][i]);
            dfs_list.push_back(v);
        }
    }
}

vector<int> lca_tree;
vector<int> first;

void lca_tree_build(int i, int l, int r) {
    if (l == r) {
        lca_tree[i] = dfs_list[l];
    } else {
        int m = (l + r) >> 1;
        lca_tree_build(i + i, l, m);
        lca_tree_build(i + i + 1, m + 1, r);
        int lt = lca_tree[i + i], rt = lca_tree[i + i + 1];
        lca_tree[i] = h[lt] < h[rt] ? lt : rt;
    }
}

void lca_prepare(int n) {
    lca_tree.assign(dfs_list.size() * 8, -1);
    lca_tree_build(1, 0, (int)dfs_list.size() - 1);

    first.assign(n, -1);
    for (int i = 0; i < (int)dfs_list.size(); ++i) {
        int v = dfs_list[i];
        if (first[v] == -1)
            first[v] = i;
    }
}

int lca_tree_query(int i, int tl, int tr, int l, int r) {
    if (tl == l && tr == r)
        return lca_tree[i];
    int m = (tl + tr) >> 1;
    if (r <= m)
        return lca_tree_query(i + i, tl, m, l, r);
    if (l > m)
        return lca_tree_query(i + i + 1, m + 1, tr, l, r);
    int lt = lca_tree_query(i + i, tl, m, l, m);
    int rt = lca_tree_query(i + i + 1, m + 1, tr, m + 1, r);
    return h[lt] < h[rt] ? lt : rt;
}

int lca(int a, int b) {
    if (first[a] > first[b])
        swap(a, b);
    return lca_tree_query(1, 0, (int)dfs_list.size() - 1, first[a], first[b]);
}

vector<int> first1, first2;
vector<char> edge_used;
vector<int> tree1, tree2;

void query_prepare(int n) {
    first1.resize(n - 1, -1);
    first2.resize(n - 1, -1);
    for (int i = 0; i < (int)edges_list.size(); ++i) {
        int j = edges_list[i];
        if (first1[j] == -1)
            first1[j] = i;
        else
            first2[j] = i;
    }

    edge_used.resize(n - 1);
    tree1.resize(edges_list.size() * 8);
    tree2.resize(edges_list.size() * 8);
}

void sum_tree_update(vector<int>& tree, int i, int l, int r, int j, int delta) {
    tree[i] += delta;
    if (l < r) {
        int m = (l + r) >> 1;
        if (j <= m)
            sum_tree_update(tree, i + i, l, m, j, delta);
        else
            sum_tree_update(tree, i + i + 1, m + 1, r, j, delta);
    }
}

int sum_tree_query(const vector<int>& tree, int i, int tl, int tr, int l, int r) {
    if (l > r || tl > tr)
        return 0;
    if (tl == l && tr == r)
        return tree[i];
    int m = (tl + tr) >> 1;
    if (r <= m)
        return sum_tree_query(tree, i + i, tl, m, l, r);
    if (l > m)
        return sum_tree_query(tree, i + i + 1, m + 1, tr, l, r);
    return sum_tree_query(tree, i + i, tl, m, l, m) +
           sum_tree_query(tree, i + i + 1, m + 1, tr, m + 1, r);
}

int query(int v1, int v2) {
    return sum_tree_query(tree1, 1, 0, (int)edges_list.size() - 1, first[v1], first[v2] - 1) -
           sum_tree_query(tree2, 1, 0, (int)edges_list.size() - 1, first[v1], first[v2] - 1);
}

int main() {
    // reading the graph
    int n;
    scanf("%d", &n);
    graph g(n), edge_ids(n);
    for (int i = 0; i < n - 1; ++i) {
        int v1, v2;
        scanf("%d%d", &v1, &v2);
        --v1, --v2;
        g[v1].push_back(v2);
        g[v2].push_back(v1);
        edge_ids[v1].push_back(i);
        edge_ids[v2].push_back(i);
    }

    h.assign(n, -1);
    dfs(0, g, edge_ids);
    lca_prepare(n);
    query_prepare(n);

    for (;;) {
        if () {
            // request for painting edge x;
            // if start = true, then the edge is painted, otherwise the painting
            // is removed
            edge_used[x] = start;
            sum_tree_update(tree1, 1, 0, (int)edges_list.size() - 1, first1[x],
                            start ? 1 : -1);
            sum_tree_update(tree2, 1, 0, (int)edges_list.size() - 1, first2[x],
                            start ? 1 : -1);
        } else {
            // query the number of colored edges on the path between v1 and v2
            int l = lca(v1, v2);
            int result = query(l, v1) + query(l, v2);
            // result - the answer to the request
        }
    }
}
```
