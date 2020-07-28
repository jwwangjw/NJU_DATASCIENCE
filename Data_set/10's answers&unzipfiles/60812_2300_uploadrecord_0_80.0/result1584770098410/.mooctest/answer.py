def stree (num):
    list_1 = []
    for i in num:
        if i == '#' and len (list_1) != 0:
            print (list_1.pop (), end=' ')
        else:
            list_1.append (i)
if __name__ == '__main__':
    while True:
        try:
            num = input ()
            stree (num)
        except:
            break