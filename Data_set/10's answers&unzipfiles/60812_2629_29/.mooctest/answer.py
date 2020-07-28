t=int(input())
for i in range(0,t):
    x=int(input())
    b=format(x,"b")
    c=0
    for j in b:
        if j=="1":
            c=c+1
    print(c)