nums = [int(i) for i in input().split(',')]
target = int(input())
n = len(nums)
start, end = 0, n
left = True
if target >= nums[start]:
    left = True
else:
    left = False
label = True
while start != end:
    middle = (start+end)//2
    temp = nums[middle]
    if left and temp < nums[start]:
        end = middle
    elif not left and temp > nums[end-1]:
        start = middle+1
    if target > temp:
        start = middle+1
    elif target < temp:
        end = middle
    else:
        print(middle)
        label = False
        break
else:
    if label:
        print(-1)