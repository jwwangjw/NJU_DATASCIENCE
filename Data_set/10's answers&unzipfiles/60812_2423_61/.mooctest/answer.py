z=0
t=int(input())
while z<t :
    m,n=map(int,input().split())
    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))    
    a1.sort()
    a2.sort()
    ans=0
    k=0
    for i in a2 :
        if k>=m :
            ans=1
            break
        if i==a1[k] :
            k=k+1
        else :
            k=k+1
            if k<m :
                while i!=a1[k] :
                    k=k+1
                    if k>=m :
                        ans=1
                        break
            else :
                ans=1
                break
    if(ans==0) :
        print("Yes")
    else :
        print("No")
    z=z+1