#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int l,n=0,i,j,ans;//n记录已匹配的2、5数
bool flag;
string s;
int main()
{
    cin>>s;
    l=s.length();
    if(l%2==1)//长度为奇数肯定不行
    {
        printf("-1\n");
        return 0;
    }
    while(n<l)
    {
        i=0;
        flag=1;
        while(i<l)//扫一遍
        {
            while(s[i]!='2')
            {
                i++;
                if(i==l)
                {
                    goto Next;
                }
            }
            j=i;
            while(s[i]!='5')
            {
                i++;
                if(i==l)
                {
                    goto Next;
                }
            }
            s[i]=s[j]='0';//删去一对
            flag=0;
            n+=2;
        }
        Next:;
        if(flag)//没有找到
        {
            printf("-1\n");
            return 0;
        }
        ans++;
    }
    printf("%d\n",ans);
    return 0;
}