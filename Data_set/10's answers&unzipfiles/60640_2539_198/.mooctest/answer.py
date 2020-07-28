def func():
    arr = [int(x) for x in input()[1:-1].split(", ")]

    arr_sorted = sorted(arr)
    L = 0
    R = 0
    i = 0
    while i < len(arr):
        if arr[i] != arr_sorted[i]:
            L = i
            break
        i += 1

    i = len(arr) - 1
    while i > -1:
        if arr[i] != arr_sorted[i]:
            R = i
            break
        i -= 1

    print(R - L + 1)


func()
