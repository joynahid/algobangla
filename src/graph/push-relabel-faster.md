---
tags:
  - Translated
e_maxx_link: preflow_push_faster
---

# ম্যাক্সিমাম ফ্লো - উন্নত পুশ-রিলেবেল পদ্ধতি

আমরা আরো ভালো রানটাইম অর্জনের জন্য [পুশ-রিলেবেল পদ্ধতি](push-relabel.md) পরিবর্তন করব।

## বর্ণনা

পরিবর্তনটি অত্যন্ত সরল:
আগের নিবন্ধে আমরা কোনো বিশেষ নিয়ম ছাড়াই এক্সেসযুক্ত একটি ভার্টেক্স বেছে নিতাম।
কিন্তু দেখা যায় যে, আমরা যদি সর্বদা **সবচেয়ে বেশি উচ্চতার** ভার্টেক্সগুলো বেছে নিই, এবং তাদের উপর পুশ ও রিলেবেল অপারেশন প্রয়োগ করি, তাহলে কমপ্লেক্সিটি আরো ভালো হবে।
তাছাড়া, সবচেয়ে বেশি উচ্চতার ভার্টেক্স নির্বাচনের জন্য আসলে কোনো ডেটা স্ট্রাকচারের দরকার নেই, আমরা শুধু সবচেয়ে বেশি উচ্চতার ভার্টেক্সগুলো একটি লিস্টে সংরক্ষণ করি, এবং তাদের সবগুলো প্রসেস হয়ে গেলে লিস্ট পুনরায় গণনা করি (তখন ইতোমধ্যে কম উচ্চতার ভার্টেক্সগুলো লিস্টে যোগ হবে), অথবা যখনই এক্সেসযুক্ত এবং বেশি উচ্চতার একটি নতুন ভার্টেক্স দেখা দেয় (কোনো ভার্টেক্স রিলেবেল করার পর)।

সরলতা সত্ত্বেও, এই পরিবর্তন কমপ্লেক্সিটি অনেক কমিয়ে দেয়।
সুনির্দিষ্টভাবে বলতে গেলে, ফলস্বরূপ অ্যালগরিদমের কমপ্লেক্সিটি $O(V E + V^2 \sqrt{E})$, যা সবচেয়ে খারাপ ক্ষেত্রে $O(V^3)$।

এই পরিবর্তনটি ১৯৮৯ সালে চেরিয়ান ও মাহেশওয়ারি প্রস্তাব করেছিলেন।

## ইমপ্লিমেন্টেশন

```{.cpp file=push_relabel_faster}
const int inf = 1000000000;

int n;
vector<vector<int>> capacity, flow;
vector<int> height, excess;

void push(int u, int v)
{
    int d = min(excess[u], capacity[u][v] - flow[u][v]);
    flow[u][v] += d;
    flow[v][u] -= d;
    excess[u] -= d;
    excess[v] += d;
}

void relabel(int u)
{
    int d = inf;
    for (int i = 0; i < n; i++) {
        if (capacity[u][i] - flow[u][i] > 0)
            d = min(d, height[i]);
    }
    if (d < inf)
        height[u] = d + 1;
}

vector<int> find_max_height_vertices(int s, int t) {
    vector<int> max_height;
    for (int i = 0; i < n; i++) {
        if (i != s && i != t && excess[i] > 0) {
            if (!max_height.empty() && height[i] > height[max_height[0]])
                max_height.clear();
            if (max_height.empty() || height[i] == height[max_height[0]])
                max_height.push_back(i);
        }
    }
    return max_height;
}

int max_flow(int s, int t)
{
    height.assign(n, 0);
    height[s] = n;
    flow.assign(n, vector<int>(n, 0));
    excess.assign(n, 0);
    excess[s] = inf;
    for (int i = 0; i < n; i++) {
        if (i != s)
            push(s, i);
    }

    vector<int> current;
    while (!(current = find_max_height_vertices(s, t)).empty()) {
        for (int i : current) {
            bool pushed = false;
            for (int j = 0; j < n && excess[i]; j++) {
                if (capacity[i][j] - flow[i][j] > 0 && height[i] == height[j] + 1) {
                    push(i, j);
                    pushed = true;
                }
            }
            if (!pushed) {
                relabel(i);
                break;
            }
        }
    }

    return excess[t];
}
```
