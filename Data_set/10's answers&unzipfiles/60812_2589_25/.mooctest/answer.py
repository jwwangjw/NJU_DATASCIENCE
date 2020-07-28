
for T1 in range(int(input().strip())):
    
    n = int(input().strip())
    
    f = 2
    s = 1
    
    
    for i in range(1, n+1):
        temp = f+s
        f = s
        s = temp
        
    print (f%1000000007)
    
    