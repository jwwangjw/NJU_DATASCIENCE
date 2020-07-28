import bisect

n = int(input())
c = [0] * (n + 1)
for i, x in enumerate(map(int, input().split()), 1):
    c[i] = c[i-1] + x

m = int(input())
for i in map(int, input().split()):
    print(bisect.bisect_right(c, i-1))
