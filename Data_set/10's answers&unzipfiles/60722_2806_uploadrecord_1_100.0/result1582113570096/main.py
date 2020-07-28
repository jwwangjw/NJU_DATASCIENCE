n=int(input())
a=[]
p=[]
money=0
for i in range(n):
    string=input().split(" ")
    a.append(int(string[0]))
    p.append(int(string[1]))
for i in range(n-1):
    for j in range(i+1,n):
        if p[j]>p[i]:
            p[j]=p[i]
for i in range(n):
    money+=a[i]*p[i]
print(money)