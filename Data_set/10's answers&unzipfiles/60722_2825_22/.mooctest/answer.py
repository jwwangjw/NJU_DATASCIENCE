n = int(input())
a = [sum(map(int, input().split())) for i in range(n)]
s = a[0]
a = sorted(a)[::-1]
print(a.index(s)+1)
