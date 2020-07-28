T=int(input())
for t in range(T):
    N=int(input())
    nums=input().split(" ")
    for i in range(N):
        nums[i]=int(nums[i])
    nums.sort()
    result=[]
    for i in range(N//2):
        result.append(nums[N-i-1])
        result.append(nums[i])
    if N%2==1:
        result.append(nums[N//2])
    length=""
    for i in range(N):
        length=length+str(result[i])+" "
    print(length[:len(length)-1])
