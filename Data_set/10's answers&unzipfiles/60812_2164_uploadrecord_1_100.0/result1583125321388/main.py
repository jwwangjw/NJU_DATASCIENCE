T = int(input())
for i in range(T):
    s = input()
    n = len(s)
    se = set()
    for j in s:
        se.add(j)
    print(n-len(se))