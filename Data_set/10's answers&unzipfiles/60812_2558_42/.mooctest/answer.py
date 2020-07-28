for _ in range(int(input())):
    string = input()
    if(len(string)%2==1):
        print(-1)
        continue
    else:
        counter = 0
        matched = 0
        for j in string:
            if(j in "{"):
                matched+=1
            if(j in "}"):
                matched-=1
            if(matched<0):
                counter+=1
                matched=1
        print(int(matched/2)+counter)
        