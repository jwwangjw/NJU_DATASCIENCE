

T = int(input())

for i in range(0,T):
    N = int(input())
    out = 1 + 2*N+ (N*(N-1))/2 + N*(N-1)+(N*(N-1)*(N-2))/2
    print(int(out))