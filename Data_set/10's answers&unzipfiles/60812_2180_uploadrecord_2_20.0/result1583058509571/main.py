def count(s, t):
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if s[i:j] == t:
                res += 1
    return res


a = input()
b = input()
na = len(a)
res = 0
for i in range(na):
    for j in range(i+1, na+1):
        res += count(b, a[i:j])
print(res, end='')