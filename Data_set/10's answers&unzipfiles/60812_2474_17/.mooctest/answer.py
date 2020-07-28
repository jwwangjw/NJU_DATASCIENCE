t=int(input())

while t:
    t=t-1
    string=input()
    
    s=[]
    res=0
    
    s.append(-1)
    
    for i in range(len(string)):
        if string[i]=='(':
            s.append(i)
        else:
            s.pop()
            
            if len(s)!=0:
                res=max(res,i-s[len(s)-1])
            else:
                s.append(i)
    print(res)