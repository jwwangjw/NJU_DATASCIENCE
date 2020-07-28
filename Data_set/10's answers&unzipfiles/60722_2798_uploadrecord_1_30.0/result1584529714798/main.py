def DFS(res,num,choice):
    global subSet,nums,N
    if num==1:
        for i in range(choice,N):
            result=res[:]
            result.append(nums[i])
            subSet.append(result)
    else:
        for i in range(choice,N-num+1):
            result=res[:]
            result.append(nums[i])
            DFS(result,num-1,i+1)

N=int(input())
nums=input().split(" ")
for i in range(N):
    nums[i]=int(nums[i])
nums.sort()
subSet=[]
for i in range(1,N+1):
    DFS([],i,0)
if sum(nums)%3!=0:
    print(0)
else:
    result=[]
    average=sum(nums)//3
    choice=[]
    for i in range(len(subSet)):
        if sum(subSet[i])==average:
            choice.append(subSet[i])
    for i in range(len(choice)):
        for j in range(len(choice)):
            for k in range(len(choice)):
                if i!=j and i!=k and j!=k:
                    cmp=choice[i]+choice[j]+choice[k]
                    cmp.sort()
                    if cmp==nums:
                        temp=[choice[i],choice[j],choice[k]]
                        temp.sort()
                        temp=temp[0]+temp[1]+temp[2]
                        result.append(" ".join(str(l) for l in temp))
    result=list(set(result))
    print(len(result))