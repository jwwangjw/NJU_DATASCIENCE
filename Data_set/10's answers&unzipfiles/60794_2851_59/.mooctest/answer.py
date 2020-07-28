n = int(input())
print(max([sum(map(int, input().split())) for i in range(n)]))
