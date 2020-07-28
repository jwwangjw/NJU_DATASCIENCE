N = int(input())
d = set()
for i in range(N):
    s = ''.join(sorted(input().rstrip(' ')))
    d.add(s)
print(len(d), end='')