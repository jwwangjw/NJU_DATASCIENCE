#include<iostream>
using namespace std;
int org[100005],delta[100005][2],n,m;
int lowbit(int x)
{
    return x&(-x);
}
void add(int pos,int k,int d)
{
    for(int i=pos;i<=n;i+=lowbit(i))
    {
        delta[i][0]+=k;
        delta[i][1]+=d;
        k+=d*lowbit(i);
    }
}
int sum(int pos)
{
    int s=0,x=pos;
    while(x)
    {
        s+=delta[x][0]+(pos-x)*delta[x][1];
        x-=lowbit(x);
    }
    return s;
}
int main()
{
    cin>>n>>m;
    for(int i=1;i<=n;i++)
     cin>>org[i];
    for(int i=1;i<=m;i++)
    {
        int q;
        cin>>q;
        if(q==1)
        {
            int l,r,k,d;
            cin>>l>>r>>k>>d;
            add(l,k,d);
            add(r+1,-k-(r+1-l)*d,-d);
        }
        else
        {
            int p;
            cin>>p;
            cout<<org[p]+sum(p)<<endl;
        }
    }
}