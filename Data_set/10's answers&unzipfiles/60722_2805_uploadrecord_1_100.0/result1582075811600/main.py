n=int(input())
nums=input().split(" ")
longest=1
for i in range(n):
    nums[i]=int(nums[i])
for i in range(n-1):
    length=1
    for j in range(i+1,n):
        if nums[j]>nums[j-1]:
            length+=1
        else:
            break
    if length>longest:
        longest=length
print(longest)