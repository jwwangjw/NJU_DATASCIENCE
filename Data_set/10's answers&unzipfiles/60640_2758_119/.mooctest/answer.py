#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <ctime>
#include <map>
#include <queue>
#include <cstdlib>
#include <string>
#include <climits>
#include <set>
#include <vector>
#include <complex>
#define int long long
using namespace std;
inline int read(){
    int k=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){k=k*10+ch-'0';ch=getchar();}
    return k*f;
}
inline void write(int x){
    if(x<0){putchar('-');x=-x;}if(x>9)write(x/10);
    putchar(x%10+'0');
}
inline void writeln(int x){
    write(x);puts("");
}
const int MOD=10007,N=210;
int n,m,f[N][N],ans=0;
int c[200*N][210];
inline int C(int x,int y){
    return c[x][y];
}
signed main()
{
    n=read();m=read();
    c[0][0]=1;
    for(int i=1;i<=n*m;i++){
        c[i][0]=1;
        for(int j=1;j<=min(i,n);j++)c[i][j]=(c[i-1][j]+c[i-1][j-1])%MOD;
    }
    f[1][1]=1;int ans=0;
    for(int i=2;i<=n;i++)
        for(int j=1;j<min(i,n);j++){
            f[i][j]=0;
            for(int k=j/m;k<=min(i-j,n);k++){
                f[i][j]=(f[i][j]+f[i-j][k]*C(k*m,j)%MOD)%MOD;
            }
        }
    for(int j=1;j<=n;j++)ans=(ans+f[n][j])%MOD;
    writeln(ans);
    return 0;
}