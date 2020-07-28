for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    stack = []
    res = []
    for i in range(n-1,-1,-1):
        if(i==n-1):
            stack.append(a[i])
            res.append(-1)
        else:
            while(a[i]>stack[len(stack)-1]):
                del stack[len(stack)-1]
                if(len(stack)==0):
                    res.append(-1)
                    break
            else:
                res.append(stack[len(stack)-1])
            stack.append(a[i])
    res.reverse()
    print(*res)
                    
                    