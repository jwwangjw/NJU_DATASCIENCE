n = int(input())
m = 0
l = 0
for i in sorted(map(int, input().split())):
    if l >= i:
        m += l - i + 1
        l += 1
    else:
        l = i
print(m)
