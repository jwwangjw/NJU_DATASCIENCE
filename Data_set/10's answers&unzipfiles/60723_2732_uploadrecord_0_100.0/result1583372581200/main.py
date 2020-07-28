num=int(input())
for i in range(num):
    temp=input().split()
    A=int(temp[0])
    B=int(temp[1])
    C=int(temp[2])
    print((A**B)%C)