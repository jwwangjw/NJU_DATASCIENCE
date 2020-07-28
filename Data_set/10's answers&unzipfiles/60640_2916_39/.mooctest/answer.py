n = int(input())
m = {}
for i, x in enumerate("4 8 15 16 23 42".split()):
    m[x] = i
c = [0] * 6
cnt = 0
for i in input().split():
    if m[i] == 0 or c[m[i]] < c[m[i]-1]:
        c[m[i]] += 1
        if i == '42' and all(x-cnt > 0 for x in c):
            cnt += 1

print(n-cnt*6)
