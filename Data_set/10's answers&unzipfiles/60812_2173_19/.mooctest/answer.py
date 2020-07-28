for t in range(int(input())):
    N = int(input())
    sum = 0
    for n in range(1, N+1):
        sum = sum + (2*n-1)*(N+1-n)
    print(sum)