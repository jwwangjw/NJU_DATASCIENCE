def summary(number):
    string=str(number)
    total=0
    for i in range(len(string)):
        total=total+int(string[i])
    return total
T=int(input())
for i in range(T):
    number=input()
    temp=input().split()
    num=str(''.join(temp))
    if summary(num)%3==0:
        print(1)
    else:
        print(0)