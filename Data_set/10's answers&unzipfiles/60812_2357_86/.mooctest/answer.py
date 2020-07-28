def findPairs(arr1, arr2, n, m, x): 
  
    for i in range(0, n): 
        for j in range(0, m): 
            if (arr1[i] + arr2[j] == x): 
                print(arr1[i], arr2[j]) 
  
for t in range(int(input())):
    n = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    findPairs(arr1, arr2, n[0], n[1], n[2]) 