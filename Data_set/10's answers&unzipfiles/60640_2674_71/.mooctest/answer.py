t=int(input())
for j in range(0,t):
    s=input()
    a=0
    b=0
    c=0
    for i in range(0,len(s)):
        if s[i]=="a":
            a=(1+2*a)
        elif s[i]=="b":
            b=(a+2*b)
        elif s[i]=="c":
            c=(b+2*c)
    print(c)