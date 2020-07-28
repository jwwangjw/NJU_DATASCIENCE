#include <iostream>
#include <fstream>
#include <deque>
#include <cstdlib>
#include <string>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <iterator>
#include <numeric>
#include <sstream>
using namespace std;
 
int main()
{
    //freopen("新建文本文档.txt","r",stdin); 
    string s1,s2;
    cin>>s1>>s2;
    if(s1>s2)
    {
        for(int i=0;i<s2.size();i++)
        {
            if(s1[i]!=s2[i])
            {
                cout<<s1[i]-s2[i]<<endl;
                break;
            }
        }
    }
    else if(s1<s2)
    {
        for(int i=0;i<s1.size();i++)
        {
            if(s1[i]!=s2[i])
            {
                cout<<s1[i]-s2[i]<<endl;
                break;
            }
        }
    }
    else
    {
        cout<<"0"<<endl;
    }
    return 0;
}