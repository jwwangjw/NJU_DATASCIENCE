n = int(input())
if n == 1:
    print(1)
else:
    a = [tuple(map(int, input().split())) for i in range(n)]
    c = 2
    l = a[0][0]
    for i in range(1, n-1):
        if a[i][0] - a[i][1] > l:
            l = a[i][0]
            c += 1
        elif sum(a[i]) < a[i+1][0]:
            l = sum(a[i])
            c += 1
        else:
            l = a[i][0]

    print(c)
