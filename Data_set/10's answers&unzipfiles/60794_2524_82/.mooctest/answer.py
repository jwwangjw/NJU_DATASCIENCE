#include<cstdio>
#include<algorithm>
using namespace std;
#define fo(a,b,c) for(int a=b;a<=c;a++)
#define go(a,b,c) for(int a=b;a>=c;a--)
#define mp make_pair
int read(){
    int a=0,f=0;char c=getchar();
    for(;c<'0'||c>'9';c=getchar())if(c=='-')f=1;
    for(;c>='0'&&c<='9';c=getchar())a=a*10+c-'0';
    return f?-a:a;
}
const int N=1e5+2;
int a[N],t[N],pre[N],suc[N],lc[N],rc[N];
void dfs(int x){
    if(!x)return;
    printf("%d ",x);
    dfs(lc[x]);dfs(rc[x]);
} 
int main(){
    int n=read();
    fo(i,1,n)
        a[t[i]=read()]=i,
        pre[i]=i-1,suc[i]=i+1; 
    go(i,n,2){
        int pree=pre[t[i]],succ=suc[t[i]];
        if(a[pree]>a[succ])rc[pree]=t[i];
        else lc[succ]=t[i];
        pre[succ]=pree,suc[pree]=succ;
    } 
    dfs(t[1]);
    return 0;
}