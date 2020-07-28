from collections import defaultdict
a = defaultdict(int)
for i in map(int, input().split()):
    a[i] += 1
d = defaultdict(int)
for v in a.values():
    d[v] += 1
if d[6] or (d[4] and d[2]):
    print('Elephant')
elif d[5] or (d[4] and d[1] == 2):
    print('Bear')
else:
    print('Alien')
