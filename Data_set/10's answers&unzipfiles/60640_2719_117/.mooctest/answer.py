#include<cstdio>
#include<iostream>
#include<algorithm>
#include<set>
using namespace std;
struct Plan{
    int l,r;
    bool operator <(const Plan &rhs)const{
        return r<rhs.l;
    }
};
int T;
set<Plan> s;
int main(){
    cin>>T;
    while(T--){
        char c; scanf(" %c",&c); //空格可以防止读入无效字符
        if(c=='A'){
            int l,r,cnt=0; scanf("%d %d",&l,&r);
            Plan tmp=(Plan){l,r};
            //删掉与该预约冲突的预约，并统计个数
            set<Plan>::iterator it=s.find(tmp);
            while(it!=s.end()){
                ++cnt; s.erase(it);
                it=s.find(tmp);
            }
            s.insert(tmp);
            printf("%d\n",cnt);
        }
        else{
            printf("%d\n",s.size());
        }
    }
    return 0;
}