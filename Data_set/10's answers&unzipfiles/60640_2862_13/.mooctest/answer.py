n = int(input())
a = [[], []]
for i in map(int, input().split()):
    a[i % 2].append(i)

d = len(a[0]) - len(a[1])
if abs(d) < 2:
    print(0)
else:
    m = a[0] if d > 0 else a[1]
    m.sort()
    print(sum(m[:abs(d)-1]))
