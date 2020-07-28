n=int(input())
string=str(n)
max=""
for i in range(len(string)):
    if string[i:i+1]>="1":
        max+="1"
    else:
        max+="0"
max=int(max)
choice=[]
while max>0:
    num=n//max
    for i in range(num):
        choice.append(max)
    n=n-num*max
    max=int(str(max),2)-1
    max=int(bin(max).replace("0b",""))
result=""
for i in range(len(choice)-1):
    result=result+str(choice[i])+" "
result+=str(choice[len(choice)-1])
print(len(choice))
print(result)