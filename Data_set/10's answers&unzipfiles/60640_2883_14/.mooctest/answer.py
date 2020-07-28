n, m = map(int, input().split())
for i in range(1, n+1):
    a = input()
    try:
        l = a.index('B')
        r = a.rindex('B')
        d = (r - l) // 2
        print(i + d, l + d + 1)
        break
    except ValueError:
        continue
