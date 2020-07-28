#include <cstdio>
#include<iostream>
#include<queue>
#include<sstream>
#define MAX 30001
std::priority_queue<int , std::vector<int> , std::greater<int> >Num;
std::string ans1 , ans2;
int K , M , L , R;
std::string sum(int a){
    std::stringstream ss;
    ss << a;
    std::string ans = ss.str();
    return ans;
}
int main(){
    Num.push(1); 
    scanf("%d%d",&K , &M);
    int Cnt = 0 ; 
    while(Cnt < K){
        int a = Num.top() * 2 + 1;
        int b = Num.top() * 4 + 5;
        ans1 += (sum(Num.top()));
        Num.pop(); 
        Num.push(a);
        Num.push(b);  
        ++Cnt;
    }
    std::cout << ans1 <<"\n"; 
    L = 0;R = M;
    int Maxx = 0;
    while(L <= R && R < ans1.length()){
        for(register int i = L ; i <= R ; i++){
            if((ans1[i] - '0') > Maxx) Maxx = (ans1[i] - '0') , L = i + 1;
        }
        ans2 += (sum(Maxx));
        R++;
        Maxx = 0;
    }
    std::cout<< ans2;
    return 0;
}