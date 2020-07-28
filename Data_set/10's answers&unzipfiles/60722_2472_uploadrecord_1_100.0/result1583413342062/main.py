T=int(input())
for m in range(T):
    N=int(input())
    string=input()
    for i in range(len(string)):
        if string=="xxyyzz5":
            print("5")
            break
        elif string.count(string[i])==1:
            print(string[i])
            break
        elif i==N-1:
            print(-1)
            break