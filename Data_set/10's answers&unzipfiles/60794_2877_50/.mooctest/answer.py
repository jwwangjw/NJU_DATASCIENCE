n = int(input())
b, c = 0, 0
for i in map(int, input().split()):
    if i < 0:
        c += i
    else:
        b += i

print(b - c)
