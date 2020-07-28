for i in range(int(input())):
    sum1 = 0
    n = int(input())
    for i in range(1,n+1):
        if n%i==0:
            sum1 = sum1+i
    if sum1<2*n:
        print(1)
    else:
        print(0)