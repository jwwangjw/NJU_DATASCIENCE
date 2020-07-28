t = int(input())
while t:
    t -= 1
    n = int(input())
    a = [0, 0, 0]
    for i in map(int, input().split()):
        a[i % 3] += 1
    print(a[0] + min(a[1], a[2]) + abs(a[1]-a[2])//3)
