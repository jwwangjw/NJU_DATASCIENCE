twoString=input()
threeString=input()
ten_two=[]
ten_three=[]
for i in range(len(twoString)):
    for j in range(2):
        newString=twoString[:i]+str(j)+twoString[i+1:]
        ten_two.append(int(newString,2))
    ten_two.remove(int(twoString[:i]+twoString[i]+twoString[i+1:],2))
for i in range(len(threeString)):
    for j in range(3):
        newString=threeString[:i]+str(j)+threeString[i+1:]
        ten_three.append(int(newString,3))
    ten_three.remove(int(threeString[:i]+threeString[i]+threeString[i+1:],3))
for i in range(len(ten_two)):
    if ten_two[i] in ten_three:
        print(ten_two[i],end='')