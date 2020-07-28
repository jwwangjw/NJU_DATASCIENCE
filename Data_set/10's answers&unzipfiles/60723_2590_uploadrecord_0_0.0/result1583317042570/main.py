num=int(input())
for i in range(num):
    temp=list(input())
    temp.sort()
    for j in range(len(temp)-1,0,-1):
        if temp[j]==temp[j-1]:
            temp.pop(j-1)
    if len(temp)%2==1:
        print('HE！')
    else:
        print('SHE！')