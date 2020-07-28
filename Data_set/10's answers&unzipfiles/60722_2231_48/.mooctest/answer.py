pr=[True for i in range(162)]
p=2
while(p*p<162):
    if(pr[p]==True):
        for j in range(p*p,162,p):
            pr[j]=False
    p=p+1
a=[]
for i in range(2,162):
    if(pr[i]==True):
        a.append(i)
b=[]
for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        for k in range(j+1,len(a)):
            if(a[i]*a[j]*a[k]<1000):
                b.append(a[i]*a[j]*a[k])
t=int(input())
while(t):
    n=int(input())
    if(n in b):
        print(1)
    else:
        print(0)
    t=t-1