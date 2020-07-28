r=''
while True:
    t=input()
    if '.'in t:
        r+="\n"
        r+=t
        break
    else:
        r+="\n"
        r+=t
L=list(r[1:])
def D(p):
    global L
    L.remove(p)
    print(''.join(L))
def I(p1,p2):
    global L
    L=L[::-1]
    L.insert(L.index(p1)+1,p2)
    L=L[::-1]
    print(''.join(L))
def R(p1,p2):
    global L
    if p1 not in L:
        print("no exist")
    else:
        while p1 in L:
            L[L.index(p1)]=p2
    print(''.join(L))
c=[i for i in input().split()]
if c[0]=="D":
    D(c[1])
elif c[0]=="I":
    I(c[1],c[2])
elif c[0]=="R":
    R(c[1],c[2])