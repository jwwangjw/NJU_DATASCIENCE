#include<bits/stdc++.h>
using namespace std;
int n,mi=0x7f7f7f7f;      //0x7f7f7f7f是一个很大的数，int在正数里的最大值 
int jian(int x,int y)     //进行取模运算的函数 
{
    while(x>y)
    {
        x-=y;
    }
    return x;
}
int ci(int x,int y)       //计算次数的函数 
{
    int cii=0;
    while(x>y)
    {
        x-=y;
        cii++;
    }
    return cii;
}
int dfs(int a,int b,int step)
{
    if(a>b)dfs(jian(a,b),b,step+ci(a,b));
    else if(a<b)dfs(a,jian(b,a),step+ci(b,a));
    else if(a==b&&a!=1)return 0x7f7f7f7f;//如果还原不了就返回一个大数 
    else return step;
}
int main()
{
    cin>>n;
    for(int i=1;i<=n;i++)               //从1到n的枚举 
    {
        mi=min(mi,dfs(n,i,0));          //取最优答案 
    }
    cout<<mi;
}