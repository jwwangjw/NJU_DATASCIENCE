aa = input()
a = input().split(" ")
b = input().split(" ")
x = 0
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j] and b[i] > b[j]:
            x = 1
if x == 0:
    print("Poor Alex")
else:
    print("Happy Alex")