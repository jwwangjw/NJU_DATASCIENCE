n=int(input())
l=[]
for i in range(0,n):
    l.append(int(input()))
for i in range(0,n):
    x=l[i]
    lst=[]
    counter=1
    z=0
    if(x==1):
        lst=[1]
    elif(x==2):
        lst=[1,2]
    elif(x==3):
        lst=[1,2,4]
    elif(x==4):
        lst=[1,2,4,5]
    for j in range(2,x):
        for k in range(1,j):
            z=z+1
            if(z<=x):
                
                
                lst.append(counter)
                counter=counter+2
            else:
                break
        counter=counter-1
        
        if(z>x):
            break
            
    for t in range(0,len(lst)):
        print(lst[t],end=" ")
    print()

