T = int(input())
for i in range(T):
    M, N = [int(i) for i in input().split(' ')]
    nums = [int(i) for i in input().split(' ')]
    index = 0
    access = []
    for i in range(M):
        access.append([True for i in range(N)])
        temp = nums[index:index + N]
        nums[index:index + N] = [0]
        nums[index] = temp
        index += 1
    i = j = index = num = 0
    while num < M*N:
        if index == 0:
            while j < N and access[i][j]:
                print(nums[i][j], end=' ')
                access[i][j] = False
                num += 1
                j += 1
            index += 1
            i += 1
            j -= 1
        elif index == 1:
            while i < M and access[i][j]:
                print(nums[i][j], end=' ')
                access[i][j] = False
                num += 1
                i += 1
            index += 1
            j -= 1
            i -= 1
        elif index == 2:
            while j > -1 and access[i][j]:
                print(nums[i][j], end=' ')
                access[i][j] = False
                num += 1
                j -= 1
            index += 1
            i -= 1
            j += 1
        else:
            while access[i][j]:
                print(nums[i][j], end=' ')
                access[i][j] = False
                num += 1
                i -= 1
            index = 0
            j += 1
            i += 1
    print()