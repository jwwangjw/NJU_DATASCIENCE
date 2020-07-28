t=int(input())
for i in range(0,t):
    n=int(input())
    a=input().split()
    b=input().split()
    a.sort()
    b.sort()
    if a==b:
        print(1)
    else:
        print(0)
    