#include <stdio.h>
#include <string.h>
#define Clean(X,K) memset(X,K,sizeof(X))
using namespace std ;
#include <iostream>
const int Maxn = 2000005 , Base = 26 ;
int N , Tail = 0 , T[Maxn][Base] , End[Maxn] , Tot = 0 , Len[Maxn];
unsigned long long HashValue[Maxn] , HashBase = 17 , HashPow[Maxn] = {1} , Ans = 0;
char S[Maxn * 2] , Tmp[Maxn];
int Add (int From ) {
int P = 0 ,R = 1 ;
unsigned long long int NowHash = 0 , NowLen = 0;
for (int i = From ; S[i] != '0' ; ++ i) {
    if (!T[P][S[i] - 'a']) T[P][S[i] - 'a'] = ++ Tot;
    P = T[P][S[i] - 'a'] ;
    ++ R;
    NowHash = NowHash * HashBase + S[i] ;
    ++ NowLen ;
}
++ End[P] ;
Len[P] = NowLen , HashValue[P] = NowHash ;
return From + R ;
}
int NowP ;
void Ask (int P , int Now , int E ) {

if (Now > E) {
    NowP = P ;
    return ;
}
Ask (T[P][S[Now] - 'a'] , Now + 1 , E ) ;

if (End[P]) {
    if (HashValue[NowP] * HashPow[Len[P]] + HashValue[P] == HashValue[P] * HashPow[Len[NowP]] + HashValue[NowP]) {
        Ans += 2 ;
        if (P == NowP) -- Ans ;
    }
}
}

int main () {
//    freopen ("P3449.in" , "r" , stdin) ;
Clean (T , 0) , Clean (End , 0) , Clean (Len , 0);
scanf ("%d" , &N) ;
for (int i = 1 ; i <= N; ++ i) {
    int L ;
    scanf ("%d " , &L) ;
    scanf ("%s" , Tmp) ;
    for (int j = 0 ; j < L; ++ j) S[Tail + j] = Tmp[j] ;
    Tail += L ;
    S[Tail++] = '0' ;
}
-- Tail ;
int Now = 0 , Cnt = -1;
while (Now <= Tail) Now = Add (Now) ;
for (int i = 1 ; i < Maxn ; ++ i) HashPow[i] = HashPow[i - 1] * HashBase ;
int Lst = 0 ;
Cnt = -1 ;
for (int i = 1 ; i <= Tail ; ++ i)
    if (S[i] == '0') {
        Ask (0 , Lst , i - 1) ;
        Lst = i + 1 ;
    }
cout << Ans + N<<endl;
fclose (stdin) , fclose (stdout) ;
return 0 ;
}