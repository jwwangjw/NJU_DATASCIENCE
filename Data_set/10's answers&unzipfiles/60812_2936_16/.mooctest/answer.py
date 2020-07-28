#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<string>
using namespace std;
int n,cnt,now,pos,sum[100005];
string s,temp,tot[100005];
char excel[100];
map<string,int> a;
struct Ans
{
    int cs;
    string chuan;
}ans[100005];
void init()        //初始化函数 
{
    excel['0']='0';excel['1']='1';
    excel['A']=excel['B']=excel['C']=excel['2']='2';
    excel['D']=excel['E']=excel['F']=excel['3']='3';
    excel['G']=excel['H']=excel['I']=excel['4']='4';
    excel['J']=excel['K']=excel['L']=excel['5']='5';
    excel['M']=excel['N']=excel['O']=excel['6']='6';
    excel['P']=excel['R']=excel['S']=excel['7']='7';
    excel['T']=excel['U']=excel['V']=excel['8']='8';
    excel['W']=excel['X']=excel['Y']=excel['9']='9';
}
bool cmp(Ans a,Ans b)
{
    return a.chuan+b.chuan<b.chuan+a.chuan;
}
int main()
{
    init();        //千万千万别忘记调用 
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        cin>>s;
        temp.clear();pos=0;        //将temp清空，pos归零 
        for(int j=0;j<s.length();j++)
        {
            if(s[j]!='-')    //转化为数字 
            {
                temp+=excel[s[j]];
                pos++;
            }
            if(pos==3) temp+='-',pos=-999999999;    //到了该加'-'的地方，加上'-',同时将pos设为负值，防止重复添加 
        }
        if(!a[temp]) tot[++cnt]=temp;    //如果这个字符串没出现过，将这个字符串加入到已有的字符串中 
        a[temp]++;    //该字符串出现的次数++ 
    }
    for(int i=1;i<=cnt;i++)        //找哪个字符串是重复的 
    {
        if(a[tot[i]]>1)
        {
            ans[++now].chuan=tot[i];    //存答案 
            ans[now].cs=a[tot[i]];
        }
    }
    if(!now)    //没有重复的 
    {
        printf("No duplicates.");
        return 0;
    }
    sort(ans+1,ans+now+1,cmp);        //按字典序排列 
    for(int i=1;i<=now;i++)
    {
        cout<<ans[i].chuan<<' ';
        printf("%d\n",ans[i].cs);
    }
    return 0;
}