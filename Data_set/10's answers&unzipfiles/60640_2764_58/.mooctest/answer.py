
def breaking(n):
    
    if n==0:
        return 0
        
    
    if temp[n]!=-1:
        return temp[n]
    
    temp[n]= max(n, breaking(n//2)+ breaking(n//3)+ breaking(n//4))
    
    return temp[n]

    
tc= int(input())
MAX=1000001
temp=[-1]*MAX

for _ in range(tc):
    x= int(input())
    
    res= breaking(x)
    
    print(res)
    