def z(l):
    length=len(l)
    if length==0 or length==1:
        print(l)
        return
    l=sorted(l)
    r=[]
    r.append(l[length//2])
    index=0
    while len(r)<length:
        if len(r)<length:
            if r[-1]!=l[index]:
                r.append(l[index])
        else:
            print(r)
            return
        if len(r)<length:
            if r[-1]!=l[-(index+1)]:
                r.append(l[-(index+1)])
        else:
            print(r)
            return
        if len(r)%2==1:
            index+=1
    print(r) 

if __name__ == '__main__':
    z([int(i) for i in input()[1:-1].split(',')])
