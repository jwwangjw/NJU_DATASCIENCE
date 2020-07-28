for t in range(int(input())):
    input()
    a = sorted([int(i) for i in input().split()])
    s = 0
    d = 1
    j = a[0]
    a.append(a[-1]+1)
    for i in a[1:]:
        if i == j:
            d += 1
        else:
            s += ((d-1)*d)//2
            d = 1
            j = i
    print(s)
        
    