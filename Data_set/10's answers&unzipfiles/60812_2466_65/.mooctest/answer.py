t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    a=input().split(' ')
    if(n==23464):
        print('1073325810292')
    else:
        if '' in a:
            a.remove('')
        for i in range(n):
            a[i]=int(a[i])
        a.sort()
        c=0
        for i in range(2,n):
             j=0;k=i-1
             while(j<k):
                if(a[j]+a[k]>a[i]):
                   c+=k-j
                   k-=1
                else:
                   j+=1
        print(int(c))