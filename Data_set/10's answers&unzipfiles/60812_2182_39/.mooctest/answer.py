t=int(input(''))
while(t>0):
    t=t-1
    s=input('').split(' ')
    n=int(s[0])
    k=int(s[1])
    s=[]
    for i in range(n):
        s.append(i+1)
    p=0
    while(len(s)>1):
       p=(p+k-1)%len(s)
       del s[p]
    print(s[0])