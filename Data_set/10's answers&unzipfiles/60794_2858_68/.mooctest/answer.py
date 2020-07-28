n = int(input())
a = [[0] * n] * n
a[0] = [1] * n
for i in range(1, n):
    a[i][0] = 1
    for j in range(1, n):
        a[i][j] = a[i-1][j] + a[i][j-1]
print(a[n-1][n-1])
