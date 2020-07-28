n = int(input())
for _ in range(n):
    num = int(input())
    temp_lst = [j for j in range(1, num+1)]
    final_card_list = [None] * num
    count = 1
    for i in range(1, num + 1):
        if len(temp_lst) >= i:
            temp_lst = temp_lst[i:] + temp_lst[:i]
            temp = temp_lst[0]
            del temp_lst[0]
            final_card_list[temp - 1] = count
        else:
            rotate = i % len(temp_lst)
            temp_lst = temp_lst[rotate:] + temp_lst[:rotate]
            temp = temp_lst[0]
            del temp_lst[0]
            final_card_list[temp - 1] = count
        count += 1

    print(" ".join([str(i) for i in final_card_list]))