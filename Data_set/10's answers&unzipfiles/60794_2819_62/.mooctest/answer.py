n = int(input())
a = [0] * 5
for i in map(int, input().split()):
    a[i] += 1
_, a1, a2, a3, a4 = a
print(a4 + a3 + a2//2 + (max(0, a1 - a3) + a2 % 2 * 2 + 3) // 4)
