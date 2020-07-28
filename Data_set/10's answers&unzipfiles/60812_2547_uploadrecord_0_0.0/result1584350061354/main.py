T = int(input())
for i in range(T):
    N = int(input())
    A = [int(i) for i in input().split(' ')]
    k = int(input())
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            temp = A[i]-A[j]
            if temp == k or temp == -k:
                count += 1
    print(count)