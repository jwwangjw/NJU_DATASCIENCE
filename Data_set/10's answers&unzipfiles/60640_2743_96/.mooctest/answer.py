#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cstdlib>
using namespace std;
struct Path{
    int next, ends;
    int wei;
}ph[600020];
int pta[300010], fa[40][300010], d[300010], s[300010], e;
int cnt[300010];
bool vis[300010];
void dfs(int p, int dpt){  //倍增LCA的初始化
    vis[p] = true;
    d[p] = dpt;
    for(int i = pta[p]; i; i = ph[i].next){
        if(vis[ph[i].ends]) continue;
        fa[0][ph[i].ends] = p;
        dfs(ph[i].ends, dpt+1);
    }
}
void makep(int u, int v){ //建边
    ph[++e].ends = v;
    ph[e].next = pta[u];
    pta[u] = e;
    ph[++e].ends = u;
    ph[e].next = pta[v];
    pta[v] = e;
}
int lca(int x, int y){//求LCA
    if(d[x] < d[y]) swap(x, y);
    int dif = d[x] - d[y];
    for(int i = 30; i >= 0; --i)
        if(1<<i <= dif)
        dif -= 1<<i,
        x = fa[i][x];
    if(x == y) return x;
    for(int i = 30;i >= 0;--i)
        if(fa[i][x]!=fa[i][y])
        x=fa[i][x],y=fa[i][y];
    if(x == y) return x;
    else return fa[0][x];
}
int dfs_ans(int p){ //还原答案
    int ans = cnt[p]; //加上自身权值
    vis[p] = true;
    for(int i = pta[p]; i; i = ph[i].next){
        if(vis[ph[i].ends]) continue;
        ans += ph[i].wei = dfs_ans(ph[i].ends); //边i的权值为子树权值和
    }
    for(int i = pta[p]; i; i = ph[i].next){
        if(ph[i].ends == fa[0][p]) ph[i].wei = ans, i = 0;
        //找到指向父亲的边（因为一条无向边被存成2条有向边）
    }
    return ans;
}
int main(){
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; ++i)
        scanf("%d", s+i);
    for(int i = 1; i < n; ++i){
        int a, b;
        scanf("%d %d", &a, &b);
        makep(a, b);
    }
    fa[0][s[1]] = s[1]; dfs(s[1], 1);
    for(int i = 1; 1<<i <= n; ++i) //倍增预处理第二步
    for(int j = 1; j <= n; ++j)
        fa[i][j] = fa[i-1][fa[i-1][j]];
    for(int i = 1; i < n; ++i) //处理每一步
        cnt[s[i]]++,cnt[s[i+1]]++,
        cnt[lca(s[i],s[i+1])] -= 2;
    memset(vis, 0, sizeof(vis));
    dfs_ans(s[1]);
    for(int i = 1; i <= n; ++i){
        int ans = 0;
        for(int j = pta[i]; j; j = ph[j].next)
            ans += ph[j].wei;
        if(i == s[n]) ans--;//结束时不需要再增加权值
        printf("%d\n", (ans+1)>>1);//向上取整
    }
    return 0;
}