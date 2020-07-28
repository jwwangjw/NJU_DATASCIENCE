a = input()
b = input()
x = 0
if len(a) != len(b):
    print(1)
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            if chr(ord(a[i])-32) == b[i] or chr(ord(a[i])+32) == b[i]:
                x = 1
                continue
            else:
                x = 2
                print(4)
                break
    if x == 0:
        print(2)
    elif x == 1:
        print(3)