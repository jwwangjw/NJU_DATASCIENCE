a = int(input())
arr = []
ans = 1
for i in range(a):
    arr.append(list(input()))
li = arr[0][0]
for i in range(a):
    if arr[i][i] != li:
        ans = 0
    arr[i][i] = ","
for i in range(a):
    if arr[i][a - 1 - i] != li and arr[i][a - 1 - i] != ",":
        ans = 0
    arr[i][a - 1 - i] = ","
re = arr[0][1]
for i in range(a):
    for j in range(a):
        if arr[i][j] == ",":
            continue
        else:
            if arr[i][j] != re:
                ans = 0
if ans == 0:
    print("NO")
else:
    print("YES")