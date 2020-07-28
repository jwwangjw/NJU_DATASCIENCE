n = int(input())
a = list(map(int, input().split()))
m = 0
for i in range(n):
    for j in range(i+1, n+1):
        x = sum(a[:i]) + (j-i) - sum(a[i:j]) + sum(a[j:])
        m = max(x, m)

print(m)
