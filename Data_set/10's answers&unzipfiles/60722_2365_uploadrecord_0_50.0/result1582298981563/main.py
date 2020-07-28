T=int(input())
for t in range(T):
    N=int(input())
    nums=input().split(" ")
    nums.sort()
    nums.reverse()
    result=""
    for i in range(N):
        result+=nums[i]
    print(result)