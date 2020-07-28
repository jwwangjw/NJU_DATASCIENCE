
for t in range(int(input())):
    m = int(input().split()[1])
    a = sorted([int(i) for i in input().split()])
    s = 0
    c = 0
    for i in a:
        s += i
        if s > m:
            break
        c += 1
    print(c)