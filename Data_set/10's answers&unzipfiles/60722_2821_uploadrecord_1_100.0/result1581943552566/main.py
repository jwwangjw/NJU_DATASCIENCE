n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
a=0
b=0
for i in range(n):
    choice=nums[0]
    if nums[len(nums)-1]>choice:
        choice=nums[len(nums)-1]
    if i%2==0:
        a+=choice
    else:
        b+=choice
    nums.remove(choice)
print(str(a)+" "+str(b))