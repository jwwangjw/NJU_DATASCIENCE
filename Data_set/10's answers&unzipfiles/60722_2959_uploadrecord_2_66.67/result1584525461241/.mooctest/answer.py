#include<bits/stdc++.h>
using namespace std;

char s1[200020],s2[200020];

struct SAM
{
    struct point
    {
        int son[26],fa,mx,len;
    }t[800080];

    int last=1,cnt=1;
    vector<int> g[800080];
    int sz[800080][2];

    void add(int c,int num)
    {
        int p=last;
        if(t[p].son[c]&&t[p].len+1==t[t[p].son[c]].len)
        {
            last=t[p].son[c];
            sz[last][num]++;
            return ;
        }
        int np=++cnt;
        t[np].len=t[p].len+1;
        sz[np][num]++;
        while(p&&!t[p].son[c])
        {
            t[p].son[c]=np;
            p=t[p].fa;
        }
        if(!p)
        {
            t[np].fa=1;
        }
        else
        {
            int q=t[p].son[c],nq;
            if(t[q].len==t[p].len+1)
            {
                t[np].fa=q;
            }
            else
            {
                nq=++cnt;
                t[nq]=t[q];
                t[nq].len=t[p].len+1;
                t[np].fa=t[q].fa=nq;
                while(p&&t[p].son[c]==q)
                {
                    t[p].son[c]=nq;
                    p=t[p].fa;
                }
            }
        }
        last=np;
    }

    long long ans=0;

    int dfs(int now)
    {
        t[now].mx=t[now].len-t[t[now].fa].len;
        for(int i=0;i<g[now].size();i++)
        {
            dfs(g[now][i]);
            sz[now][0]+=sz[g[now][i]][0];
            sz[now][1]+=sz[g[now][i]][1];
        }
        ans+=1ll*t[now].mx*sz[now][0]*sz[now][1];
    }

    int solve()
     {
        for(int i=1;i<=cnt;i++) g[t[i].fa].push_back(i);
        dfs(1);
        printf("%lld\n",ans);
    }
}sam;

int main()
{
    scanf("%s",s1);
    scanf("%s",s2);
    int len1=strlen(s1);
    int len2=strlen(s2);
    for(int i=0;i<len1;i++)
    {
        sam.add(s1[i]-'a',0);
    }
    sam.last=1;
    for(int i=0;i<len2;i++)
    {
        sam.add(s2[i]-'a',1);
    }
    sam.solve();
}