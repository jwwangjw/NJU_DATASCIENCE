s1=input()
s2=input()
result=True
for i in range(len(s1)):
    if not s1.count(s1[i])==s2.count(s1[i]):
        result=False
print(result)