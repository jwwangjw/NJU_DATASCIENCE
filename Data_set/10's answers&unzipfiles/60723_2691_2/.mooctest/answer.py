
int solve(int arr[], int n, int sum)
{
    int dp[n+1][sum+1];
    for(int i=0;i<=n;i++)
        dp[i][0]=1;
    for(int j=1;j<=sum;j++)
        dp[0][j]=0;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=sum;j++)
        {
            if(j<arr[i-1])
                dp[i][j]=dp[i-1][j];
            else
                dp[i][j]=dp[i-1][j]||dp[i-1][j-arr[i-1]];
            
        }
    }
    int pos=0;
    for(int i=1;i<=sum;i++)
    {
        if(dp[n][i])
        {
            pos=i;
        }
    }
    return pos;
}


int main()
{
	//code
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int n;
	    scanf("%d",&n);
	    int arr[n],sum=0;
	    for(int i=0;i<n;i++)
	    {
	        scanf("%d",&arr[i]);
	        sum+=arr[i];
	    }
	        
	    printf("%d\n",sum-2*solve(arr,n,sum/2));
	}
	return 0;
}