#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
const int Mn(200050),Mm(10050);
inline int lb(const int& x) { return x&(-x); }  //lowbit
int a[Mn],b[Mn],p[Mn],c[Mn];    //a是所有数, c为树状数组
bool _cmp(int x,int y)  //离散化时使用
{ return a[x]==a[y] ? x<y : a[x]<a[y]; }
struct opr
{
    int opt,n;
}o[Mm]; //存下所有操作
int main()
{
    int n,m;    //依照题意
    scanf("%d",&n);
    for(int i(1);i<=n;++i)
    {
        scanf("%d",a+i);
        b[i] = i;   //b代表了排序第i的数在a数列的位置
    }
    scanf("%d",&m);
    int ar(n);  //a数列的长度
    for(int i(1);i<=m;++i)
    {
        string s;
        cin >> s;   //读取操作
        if(s[0]=='a')
        {
            scanf("%d",&(o[i].n));
            a[++ar] = o[i].n;
            b[ar] = ar;
            o[i].opt = 1;   //add操作记为1
        }
        if(s[0]=='m')
            o[i].opt = 0;   //mid操作记为2
    }
    sort(b+1,b+ar+1,_cmp);
    for(int i(1);i<=ar;++i)
        p[b[i]] = i;    //p为a数列中第i个数的排序
    for(int i(1);i<=n;++i)
        for(int j(p[i]);j<=ar;j+=lb(j)) ++c[j]; //树状数组修改
    int cnt(n);
    for(int i(1);i<=m;++i)
    {
        if(o[i].opt)
        {
            ++cnt;
            for(int j(p[cnt]);j<=ar;j+=lb(j)) ++c[j];
        }
        else
        {
            int tar((cnt+1)/2); //搜索目标
            int l(1),r(ar);
            /*----二分搜索----*/
            while(r-l>3)
            {
                int mid((l+r)>>1);
                int ans(0);
                for(int j(mid);j;j-=lb(j))  ans += c[j];
                if(ans<tar) l = mid+1;
                else    r = mid;    
            }
            for(;l<=r;++l)
            {
                int ans(0);
                for(int j(l);j;j-=lb(j))    ans += c[j];
                if(ans==tar)    break;
            }
            /*----------------*/
            cout << a[b[l]] << endl;    //输出中位数
        }
    }
    return 0;
}