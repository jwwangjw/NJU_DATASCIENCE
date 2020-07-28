def sortrule(x, y):
    global S
    if S.index(x) < S.index(y):
        return -1
    elif S.index(x) > S.index(y):
        return 1
    else:
        return 0


from functools import cmp_to_key

S = input()
T = input()
a, b = [], []
for i in T:
    if i in S:
        a.append(i)
    else:
        b.append(i)
a = sorted(a, key=cmp_to_key(sortrule))
print(''.join(a)+''.join(b))