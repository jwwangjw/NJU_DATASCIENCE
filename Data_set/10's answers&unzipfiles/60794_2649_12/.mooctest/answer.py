for t in range(int(input())):
    n, l, r = [int(x) for x in input().split()]
    for t in range(l-1, r):
        n = n ^ (1 << t)
    print(n)