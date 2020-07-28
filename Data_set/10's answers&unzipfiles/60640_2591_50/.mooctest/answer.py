t=int(input())
for i in range(t):
    n=int(input())
    n=n+2
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
        #else:
         #   flag=1
    if flag==1:
        print('Yes')
    else:
        print('No')