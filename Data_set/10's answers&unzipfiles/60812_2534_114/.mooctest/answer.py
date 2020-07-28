def func():
    arr_pre = input()[2:-2].split("],[")
    arr = []
    for ele in arr_pre:
        arr += [int(x) for x in ele.split(",")]
    print(sorted(arr))


func()
