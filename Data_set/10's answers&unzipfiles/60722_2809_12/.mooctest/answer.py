n = int(input()) // 2
a = sorted(map(int, input().split()))
print(sum(a[:n])**2 + sum(a[n:])**2)
