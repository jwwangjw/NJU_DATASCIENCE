def maxMoney(n, k):
    if n%2 == 0:
        print(k*(n//2))
    else:
        print(k*((n//2)+1))
    return
    
t = int(input())
for i in range(0, t):
#    n = int(input())
    n = list(map(int, list(input().split())))
    maxMoney(n[0], n[1])	   
