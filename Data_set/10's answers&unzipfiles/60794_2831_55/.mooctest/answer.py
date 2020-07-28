n = int(input())
a = list(map(int, input().split()))
s, t = sorted(map(int, input().split()))
print(min(sum(a[s-1:t-1]), sum(a[:s-1]+a[t-1:])))
