#include<bits/stdc++.h>
#define maxn 100005
using namespace std;
int f[maxn],n,T,x,y,lnk[maxn],nxt[maxn<<1],son[maxn<<1],tot,k,cnt;
inline int read(){
    int ret=0,f=1;char ch=getchar();
    while (ch<'0'||ch>'9'){if (ch=='-') f=-f;ch=getchar();}
    while (ch<='9'&&ch>='0') ret=ret*10+ch-'0',ch=getchar();
    return ret*f;
}
inline void add(int x,int y){nxt[++tot]=lnk[x];lnk[x]=tot;son[tot]=y;}
inline void Dfs(int x,int fa){
    f[x]=1;
    for (int i=lnk[x];i;i=nxt[i])
      if (son[i]!=fa){
        Dfs(son[i],x);
        f[x]+=f[son[i]];
      }
    if (f[x]==k) f[x]=0,cnt++;
}
int main(){
    T=read();
    while (T--){
        n=read(),k=read();
        memset(lnk,0,sizeof lnk);cnt=0,tot=0;
        memset(f,0,sizeof f);
        for (int i=1;i<n;i++) x=read(),y=read(),add(x,y),add(y,x);
        if (n%k){printf("NO\n");continue;}
        Dfs(1,0);
        if (cnt==n/k) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}