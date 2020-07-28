import math
n=input()
n=int(n[1:len(n)-1])
result=n-1
p=int(math.log(n,2))
for i in range(2,p):
    x=pow(n,1/i)
    if n-(n-1)//x==pow(x,i):
        result=x
print("\""+str(result)+"\"")