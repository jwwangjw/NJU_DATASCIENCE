n = int(input())
a = [tuple(map(int, input().split())) for i in range(n)]
print("Poor Alex" if sorted(a, key=lambda x: x[0]) == sorted(
    a, key=lambda x: x[1]) else "Happy Alex")
