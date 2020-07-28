n = int(input())
c = 0
s = 0
for i in sorted(map(int, input().split())):
    if s > i:
        continue
    s += i
    c += 1
print(c)
