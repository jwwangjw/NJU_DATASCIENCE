#include<bits/stdc++.h>
using namespace std;
string s;
int a[101],st,i,num,sum,w;
bool flag;
int main()
{   cin>>s>>st;//输入
    for(i=0;i<s.size();i++)
    {num=s[i]-'A'+st;//算出数
    w=10000,flag=0;
    while(w){
        if(num>=w) flag=1;
        if(flag) a[++sum]=num/w;
        num=num%w;
        w/=10; 
    }   }//正序存储
    while(sum>2){
        if(sum==3&&a[1]==1&&a[2]==0&&a[3]==0){
            cout<<100; return 0;
        }//特判（如果是100 直接输出）
        for(i=1;i<sum;i++)
        a[i]=(a[i]+a[i+1])%10;//和取个位
        sum--;            //位数减一
    }
    if(sum==1) cout<<a[1];//特判，如果只有一位就只输出一位
    else cout<<a[1]*10+a[2];//否则输出正常的数（这里这样写可以去前导0）
    return 0;
}