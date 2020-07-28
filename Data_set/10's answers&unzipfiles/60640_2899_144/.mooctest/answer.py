def func6():
    num = int(input())
    if num < 0:
        num = -num
    if num & (num - 1) == 0:
        if num & 0x55555555 > 0:
            print("true")
        else:
            print("false")
    else:
        print("false")
func6()