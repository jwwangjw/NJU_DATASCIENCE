a = input().split(",")
b = input().split(",")
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])
if len(b) == 1:
    print(max(b[0]-1, a[len(a)-1] - b[0]))
else:
    ans = b[0] - 1
    for i in range(len(b) - 1):
        if (b[i + 1] - b[i] - 1) % 2 != 0:
            z = b[i + 1] - b[i]
        else:
            z = b[i + 1] - b[i] - 1
        if ans < z / 2:
            ans = z / 2
    if a[len(a)-1]-b[len(b)-1] > ans:
        ans = a[len(a)-1]-b[len(b)-1]
    print(int(ans))