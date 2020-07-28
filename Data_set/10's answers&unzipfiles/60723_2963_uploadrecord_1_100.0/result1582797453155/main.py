def judge(string):
    if string==string[::-1]:
        return True
    return False
def get_path(before,string,i,j):
    path_i=[]
    path_j=[]
    bef=i
    while bef!=-1:
        path_i.append(bef)
        bef=before[bef]
    bef = j
    while bef != -1:
        path_j.append(bef)
        bef = before[bef]
    begin=0
    result=''
    while path_i[begin] not in path_j:
        result=result+string[path_i[begin]]
        begin=begin+1
    path_j=path_j[:len(path_j)-(len(path_i)-begin)]
    path_j.reverse()
    for item in path_j:
        result=result+string[item]
    return result
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
count=0
for i in range(number-1):
    for j in range(i+1,number):
        path=get_path(before,string,i,j)
        if judge(path):
            count=count+1
print(count)