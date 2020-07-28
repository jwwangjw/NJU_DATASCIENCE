#include <cstdio>
bool a[20005];
int n,m,x;
int check() {//计算函数，虽然存在大量重复，但是本人懒得优化（毕竟数据那么水）
    int cans=1,ans=1;
    for(int i=2;i<=n;++i) { // 最大子段和
        if(a[i]!=a[i-1]) cans++;
        if(ans<cans) ans=cans;
        if(a[i]==a[i-1]) cans=1;
    }
    return ans;
}
int main() {
    scanf("%d %d",&n,&m);
    for(int i=1;i<=m;++i) {//暴力模拟不解释
        scanf("%d",&x);
        a[x]=!a[x];     //改变状态
        printf("%d\n",check());//输出
    }
    return 0;
}