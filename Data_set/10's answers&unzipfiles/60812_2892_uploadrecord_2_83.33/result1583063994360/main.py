m, n = [int(i) for i in input().split(' ')]
if m == 0 and n == 0:
    print('0 0 0 0 0 0 0 0 0 0',end='')
else:
    d = {str(i): 0 for i in range(0, 10)}
    for i in range(m, n+1):
        for j in str(i):
            d[j] += 1
    label = False
    for i in d.values():
        if label:
            print(' ', end='')
        else:
            label = True
        print(i, end='')