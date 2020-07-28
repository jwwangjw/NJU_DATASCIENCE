#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#define re register
#define il inline
#define ll long long
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define fp(i,a,b) for(re int i=a;i<=b;i++)
#define fq(i,a,b) for(re int i=a;i>=b;i--)
using namespace std;
const int mod=45989,N=5e5+100;
int n,m,top,a[N],L[N],R[N],mx,mn;
set<int>Q;
set<int>::iterator it;
il int gi()
{
  re int x=0,t=1;
  re char ch=getchar();
  while((ch<'0'||ch>'9')&&ch!='-') ch=getchar();
  if(ch=='-') t=-1,ch=getchar();
  while(ch>='0'&&ch<='9') x=x*10+ch-48,ch=getchar();
  return x*t;
}
int main()
{
  n=gi();m=gi();
  fp(i,1,n) a[i]=gi(),mx=max(mx,a[i]),mn=min(mn,a[i]);
  fq(i,n,1) if(!R[a[i]]) R[a[i]]=i;
  fp(i,1,n) if(!L[a[i]]) L[a[i]]=i;
  fp(i,1,n)
    {
      if(a[i]==0)
    {
      if(mx<m) a[i]=m,mx=m;
      else if(Q.size()) a[i]=*--Q.end();
      else a[i]=1;
    }
      else
    {
      if(L[a[i]]==i&&L[a[i]]<R[a[i]]) Q.insert(a[i]);
      if(R[a[i]]==i&&L[a[i]]<R[a[i]]) Q.erase(a[i]);
      if(Q.size()) if(a[i]<(*--Q.end())) {puts("NO");return 0;}
    }
    }
  if(mx<m) {puts("NO");return 0;}
  puts("YES");
  fp(i,1,n) printf("%d ",a[i]);puts("");
  return 0;
}