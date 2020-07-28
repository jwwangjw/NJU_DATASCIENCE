tc=int(input())
for _ in range(tc):
    s= input()
    count=1
    temp=0
    stac=[]
    for i in range(len(s)):
        if(s[i]=='('):
            stac.append(count)
            print(count, end=' ')
            count+=1
            
        elif(s[i]==')'):
            x= stac[-1]
            print(x, end=' ')
            stac.pop(-1)

    print()
        