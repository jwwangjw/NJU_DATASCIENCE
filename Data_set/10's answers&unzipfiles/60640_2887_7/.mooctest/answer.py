n = int(input())
a = [[0, 0], [0, 0]]
for i in range(n):
    t, x, y = map(int, input().split())
    a[t-1][0] += x
    a[t-1][1] += y

for i in a:
    print('LIVE' if i[0] >= i[1] else 'DEAD')
