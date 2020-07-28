T=int(input())
for m in range(T):
    n=int(input())
    nums=input().split(" ")
    for i in range(len(nums)):
        nums[i]=int(nums[i])
    result=[]
    for i in range(len(nums)):
        index=[]
        for j in range(i+1,len(nums)):
            if nums[j]>=nums[i]:
                index.append(nums[j])
        if len(index)==0:
            result.append(-1)
        else:
            result.append(index[0])
    print(" ".join(str(i) for i in result))