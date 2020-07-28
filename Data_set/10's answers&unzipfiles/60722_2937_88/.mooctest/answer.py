#include<iostream>
using namespace std;
char a[16], b[16] = {'C', 'O', 'D', 'E', 'F', 'E', 'S', 'T', 'I', 'V', 'A', 'L', '2', '0', '1', '6'};//直接字符数组走一波，后面比较方便
int ans;//定义ans为答案/在函数外面定义的全局变量初始值默认为0
int main()
{
    cin >> a;//不需要一个字符一个字符的输，题目数据全都是16位的，不用担心超界限
    for(int i = 0; i < 16; i ++){
        if(a[i] != b[i]) ans ++;//循环比较，如果不一样ans+1
    }
    cout << ans << endl;//endl可以不加
    return 0;//养成好习惯
}