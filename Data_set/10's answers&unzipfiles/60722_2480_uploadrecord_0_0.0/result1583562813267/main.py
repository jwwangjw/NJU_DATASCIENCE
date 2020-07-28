T=int(input())
for m in range(T):
    N=int(input())
    nums=input().split(" ")
    even=[]
    odd=[]
    for i in range(N):
        nums[i]=int(nums[i])
        if nums[i]%2==0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    result=even+odd
    print(" ".join(str(i) for i in result))
    