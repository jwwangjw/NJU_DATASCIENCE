n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
nums=list(set(nums))
nums.sort()
if len(nums)==1:
    print("Yes")
elif len(nums)==2:
    if nums[0]*2==nums[1] or nums[0]*3==nums[1]:
        print("Yes")
    else:
        print("No")
elif len(nums)==3:
    if nums[0]*3==nums[2] and nums[1]*2==nums[2]:
        print("Yes")
    else:
        print("No")
else:
    print("No")