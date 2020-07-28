n, k = map(int, input().split())
print(min(k//i for i in map(int, input().split()) if k % i == 0))
