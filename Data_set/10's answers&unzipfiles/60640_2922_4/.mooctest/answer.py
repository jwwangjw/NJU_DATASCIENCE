n = int(input())
a = set(map(int, input().split()))
m = "NO"
if len(a) < 4:
    a = sorted(a)
    if len(a) < 3 or a[1]-a[0] == a[2]-a[1]:
        m = "YES"
print(m)
