n = int(input())
r = list(map(int, input().split()))
a, b = map(int, input().split())
print(sum(r[a-1:b-1]))
