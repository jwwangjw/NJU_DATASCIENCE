nums1=input().split(",")
nums2=input().split(",")
nums=nums1+nums2
for i in range(len(nums)):
    nums[i]=int(nums[i])
nums.sort()
if len(nums)%2==1:
    print(str(nums[len(nums)//2])+".0")
else:
    print(format((nums[len(nums)//2-1]+nums[len(nums)//2])/2,'.5f'))