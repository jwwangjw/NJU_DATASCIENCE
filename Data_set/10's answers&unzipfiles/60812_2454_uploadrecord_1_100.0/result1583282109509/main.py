nums = [int(i) for i in input().split(',')]
n = len(nums)
start, end, middle = 0, n, n//2
while start != end:
    if nums[middle] > nums[end-1]:
        start = middle+1
    elif nums[middle] < nums[end-1]:
        end = middle+1
    else:
        break
    middle = (start + end) // 2
print(min(nums[start],nums[middle]))