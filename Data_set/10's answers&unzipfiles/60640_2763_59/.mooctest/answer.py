t = int(input())
for itr in range(t):
    m,n = map(int,input().split())
    x = []
    for i in range(m+1):
        v = []
        for j in range(n+1):
            if j==0:
                v.append(1)
            else:
                v.append(0)
        x.append(v)
    for i in range(1,m+1):
        for j in range(1,n+1):
            x[i][j] = x[i-1][j]+x[i//2][j-1]
    print(x[m][n])
            