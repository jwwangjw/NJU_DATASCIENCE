list=input().lstrip('[').rstrip(']').split(',')
size=len(list)
if size<2:
    print('0')
else:
    for i in range(size):
        list[i]=int(list[i])
    list.sort()
    max=0
    for j in range(size-1):
        if max<list[j+1]-list[j]:
            max=list[j+1]-list[j]
    
    print(max)