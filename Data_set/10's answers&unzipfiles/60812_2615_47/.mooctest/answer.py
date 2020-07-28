from collections import Counter
for _ in range(int(input())):
    s=list(map(ord,input()))
    s=list(set(s))
    #print(s)
    s.sort()
    s.reverse()
    li=Counter(s)
    
    
    st,maxi,diff=0,0,0
    for j in range(1,13,1):
        for k in range(len(s)):
            length=1
            a=s[k]
            while(li[a-j]>0):
                a-=j
                length+=1
            if length>maxi:
                diff=j
                maxi=length
                st=s[k]
                
    for x in range(maxi,0,-1):
        print(chr(st),end='')
        st-=diff
    
    print()