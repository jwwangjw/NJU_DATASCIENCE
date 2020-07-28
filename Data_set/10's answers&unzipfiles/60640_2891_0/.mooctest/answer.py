n = int(input())
a = sorted(map(int, input().split()))
print(n*a[-1] - sum(a))
