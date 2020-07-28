def gensearchtr(strr):
    lst = [[-1, -1] for i in range(10)]
    root = int(strr[0])
    for each in strr:
        troot = root
        each = int(each)
        while each != troot:
            if each < troot:
                if lst[troot][0] == -1:
                    lst[troot][0] = each
                    break
                else:
                    troot = lst[troot][0]
            elif each > troot:
                if lst[troot][1] == -1:
                    lst[troot][1] = each
                    break
                else:
                    troot = lst[troot][1]
    return lst
 
while True:
    try:
        n = int(input())
        if n:
            base = gensearchtr(input())
            for i in range(n):
                tmp = gensearchtr(input())
                print('YES' if tmp == base else 'NO')
        else:
            break
    except:
        break