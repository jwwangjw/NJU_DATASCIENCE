N=int(input())
nums=input().split(" ")
for i in range(N):
    nums[i]=int(nums[i])
if sum(nums)%3!=0:
    print(0)
else:
    count=0
    avarage=sum(nums)//3
    for i in range(1,N):
        for j in range(i,N):
            if sum(nums[:i])==avarage and sum(nums[i:j])==avarage and sum(nums[j:])==avarage:
                count+=1
    print(count)
