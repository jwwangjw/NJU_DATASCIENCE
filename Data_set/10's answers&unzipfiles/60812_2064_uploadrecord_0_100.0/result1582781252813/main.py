s = input()
num = 0
n = len(s)
for i in range(n):
    if s[i] == 'M':
        num += 1000
    elif s[i] == 'D':
        num += 500
    elif s[i] == 'C':
        if i != n-1 and (s[i+1] == 'M' or s[i+1] == 'D'):
            num -= 100
        else:
            num += 100
    elif s[i] == 'L':
        num += 50
    elif s[i] == 'X':
        if i != n-1 and (s[i+1] == 'L' or s[i+1] == 'C'):
            num -= 10
        else:
            num += 10
    elif s[i] == 'V':
        num += 5
    elif i != n-1 and (s[i+1] == 'V' or s[i+1] == 'X'):
        num -= 1
    else:
        num += 1
print(num)