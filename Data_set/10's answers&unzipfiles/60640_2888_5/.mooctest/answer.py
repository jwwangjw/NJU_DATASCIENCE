n, m = map(int, input().split())
a = list(map(int, input().split()))
x = a.count(1)
y = len(a) - x
while m > 0:
    m -= 1
    l, r = map(int, input().split())
    if (r-l+1) % 2:
        print(0)
    else:
        if (r - l + 1) / 2 <= x and (r - l + 1) / 2 <= y:
            print(1)
        else:
            print(0)
