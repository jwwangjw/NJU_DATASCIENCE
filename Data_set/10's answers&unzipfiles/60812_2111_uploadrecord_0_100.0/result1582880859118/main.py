#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int main(void){
	int n;
	/*printf("请问您想知道的第几个丑数的值？输入一个正整数n,然后程序会给你答案：");
	while(1){
		if(scanf("%d",&n)==0){
			printf("对不起，您输入的不是数字，请重新输入：");
			while(getchar()!='\n');
			continue;	
		} 
		else if(n<=0||n>1691){
			printf("对不起，您输入的不是正整数或者正整数超过了程序的处理范围(1-1691)，请重新输入：");
			continue;
		}
		else
		break;	
	}*/
	scanf("%d",&n); 
	int *p=(int*)malloc(n*sizeof(int));
	int a,b,c,sum=0,i=0,j,temp;
	for(j=0;sum<n;j++){
L:		sum=0;
		for(c=0;c<14&&c<=j;c++)
		for(b=0;b<21&&b<=j;b++)
		for(a=0;a<32&&a<=j;a++)
			if((b*log(3)+c*log(5)<(31-a)*log(2))&&(a+b+c<=j)){
				sum++;
				if(i==1){
					if(sum>n)
						p=(int*)realloc(p,sum*sizeof(int));
					*(p+sum-1)=pow(2,a)*pow(3,b)*pow(5,c);
				}
			}
	}
	if(i==0){
		j=(30>=j+7)?(j+7):30;
		i=1;
		goto L;
	}
	for(j=0;j<sum-1;j++)
	for(i=0;i<sum-1;i++)
		if(*(p+i)>*(p+i+1)){
			*(p+i)+=*(p+i+1);
			*(p+i+1)=*(p+i)-*(p+i+1);
			*(p+i)-=*(p+i+1);
		}
	free(p); 
	printf("%d\n",*(p+n-1));
}