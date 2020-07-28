int main()
{
	//code
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int n,k;
	    scanf("%d %d",&n,&k);
	    int a[n],i;
	    for(i=0;i<n;i++)
	    scanf("%d",&a[i]);
	    int res=fun1(a,n,k);
	    printf("%d\n",res);
	}
	return 0;
}
int fun1(int arr[], int n, int k)
{
    int dist_count = 0;
    for (int i=0; i<n; i++)
    {
        int j;
        for (j=0; j<n; j++)
            if (i != j && arr[j] == arr[i])
                break;
        if (j == n)
            dist_count++;
 
        if (dist_count == k)
            return arr[i];
    }
 
    return -1;
}
 