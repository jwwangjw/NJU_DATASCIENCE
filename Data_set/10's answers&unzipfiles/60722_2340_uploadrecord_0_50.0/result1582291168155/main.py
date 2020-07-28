T=int(input())
for i in range(T):
    N=int(input())
    nums=input().split(" ")
    for j in range(N):
        nums[j]=int(nums[j])
    max_num=min(nums[0],nums[N-1])
    water=0
    for j in range(1,N-1):
        water=water+max_num-nums[j]
        if nums[j]>=max_num:
            water=0
            break
    print(water)