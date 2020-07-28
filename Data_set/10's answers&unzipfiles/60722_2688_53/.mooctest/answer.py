/*
int findsum(int arr[],int size,int val,int index,int S,int R)
{
    int i;
if(S+arr[index]==val)
    {
      //  count++;
        return count;
    }
    else{
    for(i=index;i<size;i++)    
    {   
        if(R-arr[i]>val -(S+arr[i])&&i<size&&(S+arr[i]+arr[i+1]<val))
           count= findsum(arr,size,val,index+1,S+arr[i],R-arr[i]);
               if(count)
                {
                    count++;
                }

         if(R-arr[i]>val -(S+arr[i])&&i<size&&(S+arr[i]<val))
            count= findsum(arr,size,val,index+1,S,R-arr[i]);
                if(count)
                    count++;
    }
    return 0;
}
*/
//}
int perfectSum(int arr[],int size,int val,int sum)
{
int i,flag;
    if(size<0||sum>val)
        return 0;
    if(sum==val) 
        return 1;
    return (perfectSum(arr,size-1,val,sum+arr[size-1])+perfectSum(arr,size-1,val,sum));
}

int main() {
	//code	
int test_case,size,i,val;
int len,flag;
scanf("%d",&test_case);
while(test_case--)
{
    scanf("%d",&size);
	int arr[size];
	for(i=0;i<size;i++)
	   scanf("%d",&arr[i]); 
	scanf("%d",&val);
	   flag=perfectSum(arr,size,val,0);  
	    
	printf("%d\n",flag);
	}
	return 0;
}	