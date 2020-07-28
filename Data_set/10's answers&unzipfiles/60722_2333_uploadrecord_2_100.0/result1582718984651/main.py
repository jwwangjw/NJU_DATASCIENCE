import math
x=int(input())
y=int(input())
bound=int(input())
mx=int(pow(bound,1/x))
my=int(pow(bound,1/y))
nums=[]
for i in range(mx+1):
    for j in range(my+1):
        nums.append(int(pow(x,i)+pow(y,j)))
nums=list(set(nums))
nums.sort()
move=[]
for i in nums:
    if i>bound:
        move.append(i)
for i in move:
    nums.remove(i)
print(nums)