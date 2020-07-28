result=[]
def chose(index,goal,string):
    if index==1:
        for i in range(len(goal)):
            stringnew=string+str(goal[i])
            result.append(stringnew)
    else:
        for i in range(len(goal)):
            stringnew=string+str(goal[i])+" "
            goalnew=goal[i+1:]
            chose(index-1,goalnew,stringnew)

n=int(input())
nums=input().split(" ")
nums.sort()
all=0
thing=0
for i in range(n):
    nums[i]=int(nums[i])
    all+=nums[i]
average=all//3
sett=[]
for i in range(n):
    chose(i,nums,"")
move=[]
for i in range(len(result)):
    num=result[i].split(" ")
    sum=0
    for j in range(len(num)):
        sum+=int(num[j])
    if sum!=average:
        move.append(result[i])
for i in range(len(move)):
    result.remove(move[i])
for i in range(len(result)-2):
    for j in range(i+1,len(result)-1):
        for k in range(j+1,len(result)):
            num1=result[i].split(" ")
            num2=result[j].split(" ")
            num3=result[k].split(" ")
            compare=num1+num2+num3
            for l in range(len(compare)):
                compare[l]=int(compare[l])
            compare.sort()
            if compare==nums:
                thing+=1
print(thing)