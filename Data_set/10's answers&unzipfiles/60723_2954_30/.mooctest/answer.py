#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int INF=int(1e9);
const int MaxN=1010;
int T;
char a[MaxN][15]; 
int len[MaxN],lg2[(1<<10)+10];
int w[15],Ans[15],st[15],cnt[15][MaxN];
bool c1[15],c2[15],mark[15],Map[150][1150];
char Equ,Mul,Add;
bool Solved;

inline int Id(char x) { return x-'a'; }

int calc()
{
    int i,sum=0;
    for(;mark[st[0]-1];st[0]--)
        st[st[0]-1]=st[st[0]-1]*st[st[0]];
    for (int i=1; i<=st[0]; i++) sum+=st[i]; st[0]=0;
    return sum;
}

bool check(int d)
{
    int Last=-1,L=-1,R=-1; st[0]=0;
    for (int i=1; i<=len[d]; i++)
    {
        int c=w[Id(a[d][i])];
        if(c>=0)
            if(Last>=0)st[st[0]]=st[st[0]]*10+c;
                else st[++st[0]]=c;
        else
        {
            if(st[0]==0) return 0;
            for(;mark[st[0]-1];st[0]--)
                st[st[0]-1]=st[st[0]-1]*st[st[0]];

            if(c==-3) mark[st[0]]=1;
                else if(c==-1)L=calc();
                    else mark[st[0]]=0;
        }
        Last=c;
    }
    R=calc();
    return L==R;
}

void Dfs(int d,int Now,int S)
{
    bool Flag=1;
    for (int i=0; i<=12; i++) 
        if(!(Ans[i]==w[i] || Ans[i]==-200)){ Flag=0; break; }
    if(Flag) return;
    if(d>T)
    {   
        Solved=1;
        for (int i=0; i<=12; i++) if(w[i]!=INF)
        {
              if(Ans[i]==-100) Ans[i]=w[i];
              else if(Ans[i]!=w[i])Ans[i]=-200;
        }
        else Ans[i]=-200;
        return;
    }
    else
    {
        if(Now>len[d])
        {
            if(check(d)) Dfs(d+1,1,S);
            return;
        }
        int ch=Id(a[d][Now]);
        if(w[ch]==INF)
        {
            for(int S2=S; S2; S2-=S2&-S2)
            {
                int t=lg2[S2&-S2];
                if(Now==1 && t==0 && w[Id(a[d][2])]>0)continue;
                w[ch]=t;
                Dfs(d,Now+1,S-(S2&-S2));
                w[ch]=INF;
            }
        }
        else Dfs(d,Now+1,S);
    }
}

int M,lw[15],rw[15];

void Get_Range(int &L, int &R)
{ 
    L=R=0; 
    for (;M;M--) L=max(L,lw[M]),R=max(rw[M],R)+(R>0); 
}

bool Pre_Dfs()
{
    int Last,L_l,L_r,R_l,R_r;
    for (int d=1; d<=T; d++)
    {
        M=0;Last=-1;
        for (int i=1; i<=len[d]; i++)
        {
            int c=w[Id(a[d][i])];
            if(c==INF)
            { 
                if(Last<0) M++,lw[M]=rw[M]=0; 
                lw[M]++,rw[M]++;
            }
            else
            {
                if(M==0)return 0;
                for(; mark[M-1]; M--) lw[M-1]+=lw[M]-1,rw[M-1]+=rw[M];

                     if(c==-3) mark[M]=1;
                else if(c==-2) mark[M]=0;
                else if(c==-1) Get_Range(L_l,L_r);
            }
            Last=c;
        }
        Get_Range(R_l,R_r);
        if(L_r<R_l || R_r<L_l)
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    scanf("%d",&T);
    for (int i=1; i<=T; i++) scanf("%s",a[i]+1),len[i]=strlen(a[i]+1);
    for (int i=0; i<=15; i++) lg2[1<<i]=i,Ans[i]=-100;     
    memset(c1,1,sizeof(c1));

    for(char i='a';i<='m';i++)
        for (int j=1; j<=T; j++)
        {
            bool Flag=1;
            for (int k=1; k<=len[j]; k++)
            {
                if(k<len[j]) Map[a[j][k]][a[j][k+1]]=Map[a[j][k+1]][a[j][k]]=1;
                if(a[j][k]==i) cnt[Id(i)][j]++;
            }
            if(cnt[Id(i)][j]!=1) Flag=0;
            if(a[j][1]==i || a[j][len[j]]==i){ c1[i-'a']=0; Flag=0; }
            c2[Id(i)]=Flag;
        }

    for(Equ='a'; Equ<='m'; Equ++) if(c2[Id(Equ)])
        for(Mul='a'; Mul<='m'; Mul++) if(c1[Id(Mul)])
            for(Add='a'; Add<='m'; Add++) if(c1[Id(Add)])
                if(Equ!=Mul && Add!=Mul && Equ!=Add)
                    if(!Map[Equ][Mul] && !Map[Equ][Add] && !Map[Mul][Add])
                    {                 
                        for (int i=0; i<=12; i++) w[i]=INF;
                        w[Id(Equ)]=-1; w[Id(Add)]=-2; w[Id(Mul)]=-3;
                        if(!Pre_Dfs()) continue;
                        Dfs(1,1,(1<<10)-1);
                    }

    for (int i=0; i<=12; i++)
        if(Ans[i]>=-3)
        {
            putchar('a'+i);
                 if(Ans[i]==-3)putchar('*');
            else if(Ans[i]==-2)putchar('+');
            else if(Ans[i]==-1)putchar('=');
            else putchar('0'+Ans[i]);
            putchar('\n');
        }
    if(!Solved) printf("noway\n");

    return 0;
}