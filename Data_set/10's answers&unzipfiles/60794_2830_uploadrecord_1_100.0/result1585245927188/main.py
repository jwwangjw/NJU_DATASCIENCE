aa = input().split(" ")
b = int(aa[0])
aaa = input().split(" ")
a = []
for i in range(len(aaa)):
    a.append(int(aaa[i]))
ans = 0
for i in range(len(a)):
    single = a[i]
    for k in range(len(a)-i-1):
        single = single * b
    ans = ans + single
if ans % 2 != 0:
    print("odd")
else:
    print("even")