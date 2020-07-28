#include<bits/stdc++.h>
#define max 11
using namespace std;
int select(char a[],int n,char b[],int m) {
    int flag=2;   //设置默认值flag=2 
    if(n!=m) {
        flag=1;     //如果长度不等则返回1 
        return flag;   
    } else {
        for(int i=0; i<n; i++) {
            if(a[i]!=b[i]) {
                if(a[i]>='A' && a[i]<='Z') {      //将大小写转换，至双方全部变成小写字母 
                    a[i]=a[i]+32;
                } else if(b[i]>='A' && b[i]<='Z') {
                    b[i]=b[i]+32;
                }
 
                if(a[i]==b[i]) {       //变成小写字母之后如果两个字符串任然相等则返回3 
                    flag=3;
                    return flag;
                } else if(a[i]!=b[i]) {  //变成小写字母之后如果两个字符 -- 
                    flag=4;             //串任然不相等则说明字母不同，此时返回4 
                    return flag;
                }
            }
        }
    }
    return flag;       //上面一切条件都不满足，则说明两字符串完全相等，返回默认值2 
}
 
 
int main() {
    char a[max],b[max];
    int n,m;
    scanf("%s%s",a,b);  //可以用这样的输入直接让sacnf吃掉那个回车 
    n=strlen(a);
    m=strlen(b);
    cout<<select(a,n,b,m)<<endl;    //利用返回值直接输出 
    return 0;
}