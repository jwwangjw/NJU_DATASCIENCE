a = eval(input())
list.sort(a)
ans = 0
for i in range(len(a) - 1):
    if ans < a[i] - a[i + 1] or ans < a[i + 1] - a[i]:
        if a[i + 1] - a[i] > 0:
            ans = a[i + 1] - a[i]
        else:
            ans = a[i] - a[i + 1]
print(ans)