def func5():
    nums = eval(input())
    Sum = nums[0]
    while nums[0] < nums[1]:
        Sum &= nums[0]
        nums[0] += 1
    print(Sum)
func5()