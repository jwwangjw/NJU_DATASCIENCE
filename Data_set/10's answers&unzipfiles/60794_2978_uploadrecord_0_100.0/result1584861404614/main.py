b = input()
a = [[], []]
y = 0
for i in range(len(b)):
    if b[i] == " ":
        y = 1
        continue
    else:
        if y == 1:
            a[1].append(b[i])
        else:
            a[0].append(b[i])
x = 0
for i in range(min(len(a[0]), len(a[1]))):
    if ord(a[0][i]) != ord(a[1][i]):
        x = 1
        print(ord(a[0][i]) - ord(a[1][i]))
        break
if x == 0:
    print(0)
