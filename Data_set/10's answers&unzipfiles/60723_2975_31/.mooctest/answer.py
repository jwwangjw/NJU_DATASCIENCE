#include<bits/stdc++.h>
using namespace std;
int main()
{
    char s[204];
    while(gets(s))  //gets可以有效地输入空格
    {
        sort(s,s+strlen(s));  
    cout<<s<<endl;
    }
}