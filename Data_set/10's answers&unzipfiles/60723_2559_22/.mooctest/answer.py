
for _ in range(int(input())):
    s=input()
    flag=0
    for i in s :
        if s.count(i) > 1 :
            print(0)
            flag=1
            break
    if flag!=1 :
        print(1)