n = int(input())
a = list(map(int, input().split()))
b = [0] * n
m = 0
for i in range(n-1, -1, -1):
    b[i] = a[i] - m
    m = -1 * (b[i] + m)
print(*b)
