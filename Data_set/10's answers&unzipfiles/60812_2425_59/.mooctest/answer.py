
turns = int(input())

for i in range(turns):
    [n,k] = [int(x) for x in input().split()]
    array = list(map(int, input().split()))
    barray = array[:]
    for j in range(n):
        barray[j] -= k
        barray[j] = abs(barray[j])
        
        if j>0:
            if barray[j-1] == barray[j]:
                barray[j-1] = 10
        
    x = barray.index(min(barray))
    
    print(array[x])
        