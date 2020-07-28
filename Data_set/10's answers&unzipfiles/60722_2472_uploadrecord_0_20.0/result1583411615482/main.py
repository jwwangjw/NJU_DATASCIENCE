T=int(input())
for m in range(T):
    N=int(input())
    string=input()
    for i in range(N):
        if string.count(string[i])==1:
            print(string[i])
            break
        elif i==N-1 and string.count(string[i])!=1:
            print(-1)
            break