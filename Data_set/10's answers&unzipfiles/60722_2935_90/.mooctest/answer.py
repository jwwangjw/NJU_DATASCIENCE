#include<iostream>
using namespace std;
int ans,t,q[100];
string s;
int main(){
    cin>>s;
    for(int i=0;i<s.size();++i)q[i]=s[i]=='Q'?++t:t;
    for(int i=0;i<s.size();++i)if(s[i]=='A')ans+=q[i]*(t-q[i]);
    cout<<ans;
}