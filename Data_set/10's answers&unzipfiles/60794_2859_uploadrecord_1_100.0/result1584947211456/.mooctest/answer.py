n = int(input())
x = [input() for i in range(n)]
a, b = set(), set()
for i in range(n):
    for j in range(n):
        if i == j or i == n - 1 - j:
            a.add(x[i][j])
        else:
            b.add(x[i][j])

print('YES' if a.pop() != b.pop() and not a and not b else 'NO')
