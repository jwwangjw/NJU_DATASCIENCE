def part(s,x,y):
    i=x-1;j=x
    while(j<y):
        if(s[j]+s[y]>s[y]+s[j]):
            t=s[i+1]
            s[i+1]=s[j]
            s[j]=t
            i+=1
        j+=1
    t=s[i+1]
    s[i+1]=s[j]
    s[j]=t
    i+=1
    return i
    
def f(s,x,y):
    if(x<y):
        k=part(s,x,y)
        return f(s,x,k-1)+s[k]+f(s,k+1,y)
    elif(x==y):
        return s[x]
    return ''
t=int(input())
while(t>0):
    t-=1
    n=int(input())
    s=input().split(' ')
    if '' in s:
        s.remove('')
    s=f(s,0,n-1)
    print(s)