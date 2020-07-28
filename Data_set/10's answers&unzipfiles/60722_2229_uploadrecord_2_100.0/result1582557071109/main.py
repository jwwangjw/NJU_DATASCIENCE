string=input().split(",")
for i in range(len(string)):
    string[i]=int(string[i])
result=True
for i in range(len(string)-2):
    for j in range(i+2,len(string)):
        if string[i]>string[j]:
            result=False
print(result)