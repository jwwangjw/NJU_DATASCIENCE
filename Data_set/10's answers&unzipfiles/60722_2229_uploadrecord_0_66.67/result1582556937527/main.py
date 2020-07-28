string=input().split(",")
result=True
for i in range(len(string)-3):
    for j in range(i+2,len(string)):
        if string[i]>string[j]:
            result=False
print(result)