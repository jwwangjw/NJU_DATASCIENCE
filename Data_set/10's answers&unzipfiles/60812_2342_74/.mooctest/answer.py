turns = int(input())

for i in range(turns):
    [n,k] = [int(x) for x in input().split()]
    array = list(map(int, input().split()))
    for j in range(0,n,k):
        if j+k < n:
            #array[j:j+k] = array[j:j+k].reverse()
            print(*list(reversed(array[j:j+k])), end=" ")
        else:
            #array[j:] = array[j:].reverse()
            print(*list(reversed(array[j:])), end=" ")
    print()