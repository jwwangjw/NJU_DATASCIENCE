list=input()
i=int(1)
list1=[]
while i<len(list):
    list1.append(list[i])
    i=i+2
a=list1[0]
for m in range(1,len(list1)):
    if a<list1[m]:
        a=list1[m]
    else:
        m=m-1
        break
print(m)
