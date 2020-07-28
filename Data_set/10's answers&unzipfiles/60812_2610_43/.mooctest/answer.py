for _ in range(int(input())):
    size=int(input())
    A=list(map(int,input().split()))
    B={}
    count=0
    j=0
    for i in range(size):
        while j<size and A[j] not in B:
            B[A[j]]=1
            j+=1
        count+=((j-i)*(j-i+1))//2
        del B[A[i]]
    print(count)