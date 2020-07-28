k=int(input())
for i in range(k):
    n=int(input())
    length=input().split(" ")
    for j in range(n):
        length[j]=int(length[j])
    length.sort()
    for j in range(n):
        if length[j]<=n-j:
            result=length[j]
        else:
            if n-j>result:
                result=n-j
    print(result)
        