#include <iostream>
#include <cstdio>
using namespace std;

int mod = 2147483647;

struct Segment {
  int l, r, v, tag;
  Segment() {
    l = 0;
    r = 0;
    v = 0;
    tag = 0;
  }
};

struct SegmentTree {
  Segment node[4000010];

  inline int lc(int n) { return (n << 1); }
  inline int rc(int n) { return ((n << 1) | 1); } 
  inline int mid(int l, int r) { return ((l + r) >> 1); }

  void push_up(int n) {
    node[n].v = (node[lc(n)].v + node[rc(n)].v) % mod;
  }

  void build(int n, int l, int r) {
    node[n].l = l;
    node[n].r = r;
    if (l == r) { return; }
    build(lc(n), l, mid(l, r));
    build(rc(n), mid(l, r) + 1, r);
  }

  void push_down(int n) {
    node[lc(n)].v = (node[lc(n)].v + node[n].tag * (node[lc(n)].r - node[lc(n)].l + 1)) % mod;
    node[rc(n)].v = (node[rc(n)].v + node[n].tag * (node[rc(n)].r - node[rc(n)].l + 1)) % mod;
    node[lc(n)].tag = (node[lc(n)].tag + node[n].tag) % mod;
    node[rc(n)].tag = (node[rc(n)].tag + node[n].tag) % mod;
    node[n].tag = 0;
  }

  void insert(int n, int l, int r, int v) {
    if (l <= node[n].l && r >= node[n].r) {
      node[n].v = (node[n].v + (node[n].r - node[n].l + 1) * v) % mod;
      node[n].tag = (node[n].tag + v) % mod;
      return;
    }
    if (node[n].tag) { push_down(n); }
    int m = mid(node[n].l, node[n].r);
    if (l <= m) { insert(lc(n), l, r, v); }
    if (r > m) { insert(rc(n), l, r, v); }
    push_up(n);
  }

  int query(int n, int l, int r) {
    if (l <= node[n].l && r >= node[n].r) {
      return node[n].v % mod;
    }
    if (node[n].tag) { push_down(n); }
    int m = mid(node[n].l, node[n].r);
    int res = 0;
    if (l <= m) { res = (res + query(lc(n), l, r)) % mod; }
    if (r > m) {
      res = (res + query(rc(n), l, r)) % mod;
    }
    return res % mod;
  }
};

struct Node {
  int h, d, hvy, top, f_edge, l_edge, p, size, v;
};

struct Edge {
  int fr, to, n;
};

struct Graph {
  Node node[1000010];
  Edge e[1000010];
  SegmentTree sg;
  int r, last, cnt, n;

  Graph() {
    last = 1;
    cnt = 1;
    n = 0;
  }

  void connect(int fr, int to) {
    if (!node[fr].f_edge) {
      node[fr].f_edge = last;
      node[fr].l_edge = last;
    } else {
      e[node[fr].l_edge].n = last;
      node[fr].l_edge = last;
    }
    e[last].fr = fr;
    e[last].to = to;
    ++last;
  }

  void dfs(int s) {
    for (int i = node[s].f_edge; i; i = e[i].n) {
      if (e[i].to == node[s].p) { continue; }
      node[e[i].to].p = s;
      node[e[i].to].h = node[s].h + 1;
      dfs(e[i].to);
      node[s].size += node[e[i].to].size;
      if (node[e[i].to].size > node[node[s].hvy].size) {
        node[s].hvy = e[i].to;
      }
    }
    node[s].size += 1;
  }

  void subdiv(int s, int h) {
    node[s].top = h;
    node[s].d = cnt++;
    sg.insert(1, node[s].d, node[s].d, node[s].v);
    if (!node[s].hvy) { return; }
    subdiv(node[s].hvy, h);
    for (int i = node[s].f_edge; i; i = e[i].n) {
      if (e[i].to == node[s].p || e[i].to == node[s].hvy) { continue; }
      subdiv(e[i].to, e[i].to);
    }
  }

  void subdiv() {
    sg.build(1, 1, n);
    node[r].h = 0;
    dfs(r);
    subdiv(r, r);
  }

  int sum(int n) {
    return sg.query(1, node[n].d, node[n].d + node[n].size - 1) % mod;
  }

  int sum(int x, int y) {
    int fx = node[x].top, fy = node[y].top, ans = 0;
    while (fx != fy) {
      if (node[fx].h >= node[fy].h) {
        ans = (ans + sg.query(1, node[fx].d, node[x].d)) % mod;
        x = node[fx].p;
        fx = node[x].top;
      } else {
        ans = (ans + sg.query(1, node[fy].d, node[y].d)) % mod;
        y = node[fy].p;
        fy = node[y].top;
      }
    }
    if (node[x].d <= node[y].d) {
      ans = (ans + sg.query(1, node[x].d, node[y].d)) % mod;
    } else {
      ans = (ans + sg.query(1, node[y].d, node[x].d)) % mod;
    }
    return ans % mod;
  }
  void modify(int n, int v) {
    sg.insert(1, node[n].d, node[n].d + node[n].size - 1, v);
  }
  void modify(int x, int y, int v) {
    int fx = node[x].top, fy = node[y].top;
    while (fx != fy) { if (node[fx].h >= node[fy].h) {
        sg.insert(1, node[fx].d, node[x].d, v);
        x = node[fx].p;
        fx = node[x].top;
      } else {
        sg.insert(1, node[fy].d, node[y].d, v);
        y = node[fy].p;
        fy = node[y].top;
      }
    }
    if (node[x].d <= node[y].d) {
      sg.insert(1, node[x].d, node[y].d, v);
    } else {
      sg.insert(1, node[y].d, node[x].d, v);
    }
  }
};

int n, m;
Graph g;

int main() {
  scanf("%d %d %d %d", &n, &m, &g.r, &mod);
  g.n = n;
  for (int i = 1; i <= n; i++) {
    scanf("%d", &g.node[i].v);
  }
  for (int i = 1; i < n; i++) {
    int fr, to;
    scanf("%d %d", &fr, &to);
    g.connect(fr, to);
    g.connect(to, fr);
  }
  g.subdiv();
  for (int i = 1; i <= m; i++) {
    int cmd, x, y, z;
    scanf("%d", &cmd);
    switch (cmd) {
    case 1:
      scanf("%d %d %d", &x, &y, &z);
      g.modify(x, y, z);
      break;
    case 2:
      scanf("%d %d", &x, &y);
      printf("%d\n", g.sum(x, y) % mod);
      break;
    case 3:
      scanf("%d %d", &x, &z);
      g.modify(x, z);
      break;
    case 4:
      scanf("%d", &x);
      printf("%d\n", g.sum(x) % mod);
      break;
    }
  }
  return 0;
}