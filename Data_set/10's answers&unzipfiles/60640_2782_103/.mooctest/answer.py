#include <cstdio>

inline int Min(int a, int b) { return a < b ? a : b; }
inline int Max(int a, int b) { return a > b ? a : b; }

const int N = 3e5 + 1e3;
const int INF = 0x3f3f3f3f;

int n, rt;
long long ans;

struct node {
    int fa;
    int val, min, max;
    int son[2];
    node(int cur = 0) {
        fa = son[0] = son[1] = 0;
        val = min = max = cur;
    }
} tree[N];
int t_cnt;

inline bool get_son(int cur) { return tree[tree[cur].fa].son[1] == cur; }

void push_up(int cur) {
    tree[cur].min = Min(tree[tree[cur].son[0]].min, tree[tree[cur].son[1]].min);
    tree[cur].max = Max(tree[tree[cur].son[0]].max, tree[tree[cur].son[1]].max);
}

void rotate(int cur) {
    int tmp_fa = tree[cur].fa;
    bool kind = get_son(cur);
    if (tmp_fa == rt) {
        rt = cur;
        tree[cur].fa = 0;
    } else {
        tree[tree[tmp_fa].fa].son[get_son(tmp_fa)] = cur;
        tree[cur].fa = tree[tmp_fa].fa;
    }
    tree[tmp_fa].son[kind] = tree[cur].son[kind ^ 1];
    tree[tree[tmp_fa].son[kind]].fa = tmp_fa;
    tree[cur].son[kind ^ 1] = tmp_fa;
    tree[tmp_fa].fa = cur;
    //	push_up( tmp_fa ); push_up( cur );
}

void splay(int from, int to = 0) {
    if (from <= 0 || from == to || from == INF)
        return;
    while (tree[from].fa != to) {
        int tmp_fa = tree[from].fa;
        if (tree[tmp_fa].fa != to)
            rotate(get_son(from) == get_son(tmp_fa) ? tmp_fa : from);
        rotate(from);
    }
}

int insert(int cur, int val) {
    if (cur == 0) {
        t_cnt++;
        tree[t_cnt] = node(val);
        return t_cnt;
    }

    if (tree[cur].val == val)
        return cur;
    if (val < tree[cur].val) {
        tree[cur].son[0] = insert(tree[cur].son[0], val);
        tree[tree[cur].son[0]].fa = cur;
    } else {
        tree[cur].son[1] = insert(tree[cur].son[1], val);
        tree[tree[cur].son[1]].fa = cur;
    }

    //	push_up( cur );
    return cur;
}

int pre(int cur, int val) {
    if (cur == 0)
        return 1;
    if (tree[cur].val == val)
        return cur;
    if (tree[cur].val > val)
        return pre(tree[cur].son[0], val);
    if (tree[cur].val < val) {
        int tmp = pre(tree[cur].son[1], val);
        if (tree[cur].val > tree[tmp].val)
            tmp = cur;
        return tmp;
    }
    return 1;
}

int nxt(int cur, int val) {
    if (cur == 0)
        return 2;
    if (tree[cur].val == val)
        return nxt(tree[cur].son[1], val);
    if (tree[cur].val > val) {
        int tmp = nxt(tree[cur].son[0], val);
        if (tree[cur].val < tree[tmp].val)
            tmp = cur;
        return tmp;
    }
    if (tree[cur].val < val)
        return nxt(tree[cur].son[1], val);
    return INF;
}

int main() {
#ifdef woshiluo
    freopen("luogu.2234.in", "r", stdin);
    freopen("luogu.2234.out", "w", stdout);
#endif
    tree[1] = node(-INF);
    tree[2] = node(INF);
    t_cnt = 2;
    scanf("%d", &n);
    scanf("%lld", &ans);
    rt = insert(rt, ans);
    for (int i = 2, x; i <= n; i++) {
        scanf("%d", &x);
        int tmp_pre = pre(rt, x);
        splay(tmp_pre);
        int tmp_nxt = nxt(rt, x);
        splay(tmp_nxt);
        ans += Min(x - tree[tmp_pre].val, tree[tmp_nxt].val - x);
        insert(rt, x);
        splay(t_cnt);
    }
    printf("%lld", ans);
}