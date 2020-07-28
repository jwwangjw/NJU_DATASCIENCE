#include <cstdio>
#include <iostream>

#define MAXN 150010
#define swap my_swap
#define ls S[x].Son[0]
#define rs S[x].Son[1]

using namespace std ;
struct Tree{
    int dis, val, Son[2], rt ;
}S[MAXN] ; int N, T, A, B, C, i ;

inline int Merge(int x, int y) ; 
int my_swap(int &x, int &y){ x ^= y ^= x ^= y ;}
inline int Get(int x){ return S[x].rt == x ? x : S[x].rt = Get(S[x].rt) ; }
inline void Pop(int x){ S[x].val = -1, S[ls].rt = ls, S[rs].rt = rs, S[x].rt = Merge(ls, rs) ; }
inline int Merge(int x, int y){
    if (!x || !y) return x + y ; if (S[x].val > S[y].val || (S[x].val == S[y].val && x > y)) swap(x, y) ;
    rs = Merge(rs, y) ; if (S[ls].dis < S[rs].dis) swap(ls, rs) ; S[ls].rt = S[rs].rt = S[x].rt = x, S[x].dis = S[rs].dis + 1 ; return x ;
}
int main(){
    cin >> N >> T ; S[0].dis = -1 ;
    for (i = 1 ; i <= N ; ++ i) 
        S[i].rt = i, scanf("%d", &S[i].val) ; 
    for (i = 1 ; i <= T ; ++ i){
        scanf("%d%d", &A, &B) ;
        if (A == 1){
            scanf("%d", &C) ;
            if (S[B].val == -1 || S[C].val == -1) continue ;
            int f1 = Get(B), f2 = Get(C) ; if (f1 != f2) S[f1].rt = S[f2].rt = Merge(f1, f2) ;
        }
        else {
            if(S[B].val == -1) printf("-1\n") ;
            else printf("%d\n", S[Get(B)].val), Pop(Get(B)) ;
        }
    }
    return 0 ;
}