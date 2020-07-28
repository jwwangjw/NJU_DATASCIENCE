n = int(input())
a = [0] * n
for i, x in enumerate(map(int, input().split()), 1):
    a[x-1] = i
print(*a)
