n = int(input())
w = [0] * n
h = [0] * n
for i in range(n):
    w[i], h[i] = map(int, input().split())

m = max(w[0], h[0])
for i, j in zip(w, h):
    if i > j:
        i, j = j, i
    if j <= m:
        m = j
    elif i <= m:
        m = i
    else:
        print("NO")
        break
else:
    print("YES")
