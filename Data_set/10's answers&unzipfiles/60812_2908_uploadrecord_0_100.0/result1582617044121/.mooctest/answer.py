#include<algorithm>
#include<iostream>
#include<map>
using namespace std;
map<string,bool>z;//存储字符串是否出现过
string a;
int n,sum;
int main(){
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>a;
        sort(a.begin(),a.end());//排序
        if(!z[a]){//如果没有出现过，组数+1
            sum++;
            z[a]=1;
        }
    }
    cout<<sum;
    return 0;
}