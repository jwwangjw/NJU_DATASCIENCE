q=int(input())
a=list()
a.append(2)
a.append(2)
for i in range(2,20):
    
    if(i%2!=0):
        c=a[i-2]*a[i-2]*a[i-2]
        a.append(c)
    else:
        b=a[i-2]*a[i-2]
        a.append(b)
        
while(q):
    n=int(input())
    print(a[n-1])
    q=q-1