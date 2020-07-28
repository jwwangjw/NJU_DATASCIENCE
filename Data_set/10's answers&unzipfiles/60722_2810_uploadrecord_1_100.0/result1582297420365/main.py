n=int(input())
string=str(n)
all=[]
for i in range(len(string)):
    all.append(int(string[i:i+1]))
max_num=max(all)
print(max_num)
all_num=[]
for i in range(max_num):
    num=""
    for j in range(len(all)):
        if all[j]!=0:
            all[j]-=1
            num+="1"
        else:
            num+="0"
    all_num.append(num)
for i in range(len(all_num)):
    for j in range(len(all_num[i])):
        if all_num[i][j:j+1]=="1":
            break
    all_num[i]=all_num[i][j:]
result=""
for i in range(len(all_num)):
    result=result+all_num[i]+" "
print(result[:len(result)-1])