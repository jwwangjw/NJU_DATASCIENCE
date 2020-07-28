def func():
    number = int(input())
    number_str_sorted = sorted(str(number))

    two_pow_s = []
    i = 0
    while i < 42:
        temp_num = 2 ** i
        two_pow_s.append(sorted(str(temp_num)))
        i += 1

    if number_str_sorted in two_pow_s:
        print("true")
    else:
        print("false")


func()
