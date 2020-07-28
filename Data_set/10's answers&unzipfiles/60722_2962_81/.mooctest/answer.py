
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <math.h>
#include <stack>
#include <utility>
#include <string>
#include <sstream>
#include <cstdlib>
#include <set>
#define LL long long
using namespace std;
const int INF = 0x3f3f3f3f;
const int maxn = 1000000 + 11;
int dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};
string str;
int vis[maxn];
map<string,int> mp;
int m,n;
int main()
{
    scanf("%d %d",&n,&m);
    memset(vis,0,sizeof(vis));
    for(int i = 1; i <= n; i++)
    {
        cin>>str;
        int len = str.size();
        int num = 0;
        if(len == 1)
            num += (str[0] - 'A');
        else if(len == 2)
            num = 32 *(str[0] - 'A') + str[1] - 'A';
        else
        {
            for(int j = 3; j >= 1; --j)
            {
                int pos = len - j;
                num = num * 32 + str[pos] - 'A';
            }
        }
        num %= m;
        if(mp[str] == 0 && vis[num])
        {
            for(int t = 1; t < maxn; t++)
            {
                if(!vis[(num + t * t)%m])
                {
                    num = (num + t * t)%m;
                    vis[num] = 1;
                    mp[str] = num;
                    printf("%d",num);
                    break;
                }
                else if(!vis[(num-t*t+m)%m])
                {
                    num = (num - t * t + m)%m;
                    vis[num] = 1;
                    mp[str] = num;
                    printf("%d",num);
                    break;
                }
            }
 
        }
        else
        {
            num %= m;
            mp[str] = num;
            printf("%d",num);
            vis[num] = 1;
        }
        if(i < n)
            putchar(' ');
        else
            puts("");
 
    }
    return 0;
}
