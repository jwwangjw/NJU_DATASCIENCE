k=int(input())
for i in range(k):
    n=int(input())
    length=input().split(" ")
    for j in range(n):
        length[j]=int(length[j])
    length.sort()
    length.reverse()
    leng=list(set(length))
    print(len(leng))
    
                  