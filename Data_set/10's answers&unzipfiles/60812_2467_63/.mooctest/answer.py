t=int(input())
for i in range(0,t):
    d=[]
    c=input().split()
    k=int(c[2])
    a=input().split()
    b=input().split()
    for j in range(0,len(b)):
        d.append(int(b[j]))
    for j in range(0,len(a)):
        d.append(int(a[j]))
    d.sort()
    
    print(d[k-1])