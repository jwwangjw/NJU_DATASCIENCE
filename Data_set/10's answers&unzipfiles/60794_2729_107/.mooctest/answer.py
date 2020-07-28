def findnum (nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) // 2
        if mid % 2 == 0:
            if nums[mid] == nums[mid+1]:
                left = mid+2
            elif nums[mid] == nums[mid-1]:
                right = mid-2
            else:
                return nums[mid]
        else:
            if nums[mid] == nums[mid + 1]:
                right = mid-1
            elif nums[mid] == nums[mid-1]:
                left = mid+1
            else:
                return nums[mid]
    return nums[left]

mylist=input()
mylist=mylist[1:-1].split(",")
print(findnum(mylist))