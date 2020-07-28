n = int(input())

q1 = list(map(int, input().split()))[1:]
q2 = list(map(int, input().split()))[1:]

s = set()
c = 0
while q1 and q2:
    c += 1
    a = q1.pop(0)
    b = q2.pop(0)
    if a < b:
        q2.append(a)
        q2.append(b)
    else:
        q1.append(b)
        q1.append(a)
    t = (tuple(q1), tuple(q2))
    if t in s:
        break
    s.add(t)

if q1 and q2:
    print(-1)
else:
    print(c, 1 if q1 else 2)
