T = int(input())
for i in range(T):
    s = [i.title() for i in input() if i.isalpha()]
    if s == s[::-1]:
        print('YES')
    else:
        print('NO')