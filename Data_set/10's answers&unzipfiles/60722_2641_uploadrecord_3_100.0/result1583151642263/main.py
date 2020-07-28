s1=input()
s2=input()
result=False
for i in range(len(s2)-len(s1)):
    index=0
    for k in range(len(s1)):
        if not s1.count(s1[k])==s2[i:i+len(s1)].count(s1[k]):
            index=1
    if index==0:
        result=True
print(result)