#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN=(1<<17)-1;

int n,m,ans;
int a[MAXN],tree[MAXN<<1],add[MAXN<<1];
struct lint{
    int l,r;
}line[MAXN];

void build(int k,int l,int r){
    if(l==r){
        tree[k]=a[l];
        return;
    }int i=k<<1,mid=l+r>>1;
    build(i,l,mid);
    build(i|1,mid+1,r);
    tree[k]=min(tree[i],tree[i|1]);
}

bool cmp(lint a,lint b){
    if(a.r==b.r) return a.l>b.l;
    return a.r<b.r;
}

void cadd(int k,int l,int r,int le,int ri,int x){
    if(le<=l&&r<=ri){
        tree[k]+=x;
        add[k]+=x;
        return;
    }int i=k<<1,mid=l+r>>1;
    if(le<=mid) cadd(i,l,mid,le,ri,x);
    if(mid<ri) cadd(i|1,mid+1,r,le,ri,x);
    tree[k]=min(tree[i],tree[i|1])+add[k];
}

int ask(int k,int l,int r,int le,int ri,int x){
    if(le<=l&&r<=ri) return tree[k]+x;
    int i=k<<1,mid=l+r>>1;
    int num=MAXN;
    if(le<=mid) num=min(num,ask(i,l,mid,le,ri,x+add[k]));
    if(mid<ri) num=min(num,ask(i|1,mid+1,r,le,ri,x+add[k]));
    return num;
}

void init(){
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;++i){
        scanf("%d",&a[i]);
    }build(1,1,n);
    for(int i=1;i<=m;++i){
        scanf("%d%d",&line[i].l,&line[i].r);
    }sort(line+1,line+m+1,cmp);
    return;
}

void solve(){
    for(int i=1;i<=m;++i){
        if(ask(1,1,n,line[i].l,line[i].r,0)>0){
            ++ans;
            cadd(1,1,n,line[i].l,line[i].r,-1);
        }
    }return;
}

void write(){
    printf("%d\n",ans);
    return;
}

int main(){
    init();
    solve();
    write();
    return 0;
}