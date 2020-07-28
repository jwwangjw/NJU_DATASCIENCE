n=int(input())
nums=[]
for i in range(n):
    string=input().split(",")
    for j in range(n):
        nums.append(int(string[j]))
nums.sort()
k=int(input())
print(nums[k-1])