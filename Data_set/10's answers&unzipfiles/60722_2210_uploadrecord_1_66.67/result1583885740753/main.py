T=int(input())
for m in range(T):
    s=input()
    txt=input()
    result=[]
    for i in range(len(s)-len(txt)+1):
        for j in range(i+len(txt)-1,len(s)):
            string=s[i:j+1]
            index=True
            for k in range(len(txt)):
                if not txt[k] in string:
                    index=False
            if index:
                result.append(string)
    length=[]
    for i in range(len(result)):
        length.append(len(result[i]))
    index=length.index(min(length))
    print(result[index])

