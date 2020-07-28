T = int(input())
for t in range(T):
    N = int(input())
    print(int((1+N)*N/4 + N*(N+1)*(2*N+1)/12))