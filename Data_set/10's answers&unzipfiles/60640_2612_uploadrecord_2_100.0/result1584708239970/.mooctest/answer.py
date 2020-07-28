from collections import defaultdict
for _ in range(int(input())):
    p1={}
    p2={}
    #n=int(input())
    n = int(input())
    arr = list(map(int,input().split()))
    x = defaultdict(set)
    y = defaultdict(set)
    for i in range(0,len(arr),2):
        x[arr[i]].add(arr[i+1])
        y[arr[i+1]].add(arr[i])
    ans = 0
    for i in x:
        if len(x[i])>1:
            ans += len(x[i])*(len(x[i])-1)//2
    for i in y:
        #if i not in x:
        if len(y[i])>1:
            ans += len(y[i])*(len(y[i])-1)//2
    print(ans)