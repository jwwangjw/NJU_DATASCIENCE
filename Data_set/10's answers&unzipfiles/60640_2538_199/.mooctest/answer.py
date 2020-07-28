myInput = input()
myOutput = ""
myLen = len(myInput)
myList2=[]

tem=""

for char in range(1,myLen-1):
    tem=tem+myInput[char]

myList = tem.split(",")
myLen = len(myList)

for i in range(0,myLen):
    myList2.append(int(myList[i]))

mmax = 0

while mmax+1 in myList2:
    mmax+=1

mmax+=1

print(mmax)

