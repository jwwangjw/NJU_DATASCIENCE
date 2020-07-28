num = int(input())
s = ''
while num != 0:
    t = num % 26
    num //= 26
    if t == 0:
        s = 'Z'+s
        num -= 1
    else:
        s = chr(t+64) + s
print(s)