---
tags:
  - Original
---

# ম্যাক্সিমাম ফ্লো - এমপিএম অ্যালগরিদম

এমপিএম (মালহোত্রা, প্রমোদ-কুমার ও মহেশ্বরী) অ্যালগরিদম ম্যাক্সিমাম ফ্লো সমস্যা $O(V^3)$-এ সমাধান করে। এই অ্যালগরিদমটি [ডিনিকের অ্যালগরিদমের](dinic.md) সাথে সাদৃশ্যপূর্ণ।

## অ্যালগরিদম

ডিনিকের অ্যালগরিদমের মতোই, এমপিএম ফেজে ফেজে চলে, প্রতিটি ফেজে আমরা $G$-এর রেসিডুয়াল নেটওয়ার্কের লেয়ারড নেটওয়ার্কে ব্লকিং ফ্লো খুঁজে বের করি।
ডিনিকের সাথে মূল পার্থক্য হলো আমরা কীভাবে ব্লকিং ফ্লো খুঁজি।
লেয়ারড নেটওয়ার্ক $L$ বিবেচনা করুন।
প্রতিটি নোডের জন্য আমরা এর _ইনার পটেনশিয়াল_ ও _আউটার পটেনশিয়াল_ নিম্নরূপ সংজ্ঞায়িত করি:

$$\begin{align}
p_{in}(v) &= \sum\limits_{(u, v)\in L}(c(u, v) - f(u, v)) \\\\
p_{out}(v) &= \sum\limits_{(v, u)\in L}(c(v, u) - f(v, u))
\end{align}$$

এছাড়া আমরা $p_{in}(s) = p_{out}(t) = \infty$ সেট করি।
$p_{in}$ ও $p_{out}$ দেওয়া থাকলে আমরা _পটেনশিয়াল_ সংজ্ঞায়িত করি $p(v) = min(p_{in}(v), p_{out}(v))$ হিসেবে।
আমরা একটি নোড $r$-কে _রেফারেন্স নোড_ বলি যদি $p(r) = min\{p(v)\}$ হয়।
একটি রেফারেন্স নোড $r$ বিবেচনা করুন।
আমরা দাবি করি যে ফ্লো $p(r)$ পরিমাণে বাড়ানো যায় এমনভাবে যেন $p(r)$ শূন্য হয়ে যায়।
এটি সত্য কারণ $L$ অ্যাসাইক্লিক, তাই আমরা $r$ থেকে আউটগোয়িং এজ দিয়ে ফ্লো পুশ করতে পারি এবং এটি $t$-তে পৌঁছাবে কারণ প্রতিটি নোডের ফ্লো পুশ করার জন্য যথেষ্ট আউটার পটেনশিয়াল আছে যখন ফ্লো সেখানে পৌঁছায়।
একইভাবে, আমরা $s$ থেকে ফ্লো টানতে পারি।
ব্লকড ফ্লো নির্মাণ এই তথ্যের উপর ভিত্তি করে।
প্রতিটি ইটারেশনে আমরা একটি রেফারেন্স নোড খুঁজি এবং $s$ থেকে $t$ পর্যন্ত $r$-এর মধ্য দিয়ে ফ্লো পুশ করি।
এই প্রক্রিয়াটি BFS দ্বারা সিমুলেট করা যায়।
সম্পূর্ণ স্যাচুরেটেড আর্কগুলো $L$ থেকে মুছে ফেলা যায় কারণ এই ফেজে পরে সেগুলো ব্যবহৃত হবে না।
একইভাবে, $s$ ও $t$ ব্যতীত আউটগোয়িং বা ইনকামিং আর্ক নেই এমন সকল নোডও মুছে ফেলা যায়।

প্রতিটি ফেজ $O(V^2)$-এ কাজ করে কারণ সর্বাধিক $V$টি ইটারেশন হয় (কারণ অন্তত নির্বাচিত রেফারেন্স নোডটি মুছে যায়), এবং প্রতিটি ইটারেশনে আমরা সর্বাধিক $V$টি ব্যতীত যত এজ দিয়ে যাই সব মুছে ফেলি।
যোগফল করলে, আমরা পাই $O(V^2 + E) = O(V^2)$।
যেহেতু $V$-এর কম ফেজ আছে (প্রমাণ দেখুন [এখানে](dinic.md)), এমপিএম মোট $O(V^3)$-এ কাজ করে।

## ইমপ্লিমেন্টেশন

```{.cpp file=mpm}
struct MPM{
    struct FlowEdge{
        int v, u;
        long long cap, flow;
        FlowEdge(){}
        FlowEdge(int _v, int _u, long long _cap, long long _flow)
            : v(_v), u(_u), cap(_cap), flow(_flow){}
        FlowEdge(int _v, int _u, long long _cap)
            : v(_v), u(_u), cap(_cap), flow(0ll){}
    };
    const long long flow_inf = 1e18;
    vector<FlowEdge> edges;
    vector<char> alive;
    vector<long long> pin, pout;
    vector<list<int> > in, out;
    vector<vector<int> > adj;
    vector<long long> ex;
    int n, m = 0;
    int s, t;
    vector<int> level;
    vector<int> q;
    int qh, qt;
    void resize(int _n){
        n = _n;
        ex.resize(n);
        q.resize(n);
        pin.resize(n);
        pout.resize(n);
        adj.resize(n);
        level.resize(n);
        in.resize(n);
        out.resize(n);
    }
    MPM(){}
    MPM(int _n, int _s, int _t){resize(_n); s = _s; t = _t;}
    void add_edge(int v, int u, long long cap){
        edges.push_back(FlowEdge(v, u, cap));
        edges.push_back(FlowEdge(u, v, 0));
        adj[v].push_back(m);
        adj[u].push_back(m + 1);
        m += 2;
    }
    bool bfs(){
        while(qh < qt){
            int v = q[qh++];
            for(int id : adj[v]){
                if(edges[id].cap - edges[id].flow < 1)continue;
                if(level[edges[id].u] != -1)continue;
                level[edges[id].u] = level[v] + 1;
                q[qt++] = edges[id].u;
            }
        }
        return level[t] != -1;
    }
    long long pot(int v){
        return min(pin[v], pout[v]);
    }
    void remove_node(int v){
        for(int i : in[v]){
            int u = edges[i].v;
            auto it = find(out[u].begin(), out[u].end(), i);
            out[u].erase(it);
            pout[u] -= edges[i].cap - edges[i].flow;
        }
        for(int i : out[v]){
            int u = edges[i].u;
            auto it = find(in[u].begin(), in[u].end(), i);
            in[u].erase(it);
            pin[u] -= edges[i].cap - edges[i].flow;
        }
    }
    void push(int from, int to, long long f, bool forw){
        qh = qt = 0;
        ex.assign(n, 0);
        ex[from] = f;
        q[qt++] = from;
        while(qh < qt){
            int v = q[qh++];
            if(v == to)
                break;
            long long must = ex[v];
            auto it = forw ? out[v].begin() : in[v].begin();
            while(true){
                int u = forw ? edges[*it].u : edges[*it].v;
                long long pushed = min(must, edges[*it].cap - edges[*it].flow);
                if(pushed == 0)break;
                if(forw){
                    pout[v] -= pushed;
                    pin[u] -= pushed;
                }
                else{
                    pin[v] -= pushed;
                    pout[u] -= pushed;
                }
                if(ex[u] == 0)
                    q[qt++] = u;
                ex[u] += pushed;
                edges[*it].flow += pushed;
                edges[(*it)^1].flow -= pushed;
                must -= pushed;
                if(edges[*it].cap - edges[*it].flow == 0){
                    auto jt = it;
                    ++jt;
                    if(forw){
                        in[u].erase(find(in[u].begin(), in[u].end(), *it));
                        out[v].erase(it);
                    }
                    else{
                        out[u].erase(find(out[u].begin(), out[u].end(), *it));
                        in[v].erase(it);
                    }
                    it = jt;
                }
                else break;
                if(!must)break;
            }
        }
    }
    long long flow(){
        long long ans = 0;
        while(true){
            pin.assign(n, 0);
            pout.assign(n, 0);
            level.assign(n, -1);
            alive.assign(n, true);
            level[s] = 0;
            qh = 0; qt = 1;
            q[0] = s;
            if(!bfs())
                break;
            for(int i = 0; i < n; i++){
                out[i].clear();
                in[i].clear();
            }
            for(int i = 0; i < m; i++){
                if(edges[i].cap - edges[i].flow == 0)
                    continue;
                int v = edges[i].v, u = edges[i].u;
                if(level[v] + 1 == level[u] && (level[u] < level[t] || u == t)){
                    in[u].push_back(i);
                    out[v].push_back(i);
                    pin[u] += edges[i].cap - edges[i].flow;
                    pout[v] += edges[i].cap - edges[i].flow;
                }
            }
            pin[s] = pout[t] = flow_inf;
            while(true){
                int v = -1;
                for(int i = 0; i < n; i++){
                    if(!alive[i])continue;
                    if(v == -1 || pot(i) < pot(v))
                        v = i;
                }
                if(v == -1)
                    break;
                if(pot(v) == 0){
                    alive[v] = false;
                    remove_node(v);
                    continue;
                }
                long long f = pot(v);
                ans += f;
                push(v, s, f, false);
                push(v, t, f, true);
                alive[v] = false;
                remove_node(v);
            }
        }
        return ans;
    }
};
```
