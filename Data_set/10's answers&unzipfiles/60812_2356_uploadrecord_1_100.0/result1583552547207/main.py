T = int(input())
for i in range(T):
    N = int(input())
    nums = [int(i) for i in input().split(' ')]
    left = False
    biggest = big = nums[0]
    for i in range(1, N-1):
        if nums[i] > biggest:
            biggest = nums[i]
        if left:
            if nums[i] < big:
                left = False
                big = biggest
        elif nums[i] >= big:
                big = nums[i]
                left = True
    if left and nums[N-1] >= big:
        print(big)
    else:
        print(-1)