nums = [int(i) for i in input().split(',')]
tortoise = nums[0]
hare = nums[nums[0]]
while tortoise != hare:
    tortoise = nums[tortoise]
    hare = nums[nums[hare]]
hare = 0
while tortoise != hare:
    hare = nums[hare]
    tortoise = nums[tortoise]
print(hare)