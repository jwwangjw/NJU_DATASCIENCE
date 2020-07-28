
n=int(input())
N=[]
for i in range(n):
    x=int(input())
    N.append(x)

def check(n):
    if n%5==0:
        print("YES")
    else:
        print("NO")
        

for i in N:
        check(i)
        
