a=input()
li=a[1:len(a)-1].split(",")
for i in range(0,len(li)):
    li[i]=int(li[i])
print(sorted(li))