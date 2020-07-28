#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
struct stu{
    int lc,rc;
    long long int ans,tag;
};
stu tree[500050];
int k=1;
int n,q;
void build(int l,int r,int nu)//我平时所用的建树方式 
{
    tree[nu].ans=0x7f7f7f7f;//赋初值为0x7f7f7f7f 
    if (l==r)
    {
        return;
    }
    int mid=(l+r)/2;
    k++;
    tree[nu].lc=k;
    build(l,mid,tree[nu].lc);
    k++;
    tree[nu].rc=k;
    build(mid+1,r,tree[nu].rc);
}
void update(int l,int r,int ll,int u,long long int v)//线段树单点修改 
{
    if (l==ll&&r==ll)
    {
        tree[u].ans=v;
        return;
    }
    int mid=(l+r)/2;
    if (ll<=mid)
    {
        update(l,mid,ll,tree[u].lc,v);
    }
    else
    {
        update(mid+1,r,ll,tree[u].rc,v);
    }
    tree[u].ans=min(tree[tree[u].lc].ans,tree[tree[u].rc].ans);//维护最早下车的在哪里下车 
}
int quary(int l,int r,int ll,int rr,int u,long long int v)//线段树区间查询 
{
    if (l==r)
    {
        return l;//返回年龄 
    }
    int mid=(l+r)/2;
    if (rr<=mid)//线段树的区间查询方式 
    {
        if (tree[tree[u].lc].ans>v)//找不出合适的人就返回0x7f7f7f 
        {
            return 0x7f7f7f;
        }
        else
        {
            return quary(l,mid,ll,rr,tree[u].lc,v);
        }
    }
    else if (ll>mid)//同上 
    {
        if (tree[tree[u].rc].ans>v)
        {
            return 0x7f7f7f;
        }
        else return quary(mid+1,r,ll,rr,tree[u].rc,v);
    }
    else
    {
        int a1=0x7f7f7f,a2=0x7f7f7f;
        if (tree[tree[u].lc].ans<=v)//先找左区间 
        {
            a1=quary(l,mid,ll,mid,tree[u].lc,v);
        }
        if (tree[tree[u].rc].ans<=v&&a1==0x7f7f7f)//左区间实在是没有合适的人了再找右区间 
        {
            a2=quary(mid+1,r,mid+1,rr,tree[u].rc,v);
        }
        return min(a1,a2);
    }
}
int main()
{
   // freopen("deda.in","r",stdin);
   // freopen("deda.out","w",stdout);
    scanf("%d%d",&n,&q);
    build(1,n,1);//建树 
    for (int i=1;i<=q;i++)
    {
        char flag[1];
        long long int X;
        int B; 
        scanf("%s%lld%d",flag,&X,&B);
        if (flag[0]=='M')
        {
            update(1,n,B,1,X);
        }
        else
        {
            int lll=quary(1,n,B,n,1,X);//区间查询年龄从B到 N（年龄的最大值）的人。 
            if (lll==0x7f7f7f)//没有符合条件的人就输出-1； 
            {
                printf("-1\n");
            }
            else
            {
                printf("%d\n",lll);
            }
        }
    }
    return 0;
}