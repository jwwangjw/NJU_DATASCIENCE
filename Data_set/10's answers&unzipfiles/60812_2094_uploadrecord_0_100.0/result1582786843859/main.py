try:
    a = input().strip(' ')
    b = a.count('e')
    if b > 1:
        print('False')
    else:
        if b == 1:
            temp = [i for i in a.split('e')]
            float(temp[0])
            int(temp[1])
        else:
            float(a)
        print('True')
except ValueError:
    print('False')