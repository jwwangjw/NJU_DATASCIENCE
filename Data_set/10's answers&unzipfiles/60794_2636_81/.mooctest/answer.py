#include<bits/stdc++.h>
#define int long long
using namespace std;
struct edge{
    int to;
    int next;
    int data;
}e[2000000];
int n,m,h[200005],pop=0;
void add(int x,int y,int z){
    pop++;
    e[pop].to=y;
    e[pop].next=h[x];
    h[x]=pop;
    e[pop].data=z;
}
int d[200005],v[200005];
queue<int>q;
int bfs(int s){
    memset(d,0,sizeof(d));
    memset(v,0,sizeof(v));
    while(q.size())q.pop();
    q.push(s);v[s]=1;
    int Max=0,maX;
    while(q.size()){
        int x=q.front(),y;q.pop();
        for(int i=h[x];i;i=e[i].next){
            if(v[y=e[i].to])continue;
            v[y]=1;
            d[y]=d[x]+e[i].data;
            q.push(y);
            if(d[y]>Max){
                Max=d[y];
                maX=y;
            }
        }
    }
    return maX;
}
signed main()
{
    scanf("%lld%lld",&n,&m);
    for(int i=1;i<=m;i++){
        int x,y,z;
        scanf("%lld%lld%lld",&x,&y,&z);
        add(x,y,z);add(y,x,z);
    }
    int l=bfs(1);
    int r=bfs(l);
    int k[200005];
    int ans=d[r];
    for(int i=1;i<=n;i++)
      k[i]=d[i];
    bfs(r);
    int M=0;
    for(int i=1;i<=n;i++){
        M=max(M,min(d[i],k[i]));
    }
    printf("%lld\n",ans+M);
    return 0;
}