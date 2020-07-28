def judge(string):
    if string==string[::-1]:
        return True
    return False
number=int(input())
before=[-1]*number
string=['']*number
for i in range(number-1):
    temp=input().split()
    x=int(temp[0])-1
    y=int(temp[1])-1
    z=temp[2]
    before[y]=x
    string[y]=z
count=1
for i in range(number):
    str=string[i]
    bef=before[i]
    while bef!=-1:
        str=str+string[bef]
        if judge(str):
            count=count+1
        bef=before[bef]
print(count)