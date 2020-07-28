
int main() {
	int t,n;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
	    scanf("%d",&n);
	    int arr[n];
	    for(int j=0;j<n;j++){
	        scanf("%d",&arr[j]);
	    }
	    int count=0,temp;
	    for(int j=0;j<n;j++){
	        for(int k=0;k<n-j;k++){
	            if(arr[k-1]>arr[k]){
	                temp =arr[k-1];
	                arr[k-1]=arr[k];
	                arr[k]=temp;
	            }
	        }
	    }
        int p,q,r;
        for(int p=0;p<n;p++){
            q=p+1;
            r=q+1;
            
            while(r<n){
                if(arr[p]+arr[q]==arr[r]){
                    count++;
                    r++;
                    q++;
                }
                else if(arr[p]+arr[q]>arr[r]){
                    r++;
                }
                else{
                    q++;
                }
            }
            
        }
	    if(count>0){
	        printf("%d\n",count);
	    }
	    else{
	        printf("-1\n");
	    }
	}
	return 0;
}