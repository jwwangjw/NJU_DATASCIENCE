n = int(input())
m = int(input())
a = sorted(int(input()) for i in range(n))[::-1]
s = 0
for i, x in enumerate(a, 1):
    s += x
    if s >= m:
        print(i)
        break
