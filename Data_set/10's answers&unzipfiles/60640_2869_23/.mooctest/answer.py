n = int(input())
s = set()
a = []
for i in reversed(list(map(int, input().split()))):
    if i not in s:
        s.add(i)
        a.append(i)

print(len(a))
print(*reversed(a))
