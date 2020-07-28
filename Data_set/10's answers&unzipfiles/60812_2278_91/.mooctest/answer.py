if __name__ == "__main__":
    
    t = int(input())
    for i in range(t):
        
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        
        xorArr = [0] * n
        tempVar = arr[n-1]
        xorArr[n-1] = tempVar
        for j in range(n-1):
            xorArr[j] = arr[j] ^ arr[j+1]
            print(xorArr[j], end=' ')
        
        print(xorArr[n-1])
            
            
            