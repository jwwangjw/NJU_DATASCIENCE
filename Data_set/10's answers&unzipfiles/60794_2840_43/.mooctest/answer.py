n, k = map(int, input().split())
c = 0
for i in input().split():
    if i.count("4") + i.count("7") <= k:
        c += 1
print(c)
