n, k = map(int, input().split())
s = [0] * (k + 1)
for i in range(n):
    a = list(map(int, input().split()))
    for j in a[1:]:
        s[j] = 1
print("YES" if sum(s) == k else "NO")
