#include<iostream>
using namespace std;
int a[101];//如果你的第一个数存储在a[1]里,一定要多开一两个空间 ，以防越界访问
int top=0,c;
int main(){
    while(1){
        cin>>c;
        if(c==0) break;
        a[++top]=c;
        /*
        或者写成：
        top++;
        a[top]=c;
        个人比较喜欢压码……
        */ 
    }
    while(top!=0){
        cout<<a[top--]<<" ";
        /*
        或者写成：
        cout<<a[top];
        top--;
        */ 
    }
    return 0;
} 