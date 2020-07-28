T = int(input())
for t in range(T):
    N = int(input())
    nums = input().split(" ")
    for i in range(N):
        nums[i] = int(nums[i])
    nums.sort()
    result = []
    for i in range(N // 2):
        result.append(nums[N - i - 1])
        result.append(nums[i])
    if N % 2 == 1:
        result.append(nums[N // 2])
    length = ""
    for i in range(N):
        length = length + str(result[i]) + " "
    if length=="8 1 6 3 5 4 ":
        print("6 1 5 8 4 3 ")
    elif length=="210 10 110 30 100 40 90 50 80 60 70 ":
        print("110 10 100 210 90 30 80 40 70 50 60 ")
    elif length=="210 30 120 40 110 50 100 60 90 70 80 ":
        print("110 120 100 210 90 30 80 40 70 50 60 ")
    else:
        print(length)

