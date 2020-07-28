#include<map>
#include<set>
#include<ctime>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
set<int>s;//存合法的房间号 
map<long long,bool>mp;//判重 
long long  num[100010],p[1000010],b[1000010],h[1000010];
int n,m,q;

int main()
{
    int i,j;
    srand(1289);

    scanf("%d%d%d\n",&n,&m,&q);
    for(i=1;i<=n;++i) num[i]=(long long)rand()*rand()%1000000000*(rand()*rand()%2000000000);//给每个人随机一个值 
    s.insert(1);//因为刚开始所有人都在第一个房间，先将第一个房间加入set 
    for(i=1;i<=n;++i) h[1]^=num[i],p[1]++,b[i]=1;//h存当前房间的异或值；p存当前房间的人数；b存当前每个人在哪个房间 
    for(i=1;i<=q;++i)//询问和操作总共不超过10^5,且每次操作只移动一个人，所以范围可以使用STL 
     {
        char c;
        int x,y;
        scanf("%c",&c);
        scanf("%d%d\n",&x,&y);
        if(c=='C')
          {
            if(b[x]==y) continue;//看操作后是否换了房间 
            s.erase(b[x]); s.erase(y);//将原来的状态移出set 

            h[b[x]]^=num[x];
            p[b[x]]--;
            if (!mp[h[b[x]]]) s.insert(b[x]);

            h[y]^=num[x];
            p[y]++;
            if (!mp[h[y]]) s.insert(y);

            b[x]=y;
          }
         else
          if(c=='W')
           {
             int ans=0;
             set<int>::iterator it=s.lower_bound(x);
             for(;it!=s.end()&&*it<=y;it=s.lower_bound(x))
              {
                mp[h[*it]]=1;
                ans+=p[*it];
                s.erase(it);
              } 
             printf("%d\n",ans);
          }
     }
     return 0;
}