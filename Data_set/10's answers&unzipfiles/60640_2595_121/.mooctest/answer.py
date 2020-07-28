for _ in range(int(input())):
    n,k=map(int,input().split())
    print(pow(k,n-1,10**9+7))