string=input()
IsOrNot=[]
result="YES"
for i in range(len(string)):
    IsOrNot.append(True)
for i in range(len(string)):
    if string[i]==")":
        j=i-1
        while j>=0:
            if string[j]=="(" and IsOrNot[j]==True:
                IsOrNot[j]=False
                break
            j-=1
        if j==-1:
            result="NO"
for i in range(len(string)):
    if string[i]=="(" and IsOrNot[i]==True:
        result="NO"
print(result,end='')