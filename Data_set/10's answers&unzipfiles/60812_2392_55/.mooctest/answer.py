#include <stdio.h>

int main() {
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int n,i,p,f=0,j;
	    scanf("%d%d",&n,&p);
	    int a[n];
	    for(i=0;i<n;i++)
	    scanf("%d",&a[i]);
	    for(i=0;i<n;i++)
	    {
	        for(j=i+1;j<n;j++)
	        {
	            if(a[i]*a[j]==p)
	            {
	                f++;
	                break;
	            }
	        }
	        if(f!=0)
	        break;
	    }
	    if(f==0)
	    printf("No\n");
	    else
	    printf("Yes\n");
	}
	return 0;
}