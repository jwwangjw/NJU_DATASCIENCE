nums = [int(i) for i in input().split(',')]
n = len(nums)
start, end = 0, n
while start != end:
    middle = (start+end)//2
    if nums[middle] > nums[end-1]:
        start = middle+1
    else:
        end = middle
print(nums[start])