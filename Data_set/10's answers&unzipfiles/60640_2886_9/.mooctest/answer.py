n = int(input())
s = set()
m = 1
for i in input().split():
    if i in s:
        s.remove(i)
    else:
        s.add(i)
    m = max(len(s), m)
print(m)
