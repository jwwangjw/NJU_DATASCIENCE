def printMax(arr, n, k): 
    max = 0
    
    for i in range(n - k + 1): 
        max = arr[i] 
        for j in range(1, k): 
            if arr[i + j] > max: 
                max = arr[i + j] 
        print(str(max) + " ", end = "") 
  
for t in range(int(input())): 
    n=list(map(int,input().split()))
    arr = list(map(int,input().split()))
    printMax(arr, n[0], n[1]) 
    print()