a = eval(input())
n = len(a)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j] * 2:
            ans += 1
print(ans)