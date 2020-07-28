num=int(input())
for i in range(num):
    length=int(input())
    count=0
    for j in range(length):
        count=count+(length-j)**2
    print(count)