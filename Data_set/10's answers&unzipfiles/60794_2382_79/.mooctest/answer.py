#include<iostream>
#include<algorithm>
using namespace std;
int n,st,ov;
struct node //结构体存区间 
{
    int lo,hi;
}a[50000+10];
bool cmp(node a,node b) //排序 
{
    return a.lo<b.lo;
}
int main()
{
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a[i].lo>>a[i].hi;
    sort(a+1,a+n+1,cmp);
    st=a[1].lo;
    ov=a[1].hi; //答案区间初始化 
    for(int i=2;i<=n;i++)
    {
        if(a[i].lo>ov) //开新区间 
        {
            cout<<st<<" "<<ov<<endl;
            st=a[i].lo;
            ov=max(ov,a[i].hi);
        }
        else ov=max(ov,a[i].hi); //扩展原有区间 
        if(i==n) cout<<st<<" "<<ov<<endl; //注意点3 
    }
    return 0;
 }