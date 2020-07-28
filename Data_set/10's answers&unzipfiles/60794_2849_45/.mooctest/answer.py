n = int(input())
a = sorted(map(int, input().split()))
i = 1
while i < n and a[i] % a[0] == 0:
    i += 1
print(a[0] if i == n else -1)
