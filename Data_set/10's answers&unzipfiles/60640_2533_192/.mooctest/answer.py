def func():
    arr = [int(x) for x in input()[1:-1].split(",")]
    arr_odd = []
    arr_even = []
    for ele in arr:
        if ele % 2 == 1:
            arr_odd.append(ele)
        else:
            arr_even.append(ele)
    arr_odd.sort()
    arr_even.sort()

    arr_res = arr_even + arr_odd
    print(arr_res)


func()
