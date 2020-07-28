n = int(input())
a = [0, 0]
for i in map(int, input().split()):
    a[i % 2] += 1
print(min(a))
