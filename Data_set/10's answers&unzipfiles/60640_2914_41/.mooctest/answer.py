t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = [a[i]-b[i] for i in range(n)]
    i, j = 0, n-1
    while i < n and a[i] == 0:
        i += 1
    while j > i and a[j] == 0:
        j -= 1
    if i < n and a[i] > 0:
        print('NO')
    else:
        for i in range(i, j):
            if a[i] != a[i+1]:
                print('NO')
                break
        else:
            print('YES')
