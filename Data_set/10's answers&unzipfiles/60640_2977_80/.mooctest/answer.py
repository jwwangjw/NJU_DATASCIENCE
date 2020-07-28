#include<stdio.h>
#include<string.h>
 
void out_putReverse(char *A);
/*--------------------------------------*/
int main()
{
 
   char A[81];
 
    while(gets(A)!=NULL&&!(A[0]=='!'&&strlen(A)==1))
      {
           out_putReverse(A);
      }
return 0;
}
 
/*--------------------------------------*/
void out_putReverse(char *A)
{
     for(int i=0;i<strlen(A);i++)
       {
          if(A[i]>='a'&&A[i]<='z')
            printf("%c",'z'-(A[i]-'a'));
              else
              if(A[i]>='A'&&A[i]<='Z')
               printf("%c",'Z'-(A[i]-'A'));
                 else/*如果不是字母则直接输出*/
                 printf("%c",A[i]);
 
       }
       /*最后换行*/
       printf("\n");
return ;
}