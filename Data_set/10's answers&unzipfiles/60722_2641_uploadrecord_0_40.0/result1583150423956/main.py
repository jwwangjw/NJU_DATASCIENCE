s1=input()
s2=input()
result=True
for i in range(len(s1)):
    if not s1[i] in s2:
        result=False
print(result)