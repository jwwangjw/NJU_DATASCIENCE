def is_available(str1, str2):
    if len(set(str1).intersection(set(str2))) == 0:
        return True
    else:
        return False


def process(arr, cursor, now_str, is_chosen, max_len):
    if cursor >= len(arr):
        if len(now_str) > max_len[0]:
            max_len[0] = len(now_str)
        return  # reach the end of arr

    if is_available(now_str, arr[cursor]) and is_chosen:
        now_str += arr[cursor]

    process(arr, cursor + 1, now_str, True, max_len)  # recursive solution
    process(arr, cursor + 1, now_str, False, max_len)
    # traverse every case, making a tree of situations
    

def entrance():
    arr = input()[2:-2].split("\",\"")
    max_len = [0]  # use list rather than int, cuz we need to use reference
    process(arr, 0, "", True, max_len)
    process(arr, 0, "", False, max_len)
    print(max_len[0])


entrance()
