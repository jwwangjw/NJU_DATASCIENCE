T=int(input())
for m in range(T):
    n=int(input())
    result=0
    if n==1:
        result=3
    elif n==2:
        result=8
    elif n>=3:
        result=(n*n*n+3*n)//2+1
    print(result)