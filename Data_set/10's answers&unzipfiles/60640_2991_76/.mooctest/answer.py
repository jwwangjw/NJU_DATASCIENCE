def reverse(s):
    list_1=list(s)
    list_2=list_1[::-1]
    for i in list_2:
        if i==' ':
            continue
        else:
            print(i,end='')
s=input()
reverse(s)