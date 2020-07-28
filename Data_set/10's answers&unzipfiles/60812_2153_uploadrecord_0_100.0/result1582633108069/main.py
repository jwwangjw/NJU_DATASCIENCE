a = input()
if a[0] == '-':
    print('-', end='')
    a = a[-1:0:-1].lstrip('0')
else:
    a = a[::-1].lstrip('0')
for i in a:
    print(i, end='')
print()