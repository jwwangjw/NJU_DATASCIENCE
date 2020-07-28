import heapq
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    heapq.heapify(l)
    sum1=0
    while(len(l)>1):
        x=heapq.heappop(l)
        y=heapq.heappop(l)
        z=x+y
        sum1+=z
        heapq.heappush(l,z)
    print(sum1)