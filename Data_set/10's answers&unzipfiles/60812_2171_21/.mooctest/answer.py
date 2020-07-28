z=0
t = int(input())
while z<t :
    n=int(input())
    l=list(map(int,input().split()))
    e=[i for i in l if i%2==0]
    o=[i for i in l if i%2==1]
    for i in e :
        print(i,end=" ")
    for i in o :
        print(i,end=" ")
    print()
    
 
        
 
    z=z+1