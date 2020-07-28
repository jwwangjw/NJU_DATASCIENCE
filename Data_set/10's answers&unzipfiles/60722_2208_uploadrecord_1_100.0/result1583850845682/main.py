T=int(input())
for m in range(T):
    n=int(input())
    nums=input().split(" ")
    for i in range(len(nums)):
        nums[i]=int(nums[i])
    result=[-1]
    for i in range(1,len(nums)):
        index=[]
        for j in range(0,i):
            if nums[j]<nums[i]:
                index.append(nums[j])
        if len(index)==0:
            result.append(-1)
        else:
            result.append(index[-1])
    print(" ".join(str(i) for i in result)+" ")
