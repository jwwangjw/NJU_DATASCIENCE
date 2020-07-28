#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
int t[100001],n,m,c,mp[100001],ne[100001],p[100001];
struct gjh{int l,r,yd,ans;}q[100001];
int lb(int x){return x&(-x);}
void add(int x,int y){while(x<=n)t[x]+=y,x+=lb(x);}
int sum(int x){int num=0;while(x>0)num+=t[x],x-=lb(x);return num;}
bool cmp(gjh a,gjh b){return a.l==b.l?a.r<b.r:a.l<b.l;}
bool cmp1(gjh a,gjh b){return a.yd<b.yd;}
int main()
{
   int l=1;scanf("%d%d%d",&n,&c,&m);for(int i=1;i<=n;i++)scanf("%d",&mp[i]);
   for(int i=n;i>0;i--)ne[i]=p[mp[i]],p[mp[i]]=i;
   for(int i=1;i<=c;i++)if(p[i]&&ne[p[i]])add(ne[p[i]],1);
   for(int i=1;i<=m;i++)scanf("%d%d",&q[i].l,&q[i].r),q[i].yd=i;
   sort(q+1,q+m+1,cmp);
   for(int i=1;i<=m;i++)
   {
        for(;l<q[i].l;l++)
     {
       if(ne[l])add(ne[l],-1);
       if(ne[l]&&ne[ne[l]])add(ne[ne[l]],1);
     }
        q[i].ans=sum(q[i].r)-sum(q[i].l-1);
   }
   sort(q+1,q+m+1,cmp1);
   for(int i=1;i<=m;i++)printf("%d\n",q[i].ans);
   return 0;
}