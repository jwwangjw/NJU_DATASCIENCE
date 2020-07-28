t=int(input())
for i in range(0,t):
    s1=input()
    s2=input()
    c=""
    for j in s1:
        if j in s2:
            c=j
            break
    if c=="":
        print ("$")
    else:
        print(c)
    