#include<iostream>
#include<cstdio>
#define For(i,a,b) for(int i=a;i<=b;i++)
#define Ford(i,a,b) for(int i=a;i>=b;i--)
const int N=5e5,Logn=21;
void read(int &x)
{
    int t=0,opt=1;
    char c=getchar();
    while (c<'0'||c>'9') (c=='-'?opt=-1:0),c=getchar();
    while ('0'<=c&&c<='9')
    {
        t=t*10+c-'0';
        c=getchar();
    }
    x=t*opt;return ;
}
int n,pa[N][Logn];char s[N];
namespace SA
{
    int rank[N],rank_pa[N],temp[N],pos[N],tax[N],tp[N],sa[N],size;
    void Qsort(int *sa,int *rank,int *tp,int size)
    {
        For(i,0,size) tax[i]=0;
        For(i,1,n) tax[rank[tp[i]]]++;
        For(i,1,size) tax[i]+=tax[i-1];
        Ford(i,n,1) sa[tax[rank[tp[i]]]--]=tp[i];
    }
    void Sort()
    {
        For(i,1,n) rank[i]=s[i]-'a'+1,tp[i]=i;//一定记住0是用来放'\0'的,而不是'a'
        Qsort(sa,rank,tp,'z'-'a'+1);For(i,1,n) pos[sa[i]]=i;
        for(int w=1,p=0;w<n;w<<=1,p++) //在长度为w时所有人的聪明程度都是对的
        {                                 //(pos即此时严格排名(含编号,绝对不同),rank为智商字符串排名(无视编号))
            For(i,1,n) rank_pa[i]=pos[pa[i][p]];
            Qsort(tp,rank_pa,sa,n); //以自己的字符串排名为第一关键字,以父亲严格排名为第二键字，自己位置为第三关键字
            Qsort(sa,rank,tp,rank[sa[n]]);//如果两个人智商字符串相同，则按照其父亲的严格排名，若父亲相同，则按自己的严格排名
            For(i,1,n) temp[i]=rank[i];rank[sa[1]]=1;
            For(i,2,n) rank[sa[i]]=(temp[sa[i]]==temp[sa[i-1]]&&temp[pa[sa[i]][p]]==temp[pa[sa[i-1]][p]])?rank[sa[i-1]]:rank[sa[i-1]]+1;
            For(i,1,n) pos[sa[i]]=i;//最终得到2*w的严格排名
        }
    }
}
int main()
{
    read(n);
    For(i,2,n) {read(pa[i][0]);For(j,1,Logn-1) pa[i][j]=pa[pa[i][j-1]][j-1];}
    scanf("%s",s+1);
    SA::Sort();For(i,1,n) printf("%d ",SA::sa[i]);
    return 0;
}