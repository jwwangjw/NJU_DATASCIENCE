"""
要使得曼哈顿距离等于欧几里得距离
只有在两点在同一直线上时才有成立
"""


def is_equal(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return False
    elif a[0] == b[0] or a[1] == b[1]:
        return True
    return False


t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    points = []
    for j in range(n):
        inp = input().split(" ")
        points.append([int(inp[0]), int(inp[1])])
    for p in range(n-1):
        for q in range(p+1, n):
            if is_equal(points[p], points[q]):
                ans += 1
    print(ans)
