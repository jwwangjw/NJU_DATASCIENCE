#include<stdio.h>
#include<string.h>
#define N 5
int main()
{
    int i,j,k;
    char x[N][200],ans[200];
    for(i=0;i<N;i++) scanf("%s",x[i]);
    int max=0;
    for(i=0;i<N;i++)
    {
        if(strlen(x[i])>max) strcpy(ans,x[i]),max=strlen(x[i]);
    }
    puts(ans);
    return 0;
}