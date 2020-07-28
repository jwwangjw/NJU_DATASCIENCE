n = int(input())
a = list(map(int, input().split()))
r = [a[i] for i in range(n-1) if a[i+1] == 1] + [a[-1]]
print(len(r))
print(*r)
