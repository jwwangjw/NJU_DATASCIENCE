
 
testCases = int(input().strip())
while testCases > 0:
    testCases -= 1
    l = int(input().strip())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    C = list(map(int, input().strip().split()))
    C = set(C)
    
    totalCount = 0
    for i in range(l):
        if A[i] - B[i] in C:
            totalCount += 1
    print(totalCount)