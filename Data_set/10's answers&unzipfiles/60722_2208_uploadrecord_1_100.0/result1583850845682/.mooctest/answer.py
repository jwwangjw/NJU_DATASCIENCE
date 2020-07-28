 
 #include<stdio.h>
 
 int main(void){
 	int t,n,nums[100], vals[100];
 	int min,j;
 	scanf("%d",&t);
 
 	
 	int i=0;
 	while(t--){
 		scanf("%d",&n);
		for(i=0;i<n;i++){
 			scanf("%d",&nums[i]);
 		}
 	//		for(i=0;i<n;i++){
 	//		printf("%d ",nums[i]);
 	//	}
 		
 		for(i=n-1;i>=0;i--){
 			min=-1;
 			for(j=i-1;j>=0;j--){
 				if(nums[j]<nums[i]){
 					min=nums[j];
 					break;
 				}
 			}
 			vals[i]=min;
 		}
 		for(i=0;i<n;i++){
 			printf("%d ",vals[i]);
 		}
 		printf("\n");
 		
 }
 return 0;
 }
