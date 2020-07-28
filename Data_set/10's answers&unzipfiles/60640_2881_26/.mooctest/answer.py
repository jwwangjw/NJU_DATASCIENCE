n = int(input())
a, b, d = (n-1)//2, 1, 1
for i in range(n):
    if a == 0:
        b = -1
    print('*' * a + 'D' * d + '*' * a)
    a -= b
    d += b * 2
