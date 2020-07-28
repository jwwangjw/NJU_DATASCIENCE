k=int(input())
for i in range(k):
    n=int(input())
    length=input().split(" ")
    for j in range(n):
        length[j]=int(length[j])
    length.sort()
    length.reverse()
    leng=list(set(length))
    nums=[]
    num=0
    for j in range(len(leng)):
        nums.append(length.count(leng[j]))
    for j in range(len(leng)):
        num+=nums[j]
        if num>=leng[j]:
            print(leng[j])
            break
    
                  