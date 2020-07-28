#include <stdio.h>
int main() {
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int n,i,x,f=0,j;
	    scanf("%d%d",&n,&x);
	    int a[n];
	    for(i=0;i<n;i++)
	    {
	        scanf("%d",&a[i]);
	    }
	    for(i=0;i<n-1;i++)
	    {
	        if(a[i]>x)
	        continue;
	        for(j=i+1;j<n;j++)
	        {
	            if(a[i]+a[j]==x)
	            {
	                f++;
	                break;
	            }
	        }
	        if(f==1)
	        break;
	    }
	    if(f==1)
	    printf("Yes\n");
	    else
	    printf("No\n");
	}
	return 0;
}