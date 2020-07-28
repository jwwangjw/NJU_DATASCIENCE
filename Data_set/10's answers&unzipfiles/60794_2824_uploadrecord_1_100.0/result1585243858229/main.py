pp = input().split()
t = int(pp[1])
n = int(pp[2])
aaa = input().split(" ")
a = []
for i in range(len(aaa)):
    a.append(int(aaa[i]))
ans = 0
for i in range(len(a)-(n-1)):
    p = 0
    for j in range(n):
        if a[i+j] > t:
            p = 1
    if p == 0:
        ans = ans + 1
print(ans)