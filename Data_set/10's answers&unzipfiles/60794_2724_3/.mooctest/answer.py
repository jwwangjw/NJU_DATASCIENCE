a=int(input())
b =[]
c =[]

for i in range(0,a):
    x=int(input())
    b.append(x)

for i in range(0,a):
    if(b[i]==1):
       c.append(6)
    elif(b[i]==2):
       c.append(5)
    elif(b[i]==3):
       c.append(4)
    elif(b[i]==4):
       c.append(3)
    elif(b[i]==5):
       c.append(2)
    elif(b[i]==6):
       c.append(1)
        
for i in range(0,a):
    print(c[i])

