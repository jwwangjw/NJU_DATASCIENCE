#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
const int maxn = 100000 + 10;
vector<pair<int,int> > edges[maxn];
int n,m,dis[maxn];
inline void dfs(int now,int f,int Xor) {
    dis[now] = Xor;
    for (size_t i = 0;i < edges[now].size();i++)
        if (edges[now][i].first != f) dfs(edges[now][i].first,now,Xor^edges[now][i].second);
}
int main() {
    scanf("%d",&n);
    for (int i = 1,u,v,w;i < n;i++) {
        scanf("%d%d%d",&u,&v,&w);
        edges[u].push_back(make_pair(v,w));
        edges[v].push_back(make_pair(u,w));
    }
    dfs(1,1,1);
    scanf("%d",&m);
    for (int i = 1,u,v;i <= m;i++) {
        scanf("%d%d",&u,&v);
        printf("%d\n",dis[u]^dis[v]);
    }
    return 0;
}