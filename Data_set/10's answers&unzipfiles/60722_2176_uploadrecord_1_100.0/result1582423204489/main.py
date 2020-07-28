string=input()
suffix=[]
for i in range(len(string)):
    suffix.append(string[i:])
suffix.sort()
result=""
for i in range(len(suffix)):
    result=result+str(len(string)-len(suffix[i])+1)+" "
print(result[:len(result)-1])