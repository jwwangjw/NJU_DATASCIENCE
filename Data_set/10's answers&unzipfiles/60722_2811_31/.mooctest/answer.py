p, n = map(int, input().split())
s = set()
r = -1
for i in range(1, n+1):
    x = int(input()) % p
    if x in s:
        r = i
        break
    s.add(x)

print(r)
