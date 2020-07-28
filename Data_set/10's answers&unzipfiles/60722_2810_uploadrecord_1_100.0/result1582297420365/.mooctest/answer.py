n = int(input())
a = []
while n > 0:
    x = n
    b = []
    while x:
        if x % 10:
            b.append('1')
        else:
            b.append('0')
        x //= 10
    b = int(''.join(b[::-1]))
    a.append(b)
    n -= b

print(len(a))
print(*sorted(a)[::-1])
