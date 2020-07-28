T=int(input())
for m in range(T):
    N=int(input())
    nums=input().split(" ")
    count=0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                count+=1
    print(count)