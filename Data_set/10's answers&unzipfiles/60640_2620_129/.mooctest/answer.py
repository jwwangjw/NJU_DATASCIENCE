for _ in range(int(input())):
    n=int(input())
    sum=0
    for i in range(1,n+1):
        sum+=i*i*i*i*i
    print(sum)