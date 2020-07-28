#include<iostream>
#include<cstdio>
#include<cstring>
#define int long long
using namespace std;
typedef struct _int{int len;
    _int(){
        len=1;
    }
    int data[1000];//9位一个 
    void init(){
        len=1;
        for(register int i=0;i<1000;i++)data[i]=0;
    }
    void print(){
        //printf("%lld",data[len-1]);
        for(register int i=len-1;i>=0;i--){
            printf("%.1lld",data[i]);
        }
    }
}INT;
void add(_int &a,_int &b,_int &c){
        //c.init();
        unsigned long long cf=0;
        int newl=max(a.len,b.len)+50;
        //a.print();printf("+");b.print();printf("=");
        for(register int i=0;i<newl;i++){
            unsigned long long res=a.data[i]+b.data[i]+cf;
            c.data[i]=res%10;cf=res/10;
        }
        while(newl>1&&c.data[newl-1]==0)newl--;c.len=newl;
        //c.print();cout<<endl;
}
void mul(_int &a,_int &b,_int &c){
    int newl=a.len+b.len+10;
    for(register int i=1;i<=a.len+10;i++){
        unsigned long long cf=0;
        unsigned long long tmp=a.data[i-1];
        for(register int j=1;j<=b.len+10;j++){
            unsigned long long res=(tmp*b.data[j-1])+cf+c.data[i+j-2];
            c.data[i+j-2]=res%10;
            cf=res/10;
        }
    }
    while(newl>1&&c.data[newl-1]==0)newl--;
    c.len=newl;
}
INT C[33][33];
INT dp[17];
INT mi[17][33];
INT g[17];
INT gmi[17][33];
signed main(){
    int n,d;cin>>n>>d;
    C[0][0].data[0]=1;
    for(register int i=1;i<=n;i++){
        C[i][0].data[0]=1;
        for(register int j=1;j<=i;j++){
            //printf("add(C[%d][%d],c[%d],[%d])--",i-1,j,i-1,j-1);C[i-1][j].print();printf("+");C[i-1][j-1].print();
            //cout<<endl;
            add(C[i-1][j],C[i-1][j-1],C[i][j]);
        }
    }
    dp[0].data[0]=1;
    g[0].data[0]=1;
    dp[1].data[0]=1;
    g[1].data[0]=2;
    gmi[1][0].data[0]=1;
    for(register int i=0;i<=n;i++){
        mi[0][i].data[0]=gmi[0][i].data[0]=mi[1][i].data[0]=1;
        if(i>0)mul(gmi[1][i-1],g[1],gmi[1][i]);
    }
    for(register int i=2;i<=d;i++){
        INT tmp;tmp.init();
        for(register int j=1;j<=n;j++){
            INT cjr=C[n][j];
            INT ywy;ywy.init();mul(cjr,mi[i-1][j],ywy);
            cjr.init();mul(ywy,gmi[i-2][n-j],cjr);
            ywy=tmp;tmp.init();add(cjr,ywy,tmp);
        }
        dp[i]=tmp;
        add(g[i-1],dp[i],g[i]);
        gmi[i][0].data[0]=1;
        mi[i][0].data[0]=1;
        for(register int j=1;j<=n;j++){
            mul(gmi[i][j-1],g[i],gmi[i][j]);
            mul(mi[i][j-1],dp[i],mi[i][j]);
        }
    }
    dp[d].print();
    return(0);
} 
