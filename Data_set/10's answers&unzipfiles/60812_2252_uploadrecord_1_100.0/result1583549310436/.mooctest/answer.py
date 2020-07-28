a=int(input())
for _ in range(a):
    b=input()
    c=list(input())
    c.sort()
    cc=0
    for i in range(len(b)-len(c)+1):
        d=list(b[i:i+len(c)])
        d.sort()
        if(c==d):
            cc+=1
    print(cc)