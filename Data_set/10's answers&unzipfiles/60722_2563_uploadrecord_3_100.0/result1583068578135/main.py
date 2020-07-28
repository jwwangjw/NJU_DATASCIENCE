import math
n=input()
n=int(n[1:len(n)-1])
result=n-1
p=int(math.log(n,2))
#x^i+x^(i-1)+x^(i-2)+,,,+1=n-->i确定则x
#求i的最大值
for i in range(2,p):
    x=int(pow(n,1/i))
    if n-(n-1)//x==pow(x,i):
        result=x
print(result)