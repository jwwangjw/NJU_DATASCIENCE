n=int(input())
a=[]
p=[]
node=[]
money=0
for i in range(n):
    string=input().split(" ")
    a.append(int(string[0]))
    p.append(int(string[1]))
node.append(0)
for i in range(n):
    for j in range(i+1,n):
        if p[j]<p[i]:
            node.append(j)
            break
node.append(n)
for i in range(1,len(node)):
    kilogram=0
    for j in range(node[i-1],node[i]):
        kilogram+=a[j]
    money=money+kilogram*p[node[i-1]]
print(money)