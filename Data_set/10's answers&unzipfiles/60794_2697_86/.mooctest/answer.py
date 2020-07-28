temp=input()
temp=temp[1:len(temp)-1]
temp=temp.split(',')
array=[-1]*len(temp)
for i in range(int(len(temp)/2)):
    if temp[i]!="null":
        array[2*i+1]=int(temp[i])
        array[2*i+2]=int(temp[i])
flag=True
for i in range(1,len(array)):
    if array[i]!=-1:
        if i%2==1:
            if array[i]<=int(temp[i]):
                flag=False
                break
        else:
            if array[i]>=int(temp[i]):
                flag=False
                break
print(str(flag).lower())