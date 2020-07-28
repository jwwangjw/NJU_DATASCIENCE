#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
 long long m,n,s0=0,s1=0,s2=0,s3=0,s4=0,s5=0,s6=0,s7=0,s8=0,s9=0;int i,j; //m,n很大，可以用long long  
 cin>>m>>n;
 for(i=m;i<=n;i++)
  {j=i;//一定要重新用一个变量
  while(j>0)//当j可以继续除10时
 {
 if(j%10==0) s0++;    
 if(j%10==1) s1++;
 if(j%10==2) s2++;
 if(j%10==3) s3++;
 if(j%10==4) s4++;
 if(j%10==5) s5++;
 if(j%10==6) s6++;
 if(j%10==7) s7++;
 if(j%10==8) s8++;
 if(j%10==9) s9++;
 j=j/10;//计算下一位整除情况
 }}
 printf("%d %d %d %d %d %d %d %d %d %d",s0,s1,s2,s3,s4,s5,s6,s7,s8,s9);
return 0;   
}