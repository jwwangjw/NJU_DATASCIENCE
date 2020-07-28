n, q = map(int, input().split())
a = sorted(map(int, input().split()))
b = [0] * (n+1)

for i in range(q):
    l, r = map(int, input().split())
    b[l-1] += 1
    b[r] -= 1

for i in range(1, n):
    b[i] += b[i-1]

b[-1] = 1000000
b.sort()

print(sum([a[i]*b[i] for i in range(n)]))
