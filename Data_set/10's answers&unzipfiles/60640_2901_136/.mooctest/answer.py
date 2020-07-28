def func12():
    val = int(input())
    res = str(bin(val))
    flag = True
    for i in range(3, len(res)):
        if res[i] == res[i - 1]:
            flag = False
            break
    print(flag)
func12()
