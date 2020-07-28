n = int(input())
a = [int(i)-1 for i in input().split()]
f = False
for i in range(n):
    if a[a[a[i]]] == i:
        f = True
        break

print("YES" if f else "NO")
