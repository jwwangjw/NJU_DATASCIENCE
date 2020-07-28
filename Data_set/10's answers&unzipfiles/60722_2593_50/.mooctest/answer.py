
int main() {
	int i,j,n,t,s,k,l;
	scanf("%d",&t);
	while(t--){
	    scanf("%d",&n);
	    int a[n],res=0;
	    for(i=0;i<n;i++)
	    scanf("%d,",&a[i]);
	    for(i=0;i<n-1;i++){
	        for(j=i+1;j<n;j++){
	            s=a[i]+a[j];
	            for(k=0;k<n-1;k++){
	                if(k!=i&&k!=j){
	                    for(l=k+1;l<n;l++){
	                        if(l!=j&&l!=i){
	                            if(s==a[k]+a[l]){res=1;
	                            break;}
	                        }
	                    }
	                    if(res==1)break;
	                }
	            }if(res==1)break;
	        }if(res==1)break;
	    }
	    if(i==n-1)
	    printf("no pairs\n");
	    else
	    printf("%d %d %d %d\n",i,j,k,l);
	}
	return 0;
}