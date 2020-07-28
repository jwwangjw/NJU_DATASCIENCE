#     for i in range(3,n+1):
#         p.append((p[i-3]+p[i-2])%1000000007)
    
#     return p[n]    


    
tc= int(input())
for _ in range(tc):
    p=[1,1,1]

    n= int(input())
    
    num=3
    while num<n+1:
        temp= p[num-3]%1000000007 + p[num-2]%1000000007
        p.append(temp)
        num+=1
    
    res= p[n]%1000000007
    print(res)
        
        

