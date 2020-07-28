#include<bits/stdc++.h>
#define ts cout<<"ok"<<endl
#define ll long long
#define hh puts("")
using namespace std;
int n,c,tot,f[200005],g[200005];
struct node{
    int sc,mn;
}a[200005];
priority_queue<int> q;
inline int read(){
    int ret=0,ff=1;char ch=getchar();
    while(!isdigit(ch)){if(ch=='-') ff=-ff;ch=getchar();}
    while(isdigit(ch)){ret=ret*10+(ch^48);ch=getchar();}
    return ret*ff;
}
inline bool cmp(node A,node B){
    return A.sc<B.sc;
}
signed main(){
    n=read(),c=read(),tot=read();
    for(int i=1;i<=c;i++){
        a[i].sc=read();
        a[i].mn=read();
    }
    sort(a+1,a+c+1,cmp);
    int sum=0;
    for(int i=1;i<=n/2;i++){
        q.push(a[i].mn);
        sum+=a[i].mn;
    }
    for(int i=n/2+1;i<=c-n/2;i++){
        f[i]=sum;
        if(a[i].mn<q.top()){
            sum-=q.top();
            sum+=a[i].mn;
            q.pop();
            q.push(a[i].mn);
        }
    }
    while(!q.empty()) q.pop();
    sum=0;
    for(int i=c;i>=c-n/2+1;i--){
        q.push(a[i].mn);
        sum+=a[i].mn;
    }
    for(int i=c-n/2;i>=n/2+1;i--){
        g[i]=sum;
        if(a[i].mn<q.top()){
            sum-=q.top();
            sum+=a[i].mn;
            q.pop();
            q.push(a[i].mn);
        }
    }
    for(int i=c-n/2;i>=n/2+1;i--){
        if(f[i]+g[i]+a[i].mn<=tot){
            printf("%d",a[i].sc);
            return 0;
        }
    }
    printf("-1");
    return 0;
}