#include<bits/stdc++.h>
using namespace std;
struct node
{
    int l,r,sz,pri,val;
}tree[150005];
int tot=0,root,m,q;
int newnode(int x)
{
    tree[++tot].val=x;
    tree[tot].pri=rand();
    tree[tot].sz=1;
    return tot;
}
void pushup(int u)
{
    tree[u].sz=tree[tree[u].l].sz+tree[tree[u].r].sz+1;
}
void split(int u,int x,int &l,int &r)
{
    if(!u)
    {
        l=r=0;
        return;
    }
    if(tree[u].val<=x)
    {
        l=u;
        split(tree[u].r,x,tree[u].r,r);
    }
    else
    {
        r=u;
        split(tree[u].l,x,l,tree[u].l);
    }
    pushup(u);
}
int merge(int l,int r)
{
    if(!l||!r)return l+r;
    if(tree[l].pri<tree[r].pri)
    {
        tree[l].r=merge(tree[l].r,r);
        pushup(l);
        return l;
    }
    else
    {
        tree[r].l=merge(l,tree[r].l);
        pushup(r);
        return r;
    }
}
int kth(int u,int rank)
{
    while(1)
    {
        if(rank<=tree[tree[u].l].sz)
        {
            u=tree[u].l;
        }
        else if(rank==tree[tree[u].l].sz+1)
        {
            return tree[u].val;
        }
        else
        {
            rank=rank-tree[tree[u].l].sz-1;
            u=tree[u].r;
        }
    }
}
void ins(int x)
{
    int L,R;
    split(root,x,L,R);
    root=merge(merge(L,newnode(x)),R);
}
int main()
{
    srand(19260817);
    scanf("%d%d",&m,&q);
    for(int i=1;i<=m;++i)
    {
        int v;
        scanf("%d",&v);
        ins(v);
    }
    for(int i=1;i<=q;++i)
    {
        int c,n;
        scanf("%d%d",&c,&n);
        if(c==1)
        {
            printf("%d\n",kth(root,tree[root].sz-n+1));
        }
        if(c==2)
        {
            ins(n);
        }
    }
    return 0;
}