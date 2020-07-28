def getInvCount(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 
  
# Driver Code 
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(getInvCount(arr, n)) 