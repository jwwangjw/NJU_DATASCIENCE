n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
for i in range(len(nums)):
    a=nums[i]
    while a%2==0:
        a=a//2
    while a%3==0:
        a=a//3
    nums[i]=a
nums=list(set(nums))
if len(nums)==1:
    print("Yes")
else:
    print("No")