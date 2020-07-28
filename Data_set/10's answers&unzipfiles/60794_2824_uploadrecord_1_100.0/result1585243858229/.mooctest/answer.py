n, t, c = map(int, input().split())
m = 0
j = 0
for i in map(int, input().split()):
    if i <= t:
        j += 1
    else:
        if j >= c:
            m += j - c + 1
        j = 0
if j >= c:
    m += j - c + 1
print(m)
