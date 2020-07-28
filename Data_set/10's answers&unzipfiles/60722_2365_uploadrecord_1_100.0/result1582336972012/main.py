T=int(input())
for t in range(T):
    N=int(input())
    nums=input().split(" ")
    nums.sort()
    nums.reverse()
    for i in range(N-1):
        if nums[i]==nums[i+1]+"0":
            index=nums[i]
            nums[i]=nums[i+1]
            nums[i+1]=index
    result=""
    for i in range(N):
        result+=nums[i]
    print(result)