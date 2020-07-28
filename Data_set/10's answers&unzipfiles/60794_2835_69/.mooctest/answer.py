n = int(input())
z = input().count('0')
f = n - z
if z == 0:
    print(-1)
elif f < 9:
    print(0)
else:
    print('5' * (f//9)*9 + '0' * z)
