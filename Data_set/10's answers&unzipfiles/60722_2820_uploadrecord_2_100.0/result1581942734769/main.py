n=int(input())
time=[]
nums=[]
for i in range(n):
    time.append(input())
for i in range(n):
    num=1
    for j in range(i+1,n):
        if time[i]==time[j]:
            num+=1
    nums.append(num)
nums.sort()
print(nums[len(nums)-1])