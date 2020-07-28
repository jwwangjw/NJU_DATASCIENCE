n, m = map(int, input().split())
s = list(map(int, input().split()))
k = set(map(int, input().split()))
r = [i for i in s if i in k]
print(*r)
