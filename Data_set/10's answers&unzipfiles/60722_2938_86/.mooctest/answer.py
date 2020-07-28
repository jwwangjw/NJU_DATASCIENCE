#include<bits/stdc++.h>//头文件
using namespace std;
string a[100];//定义要排序的字符串数组
stringstream ss;//百度一下，你就知道
int main(){
    for(int i=1;i<=100;i++){//开始存入1-1000的数
        ss<<i;
        ss>>a[i-1];
        ss.str("");//清空缓存
        ss.clear();//充值(重置)状态
    }
    sort(a,a+100);//排序
    for(int i=0;i<100;i++)
    cout<<a[i]<<endl;//输出
    return 0;//完美结束
}