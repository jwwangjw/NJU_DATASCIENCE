#include<bits/stdc++.h>
using namespace std;
struct node
{
    int l,r;int size,rnd,v;
}t[500005*50];
int cnt,rt[500005];
void update(int k)
{
    t[k].size=t[t[k].l].size+t[t[k].r].size+1;
}
void newnode(int &k,int x)
{
    t[k=++cnt].v=x;t[k].size=1;t[k].rnd=rand();
}
int merge(int a,int b)
{
    if(!a||!b)return a+b;
    if(t[a].rnd>t[b].rnd)
    {
        int p=++cnt;t[p]=t[a];
        t[p].r=merge(t[p].r,b);
        update(p);return p;
    }
    else
    {
        int p=++cnt;t[p]=t[b];
        t[p].l=merge(a,t[p].l);
        update(p);return p;
    }
}
void split(int now,int k,int &x,int &y)
{
    if(!now)x=y=0;
    else
    {
        if(t[now].v<=k)
        {
            x=++cnt;t[x]=t[now];
            split(t[x].r,k,t[x].r,y);
            update(x);
        }
        else 
        {
            y=++cnt;t[y]=t[now];
            split(t[y].l,k,x,t[y].l);
            update(y);
        }
    }
}
void Delete(int &root,int w)
{
    int x=0,y=0,z=0;
    split(root,w,x,z);
    split(x,w-1,x,y);
    y=merge(t[y].l,t[y].r);
    root=merge(merge(x,y),z);
}
void Insert(int &root,int w)
{
    int x=0,y=0,z=0;
    split(root,w,x,y);
    newnode(z,w);
    root=merge(merge(x,z),y);
}
int getval(int k,int w)
{
    if(w==t[t[k].l].size+1)return t[k].v;
    else if(w<=t[t[k].l].size)return getval(t[k].l,w);
    else return getval(t[k].r,w-t[t[k].l].size-1);
}
int getkth(int &root,int w)
{
    int x,y;
    split(root,w-1,x,y);
    int ans=t[x].size+1;
    root=merge(x,y);
    return ans;
}
int getpre(int &root,int w)
{
    int x,y,k,ans;
    split(root,w-1,x,y);
    if(!x)return -2147483647;
    k=t[x].size;
    ans=getval(x,k);
    root=merge(x,y);
    return ans;
}
int getnex(int &root,int w)
{
    int x,y,ans;
    split(root,w,x,y);
    if(!y)return 2147483647;
    else ans=getval(y,1);
    root=merge(x,y);
    return ans;
}
int main()
{
    int n,f,w,tim;
    scanf("%d",&n);
    for(int i=1;i<=n;++i)
    {
        scanf("%d%d%d",&tim,&f,&w);
        rt[i]=rt[tim];
        if(f==1)Insert(rt[i],w);
        else if(f==2)Delete(rt[i],w);
        else if(f==3)printf("%d\n",getkth(rt[i],w));
        else if(f==4)printf("%d\n",getval(rt[i],w));
        else if(f==5)printf("%d\n",getpre(rt[i],w));
        else printf("%d\n",getnex(rt[i],w));
    }
    return 0;
}