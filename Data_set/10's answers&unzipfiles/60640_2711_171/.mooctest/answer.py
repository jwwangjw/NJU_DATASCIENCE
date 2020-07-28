words=eval(input())
def isvalid(s1,s2):
    count=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1
        if count>2:
            return False
    return True
temp=[]
for word in words:
    if len(temp)==0:
        temp.append([word])
    else:
        flag=False
        for arr in temp:
            for w in arr:
                if isvalid(w,word):
                    flag=True
                    arr.append(word)
                    break
        if flag==False:
            temp.append([word])
print(len(temp))