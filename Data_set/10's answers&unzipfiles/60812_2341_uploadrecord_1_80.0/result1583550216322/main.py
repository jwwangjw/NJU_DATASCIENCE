T = int(input())
for i in range(T):
    X, Y = [int(i) for i in input().split(' ')]
    A = [int(i) for i in input().split(' ')]
    B = [int(i) for i in input().split(' ')]
    i = j = 0
    while i < X:
        if j < Y:
            if A[i] < B[j]:
                print(A[i], end=' ')
                i += 1
            else:
                print(B[j], end=' ')
                j += 1
        else:
            print(A[i], end=' ')
            i += 1
    while j < Y:
        print(B[j], end=' ')
        j += 1
    print()