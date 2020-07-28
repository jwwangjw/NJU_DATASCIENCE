t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    a=[]
    s=input().split(' ')
    if '' in s:
        s.remove('')
    for i in range(n):
        s[i]=int(s[i])
        a.append(s[i])
    m1=max(s)
    s.remove(m1)
    m2=max(s)
    s.remove(m2)
    m3=max(s)
    s.remove(m3)
    n1=min(a)
    a.remove(n1)
    n2=min(a)
    print(max(n1*n2*m1,m1*m2*m3))
    