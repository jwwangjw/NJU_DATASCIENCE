n = int(input())
s = set()
for i in range(n):
    x = input()
    print("YES" if x in s else "NO")
    s.add(x)
