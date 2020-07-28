T=int(input())
for i in range(T):
    string1=input()
    string2=input()
    result=[]
    for i in range(len(string1)):
        if not string1[i] in string2:
            result.append(string1[i])
    for i in range(len(string2)):
        if not string2[i] in string1:
            result.append(string2[i])
    print("".join(sorted(list(set(result)))))
    print()
