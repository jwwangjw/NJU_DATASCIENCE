c = eval(input())
a = []
b = []
for n in c:
    if n % 2 == 0: a.append(n)
    else: b.append(n)
c = []
for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])
print(c)