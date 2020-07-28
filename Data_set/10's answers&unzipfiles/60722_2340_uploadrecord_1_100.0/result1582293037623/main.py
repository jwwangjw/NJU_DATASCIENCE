T=int(input())
for i in range(T):
    N=int(input())
    nums=input().split(" ")
    for j in range(N):
        nums[j]=int(nums[j])
    index=[0]
    water=0
    for j in range(N-1):
        if nums[j]<nums[j+1]:
            index.append(j+1)
    move=[]
    for j in range(len(index)-1):
        if index[j]+1==index[j+1]:
            move.append(index[j])
    for j in range(len(move)):
        index.remove(move[j])
    for j in range(len(index)-1):
        left=index[j]
        right=index[j+1]
        max_num=min(nums[left],nums[right])
        if left+1==right:
            continue
        else:
            for k in range(left+1,right):
                water=water+max_num-nums[k]
    print(water)