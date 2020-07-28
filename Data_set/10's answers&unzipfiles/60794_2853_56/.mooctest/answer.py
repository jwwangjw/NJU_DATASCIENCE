n = int(input())
a = list(map(int, input().split()))
c = [0, 0]
for i in a:
    c[i % 2] += 1
print(c[sum(a) % 2])
