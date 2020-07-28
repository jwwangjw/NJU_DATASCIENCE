
t=int(input())
for _ in range(t):
    i,j,k=map(int,input().split())
    c=0
    for a in range(i,j+1):
        if a%k==0:
            c=c+1
    print(c)