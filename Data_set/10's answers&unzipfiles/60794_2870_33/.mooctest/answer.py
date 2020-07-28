n = int(input())
a = sorted(map(int, input().split()))
s = sum(a)
if s % 2:
    for i in a:
        if i % 2:
            s -= i
            break
print(s)
