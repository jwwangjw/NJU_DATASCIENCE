t = int(input())
z=0
while z<t :
    n=int(input())
    arr=list(map(int,input().split()))
    x=int(input())
    arr.sort()
    for el in range(n) :
        if arr[el] > x :
            arr=arr[0:el]
            break
    n=len(arr)
    flag=0
    for i in range(n) :
        for j in range(i+1,n) :
            for k in range(j+1,n) :
                for l in range(k+1,n) :
                    s=arr[i]+arr[j]+arr[k]+arr[l]
                    if s==x :
                        print(1)
                        flag=1
                        break
                if flag==1 :
                    break
            if flag==1 :
                break
        if flag==1 :
            break
    if flag!=1 :
        print(0)
                    
 
        
 
    z=z+1
        
    t -= 1