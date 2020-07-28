#include<iostream>
#include<cstdio>
#include<algorithm>//sort所需要的STL头文件
using namespace std;
int n,m,f[200],ans,x,sum;
struct lol{
    int from,to,val;//使用结构体存储边的两端点，长度
}l[20010];
bool cmp(lol a, lol b){
    return a.val<b.val;//sort排序设置边长为关键字
}
int find(int x){
    if (f[x]==x) return x;
    else return f[x]=find(f[x]);//并查集
}
void Kuskal(){
    int a,b;
    sort(l+1,l+1+m,cmp);//sort快排
    for (int i=1; i<=m; i++){
        a=find(l[i].from); b=find(l[i].to);//找两点的祖先
        if (a==b) continue;//ab在同一集合，即a，b点已连通，则跳过
        sum+=l[i].val;//记录长度
        f[a]=b;//合并
        x++;
        if (x==n) return;//边达到需要值，跳出函数
    }
}
int main(){
    int i;

    cin>>n>>m;

    for (i=1; i<=n; i++){
        f[i]=i;
    }
    for (i=1; i<=m; i++){
        scanf("%d%d%d",&l[i].from,&l[i].to,&l[i].val);
        ans+=l[i].val;//算总长
    }
    Kuskal();

    printf("%d",ans-sum);//输出

    return 0;
}