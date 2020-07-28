n=int(input())
nums=input().split(" ")
grade=input().split(" ")
for i in range(n-1):
    nums[i]=int(nums[i])
a=int(grade[0])
b=int(grade[1])
num=0
for i in range(a-1,b-1):
    num+=nums[i]
print(num)