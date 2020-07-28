n = int(input())
s = set(list(map(int, input().split()))) - set([0])
print(len(s))
