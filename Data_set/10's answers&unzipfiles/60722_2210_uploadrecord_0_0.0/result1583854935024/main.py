def subset(set,choice,i):
    global allsubset
    if i==1:
        for j in range(len(choice)):
            new_set=set[:]
            new_set.append(choice[j])
            allsubset.append(new_set)
    else:
        for j in range(len(choice)-i+1):
            new_set=set[:]
            new_set.append(choice[j])
            subset(new_set,choice[j+1:],i-1)
T=int(input())
for m in range(T):
    s=input()
    txt=input()
    sset=[]
    tset=[]
    result=[]
    for i in range(len(s)):
        sset.append(s[i])
    for i in range(len(txt)):
        tset.append(txt[i])
    allsubset=[]
    result=[]
    for i in range(len(sset)-len(tset)):
        for j in range(i+len(tset),len(sset)):
            allsubset=[]
            subset([],sset[i:j+1],len(tset))
            if tset in allsubset:
                result.append([i,j])
    length=[]
    for i in range(len(result)):
        length.append(result[i][1]-result[i][0]+1)
    index=length.index(min(length))
    print(s[result[index][0]:result[index][1]+1])
