#include <cstdio> 
#include <iostream>
#include <algorithm>
using namespace std;
const int maxm=1100000;
int a[maxm],b[maxm],c[maxm];
int num[3*maxm],cnt;
int tree[5][4*maxm];
int dp[5][maxm];
void updata(int id,int o,int l,int r,int ind,int ans)
{
    if(l==r)
    {
        tree[id][o]=max(tree[id][o],ans);
        return;
    }
    int mid=(l+r)>>1;
    if(ind<=mid)
     updata(id,(o<<1),l,mid,ind,ans);
    else
     updata(id,(o<<1)|1,mid+1,r,ind,ans);
    tree[id][o]=max(tree[id][(o<<1)],tree[id][(o<<1)|1]);
}
int ask(int id,int o,int l,int r,int ql,int qr)
{
    if(ql>r||qr<l) return -1;
    if(ql<=l&&qr>=r) return tree[id][o];
    int mid=l+((r-l)>>1);
    int p1=ask(id,(o<<1),l,mid,ql,qr);
    int p2=ask(id,(o<<1)+1,mid+1,r,ql,qr);
    return max(p1,p2);
}
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
     scanf("%d",&a[i]),num[++cnt]=a[i];
    for(int i=1;i<=n;i++)
     scanf("%d",&b[i]),num[++cnt]=b[i];
    for(int i=1;i<=n;i++)
     scanf("%d",&c[i]),num[++cnt]=c[i];
    sort(num+1,num+cnt+1);
    int t=unique(num+1,num+cnt+1)-num-1;//离散化
    for(int i=1;i<=n;i++)
     a[i]=lower_bound(num+1,num+t+1,a[i])-num;
    for(int i=1;i<=n;i++)
     b[i]=lower_bound(num+1,num+t+1,b[i])-num;
    for(int i=1;i<=n;i++)
     c[i]=lower_bound(num+1,num+t+1,c[i])-num;//还原大小关系
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=4;j++)
         dp[1][i]=max(dp[1][i],ask(j,1,1,t,1,a[i]));
        for(int j=1;j<=4;j++)
         dp[2][i]=max(dp[2][i],ask(j,1,1,t,b[i],t));
        dp[3][i]=max(dp[3][i],ask(1,1,1,t,1,c[i]));
        dp[3][i]=max(dp[3][i],ask(2,1,1,t,1,c[i]));
        dp[3][i]=max(dp[3][i],ask(3,1,1,t,1,c[i]));
        dp[4][i]=max(dp[4][i],ask(1,1,1,t,c[i],t));
        dp[4][i]=max(dp[4][i],ask(2,1,1,t,c[i],t));
        dp[4][i]=max(dp[4][i],ask(4,1,1,t,c[i],t));
        dp[1][i]++,dp[2][i]++,dp[3][i]++,dp[4][i]++;
        updata(1,1,1,t,a[i],dp[1][i]);
        updata(2,1,1,t,b[i],dp[2][i]);
        updata(3,1,1,t,c[i],dp[3][i]);
        updata(4,1,1,t,c[i],dp[4][i]);//更新线段树的值。
    }
    int ans=0;
    for(int j=1;j<=n;j++)
     for(int i=1;i<=4;i++)
     ans=max(ans,dp[i][j]);//找最大的
    printf("%d",ans);
}