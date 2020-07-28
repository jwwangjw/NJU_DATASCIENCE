a = input()
b = input()
na = len(a)
res = 0
for i in range(na):
    for j in range(i+1, na+1):
        res += b.count(a[i:j])
print(res)