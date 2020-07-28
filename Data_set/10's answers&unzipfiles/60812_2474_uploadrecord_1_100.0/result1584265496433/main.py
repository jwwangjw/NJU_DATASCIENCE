T = int(input())
for i in range(T):
    left = 0
    length = temp = 0
    for i in input():
        if i == '(':
            left += 1
        elif left != 0:
            left -= 1
            temp += 2
        else:
            length = max(length, temp)
            temp = 0
    print(max(length,temp))