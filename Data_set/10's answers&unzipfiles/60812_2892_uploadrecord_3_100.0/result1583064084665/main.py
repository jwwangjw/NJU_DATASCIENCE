m, n = [int(i) for i in input().split(' ')]
d = {str(i): 0 for i in range(0, 10)}
for i in range(m, n+1):
    for j in str(i):
        d[j] += 1
if m == 0:
    d['0'] -= 1
label = False
for i in d.values():
    if label:
        print(' ', end='')
    else:
        label = True
    print(i, end='')