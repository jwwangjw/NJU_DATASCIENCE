T = int(input())
for i in range(T):
    N = int(input())
    A = [int(i) for i in input().split(' ')]
    k = int(input())
    nums = set()
    for i in range(N-1):
        for j in range(i+1, N):
            temp = A[i]-A[j]
            if temp == k:
                nums.add(A[i])
            elif temp == -k:
                nums.add(A[j])
    print(len(nums))