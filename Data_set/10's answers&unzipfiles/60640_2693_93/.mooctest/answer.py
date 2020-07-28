#include<cstdio>
#include<cstring>
#include<iostream>
#define Rg register
#define fp(i,a,b) for(Rg int i=(a),I=(b)+1;i<I;++i)
#define fd(i,a,b) for(Rg int i=(a),I=(b)-1;i>I;--i)
#define ll long long
using namespace std;
const int mod=998244353,M=53;
typedef int ARR[M][M];
char s[M]; ARR C,f,g,ans;
int n,one,zero,fac[M];
inline int mul(int x,int y){return 1ll*x*y%mod;}
inline void Pls(int& x,int y){if((x+=y)>=mod)x-=mod;}
inline int qpow(int x,int p){ Rg int s=1; if(p<=0) return 1;
    for(;p;p>>=1,x=mul(x,x)) if(p&1) s=mul(s,x); return s;
}
int main(){ scanf("%s",s+1),n=strlen(s+1);
    fp(i,1,n) if(s[i]==48) ++zero; else ++one;
    fac[0]=1; fp(i,1,n) fac[i]=mul(fac[i-1],i);
    fp(i,0,n) C[i][0]=1;
    fp(i,1,n) fp(j,1,n) C[i][j]=(C[i-1][j-1]+C[i-1][j])%mod;
    // i 个人构成 fake 圈， j 个人构成 fake 链 
    fp(i,1,n) fp(j,0,n-i) g[i][j]=mul(fac[i-1],mul(j?i:1,qpow(i+j,j-1)));
    // i 个人没有 fake ，j 个人 fake , a+b 个人构成 fake 圈，a 个人不 fake ，剩下的人构成 fake 链 
    fp(i,0,one) fp(j,0,zero) fp(a,0,i) for(Rg int b=0;b<=j;b+=2) if(a|b)
        Pls(f[i][j],mul(mul(C[i][a],C[j][b]),g[a+b][i+j-a-b]));
    ans[0][0]=1;
    fp(i,0,one) fp(j,0,zero) if(i|j){
        if(i) fp(a,1,i) fp(b,0,j) Pls(ans[i][j],mul(ans[i-a][j-b],mul(mul(C[i-1][a-1],C[j][b]),f[a][b])));
        else fp(b,1,j) Pls(ans[i][j],mul(ans[i][j-b],mul(mul(C[i][i],C[j-1][b-1]),f[i][b])));
    } return !printf("%d\n",ans[one][zero]);
}