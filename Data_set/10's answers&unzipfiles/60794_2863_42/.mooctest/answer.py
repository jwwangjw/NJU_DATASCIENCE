n, h = map(int, input().split())
print(sum(1 for i in input().split() if int(i) > h) + n)
