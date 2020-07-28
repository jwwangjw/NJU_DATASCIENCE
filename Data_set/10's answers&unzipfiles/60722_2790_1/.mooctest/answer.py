from bisect import bisect_right

n, m = map(int, input().split())
a = sorted(map(int, input().split()))

print(*(bisect_right(a, i) for i in map(int, input().split())))
