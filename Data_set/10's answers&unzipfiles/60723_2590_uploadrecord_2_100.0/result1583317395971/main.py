num=int(input())
for i in range(num):
    temp=list(input())
    temp.sort()
    for j in range(len(temp)-1,0,-1):
        if temp[j]=='a' or temp[j]=='o' or temp[j]=='u' or temp[j]=='i' or temp[j]=='e':
            temp.pop(j)
        elif temp[j]==temp[j-1]:
            temp.pop(j-1)
    if temp[0]=='a' or temp[0]=='o' or temp[0]=='u' or temp[0]=='i' or temp[0]=='e':
        temp.pop(0)
    if len(temp)%2==1:
        print('HE!')
    else:
        print('SHE!')