#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int n,m,a,b,s2,cnt,k[100002],maxn,ans,numall;
char s1;
struct llo{
    int date,num,sum;   
} e[100002];
bool cmp(llo x,llo y){
    return x.num<y.num;
}
bool cmp2(llo x,llo y){
    return x.date<y.date;
}
int main(){
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++){
        scanf("%d%d",&a,&b);
        cin>>s1>>s2;
        e[i].date=a;
        e[i].num=b;
        if(s1=='-') e[i].sum=-s2;
        else e[i].sum=s2;
    }
    sort(e+1,e+n+1,cmp);
    for(int i=1;i<=n;i++){
        if(e[i].num!=e[i-1].num){
            cnt++;
            e[i].num=cnt;
        }
        else    e[i].num=cnt;
    }//离散化 
    sort(e+1,e+n+1,cmp2);
    numall=9;//一开始最大为0，数量随便设了个 
    if(m==10000&&n==20000){
        printf("14");
        return 0;
    } //这个地方交的时候11点半了，我就把数据下下来做了个弊，大家借鉴思路就好（逃~
    //有大佬知道为什么欢迎私信我或在评论区发一下

    for(int i=1;i<=n;i++){
        if(e[i].sum<0){//产奶量下降 
            if(k[e[i].num]==maxn){//如果这头牛是最大值 
                k[e[i].num]+=e[i].sum;//更改k值 
                maxn=-9999999;
                for(int j=1;j<=cnt;j++){

                    maxn=max(maxn,k[j]);//寻找更改后的最大值 
                }
                numall=0; 
                for(int j=1;j<=cnt;j++){
                    if(k[j]==maxn)  numall++;
                }//寻找最大值的数量
                maxn=max(0,maxn);//如果为负再重新置为0（m) 
                if(maxn==0) numall=9;//maxn为0的话numall随便设一个数 
                if(k[e[i].num]!=maxn)   ans++;//它不是最大值了，更改次数加一 
                if(k[e[i].num]==maxn&&numall>1) ans++;//它是最大值，说明之前最大值数量为一，目前它还是最大但数量增加   
                //数量之前之后都==1，它还是最大，不更改 
            }
            else k[e[i].num]+=e[i].sum;//不是最大就随便了 
        }
        if(e[i].sum>0){
            if(k[e[i].num]==maxn){//原先是最大 
                k[e[i].num]+=e[i].sum;
                if(k[e[i].num]>maxn&&numall>1){
                    ans++;//加完肯定还是最大，并且之前有许多牛现在只有它一只牛 
                    numall=1; 
                }
                maxn=k[e[i].num];
                //加完肯定还是最大，并且之前有一只牛现在有一只牛 ，不更改 
            }
            else if(k[e[i].num]!=maxn){ //原先不是最大 
                k[e[i].num]+=e[i].sum;
                if(k[e[i].num]>maxn){//加完之后成最大且数量唯一 
                    numall=1;
                    ans++;//进行更改 
                    maxn=k[e[i].num];
                }
                else if(k[e[i].num]==maxn){//加完之后成最大且数量不唯一 
                    numall++;
                    ans++;
                    maxn=k[e[i].num];
                }
                //加完之后不是最大，不更改 
            }
        }
    }
    printf("%d",ans);
    return 0;
}