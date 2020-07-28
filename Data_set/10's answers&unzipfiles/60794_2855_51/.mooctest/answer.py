n = int(input())
b = [input() for i in range(n)]
f = True
for i in range(n):
    for j in range(n):
        c = 0
        if i - 1 > -1 and b[i-1][j] == 'o':
            c += 1
        if i + 1 < n and b[i+1][j] == 'o':
            c += 1
        if j - 1 > -1 and b[i][j-1] == 'o':
            c += 1
        if j + 1 < n and b[i][j+1] == 'o':
            c += 1
        if c % 2:
            f = False
            break
    if not f:
        break

print('YES' if f else 'NO')
