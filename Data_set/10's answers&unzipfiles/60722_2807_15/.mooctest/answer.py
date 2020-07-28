n, m = map(int, input().split())


def cnt():
    a = [0, 0]
    for i in map(int, input().split()):
        a[i % 2] += 1
    return a


a = cnt()
b = cnt()
print(min(a[0], b[1]) + min(a[1], b[0]))
