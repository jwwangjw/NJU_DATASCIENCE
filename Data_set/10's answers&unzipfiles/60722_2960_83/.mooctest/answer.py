#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
#include<math.h>
using namespace std;

const int N=2e6+5;
const int mod=998244353;
const int sqr=3;
const int sqrinv=332748118;

int n,m,a[N],b[N],r[N];
int limit=1,lg,ans[N],vis[N];
char s[N],t[N];

void write(int x)
{
    if(!x) return;
    write(x/10),putchar(x%10+'0');
}

int F_p(int x,int y)
{
    int bas=x,ret=1;
    while(y)
    {
        if(y&1) ret=1LL*ret*bas%mod;
        bas=1LL*bas*bas%mod;
        y>>=1;
    }
    return ret;
}

int solve_complex(int x,int tp)
{
    if(~tp) return F_p(sqr,x);
    else return F_p(sqrinv,x);
}

void NTT(int *A,int tp)
{
    int i;
    for(i=0;i<limit;++i)
        if(i<r[i])
            swap(A[i],A[r[i]]);

    int len,j,k;
    for(len=1;len<limit;len<<=1)
    {
        int wn=solve_complex((mod-1)/(2*len),tp);
        for(j=0;j<limit;j+=len<<1)
        {
            int w=1;
            for(k=0;k<len;++k,w=1LL*w*wn%mod)
            {
                int x=A[j+k];
                int y=1LL*w*A[j+k+len]%mod;
                A[j+k]=x+y,A[j+k+len]=x-y;
                if(A[j+k]>=mod) A[j+k]-=mod;
                if(A[j+k+len]<0) A[j+k+len]+=mod; 
            }
        }
    }
}

void calc(char op)
{
    int i;
    for(i=1;i<=m;++i) b[i]=(t[m+1-i]==op);
    for(i=1;i<=n;++i) a[i]=((s[i]==op)|(s[i]=='*'));

    for(i=m+1;i<limit;++i) b[i]=0;
    for(i=n+1;i<limit;++i) a[i]=0;
    a[0]=b[0]=0;

    NTT(a,1),NTT(b,1);
    for(i=0;i<limit;++i) a[i]=1LL*a[i]*b[i]%mod;
    NTT(a,-1);

    int tt=F_p(limit,mod-2);
    for(i=0;i<limit;++i) ans[i]+=1LL*a[i]*tt%mod;
}

void init()
{
    int i,cnt=0,totans=0;
    scanf("%d%d",&m,&n);
    scanf("%s",t+1);
    scanf("%s",s+1);
    for(i=1;i<=m;++i) vis[t[i]]=1;

    while(limit<=n+m) limit<<=1,++lg;
    for(i=0;i<limit;++i) r[i]=(r[i>>1]>>1)|((i&1)<<(lg-1));
    for(i='a';i<='z';++i) if(vis[i]) calc(i);
    for(i=1;i<=m;++i) if(t[i]!='*') ++cnt;

    for(i=m+1;i<=n+m;++i)
        if(ans[i]==cnt)
            ++totans;

    write(totans),putchar('\n');
    for(i=m+1;i<=n+m;++i)
        if(ans[i]==cnt)
            write(i-m),putchar(' ');
    putchar('\n');
}

int main()
{
//  freopen("string.in","r",stdin);
//  freopen("string.out","w",stdout);
    init();
    return 0;
}