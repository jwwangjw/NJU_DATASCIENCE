string=input().split("=")
if string[0][0]!="-":
    string[0]="+"+string[0]
if string[1][0]!="-":
    string[1]="+"+string[1]
CoefficientLeft=[]
CoefficientRight=[]
numsLeft=[]
numsRight=[]
for i in range(len(string[0])):
    if string[0][i]=="x":
        j=i-1
        while string[0][j]!="+" and string[0][j]!="-":
            j-=1
        if j+1==i:
            CoefficientLeft.append(1)
        else:
            CoefficientLeft.append(int(string[0][j:i]))
    elif string[0][i]>"0" and string[0][i]<"9" and i==len(string[0])-1:
        numsLeft.append(int(string[0][i-1:i+1]))
    elif string[0][i]>"0" and string[0][i]<"9" and string[0][i+1]!="x":
        numsLeft.append(int(string[0][i-1:i+1]))
for i in range(len(string[1])):
    if string[1][i]=="x":
        j=i-1
        while string[1][j]!="+" and string[1][j]!="-":
            j-=1
        if j+1==i:
            CoefficientRight.append(1)
        else:
            CoefficientRight.append(int(string[1][i:j]))
    elif string[1][i]>"0" and string[1][i]<="9" and i==len(string[1])-1:
        numsRight.append(int(string[1][i-1:i+1]))
    elif string[1][i]>"0" and string[1][i]<="9" and string[1][i+1]!="x":
        numsRight.append(int(string[1][i-1:i+1]))
a=sum(CoefficientLeft)-sum(CoefficientRight)
b=sum(numsRight)-sum(numsLeft)
if a==0 and b!=0:
    print("No solution")
elif a==0 and b==0:
    print("Infinite solutions")
else:
    print("x="+str(b//a))