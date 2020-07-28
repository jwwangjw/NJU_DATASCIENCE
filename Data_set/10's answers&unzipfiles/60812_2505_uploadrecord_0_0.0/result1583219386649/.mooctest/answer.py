#include<bits/stdc++.h>
using namespace std;
const int maxn = 100005;
int sum[maxn];

void build(int p){            //建树不多说
    int v;
    cin >> v;
    if(v == -1) return;
    sum[p] += v;
    build(p - 1);
    build(p + 1);   
}

bool init(){               //输入
    int v;
    cin >> v;
    if(v == -1) return false;
    memset(sum,0,sizeof(sum));    
    int p = maxn/2;          //树根的水平位置  
    sum[p] = v;
    build(p - 1);
    build(p + 1);   
    return 1;
}

int main(){
    int kase = 0;
    while(init()){
        int p = 0;
        while(!sum[p]) p++;  //向左找最左边的孩子
        cout << "Case " << ++kase << ':' << endl << sum[p++];
        //避免行末多余空格
        while(sum[p]) cout << " " << sum[p++];
        cout << endl << endl;//UVa的非正常输出2333     
    } 
    return 0;
}