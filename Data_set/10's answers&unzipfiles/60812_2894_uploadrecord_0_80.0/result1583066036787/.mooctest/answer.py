#include<iostream>
      using namespace std; //头文件激活；
      int main()
      {
          int n,ans=0,x;//ans记达到条件的数量，要记得清零；
          string s;//我们伟大的字符串；
          cin>>n;//n是s的长度。
          cin>>s;//因为我们要输入的字符串里只有“V”和“K"，所以用cin就行了；
          for(x=0;x<n-1;x++)//字符串的第一位都在是s[0]上，我们就从0开始判断到n-1，0位上有了就可以到s的长度减一。
          {
              if (s[x]=='V'&&s[x+1]=='K') {ans++;s[x]='v';s[x+1]='k';}//s[x]和s[x+1]是两相邻的字符。如果条件符合，ans++，把这两的字符标记成以符合，注意，两个标记得不能相同。
          }
          for(x=0;x<n-1;x++)//第二步；
          if (s[x+1]==s[x]) {ans++;cout<<ans;return 0;}//如果相邻两个相同，也就是“VV”或“KK”，就ans加一，输出答案，结束程序。
          cout<<ans;//如果没有相邻相同的就输出原来的数。
          return 0;//就这样，愉快的结束程序。
      }