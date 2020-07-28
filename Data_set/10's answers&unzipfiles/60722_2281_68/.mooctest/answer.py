T = int(input())
for i in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    # print('lst', lst)
    output_str = str(lst[n-1])
    maxx = lst[n-1]
    if n < 3:
        if lst[0] > lst[1]:
            output_str = str(lst[0]) + ' ' + output_str
            break
    for num in range(n-2, -1, -1):
        if lst[num] >= maxx:
            output_str = str(lst[num]) + ' '  + output_str
        maxx = max(lst[num], maxx)
    print(output_str)