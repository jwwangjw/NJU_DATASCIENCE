#include<stdio.h>
#include<string.h>
long long ans2,ans3;
int map2[100000],map3[100000],l2,l3;
char t[100000];
int main()
{
    scanf("%s",t);
    for(int i=0;i<strlen(t);i++)
    t[i]-='0'-1,map2[i]=t[i]-1,l2=i+1;
    scanf("%s",t);
    for(int i=0;i<strlen(t);i++)
    t[i]-='0'-1,map3[i]=t[i]-1,l3=i+1;
    for(int i=0;i<l2;i++)
    {
        for(int j=0;j<l3;j++)
        {
            int x=map3[j];
            for(int k=0;k<=2;k++)
            {
                if(map2[i]==1)
                map2[i]=0;
                else
                map2[i]=1;
                map3[j]=k;
                for(int l=0;l<l2;l++)
                ans2+=map2[l],ans2*=2;
                ans2/=2;
                for(int l=0;l<l3;l++)
                ans3+=map3[l],ans3*=3;
                ans3/=3;
                if(map2[i]==1)
                map2[i]=0;
                else
                map2[i]=1;
                map3[j]=x;
                if(ans2==ans3){
                printf("%d",ans2);
                return 0;
                }
                ans2=ans3=0;
            }
        }
    }
 } 