a = input()
aa = a[1: len(a)-1].split(",")
b = []
for x in aa:
    b.append(int(x))
i = 0
while True:
    temp = b[i]
    if temp == b[i+1]:
        b.pop(i)
        b.pop(i)
    elif temp != b[i+1]:
        print(b[i])
        break
