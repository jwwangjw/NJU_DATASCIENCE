def DFS(res,nums,choice,index):
    global allSubs1
    global allSubs2
    if nums==1:
        for i in range(len(choice)):
            result=res+choice[i]
            if index==1:
                allSubs1.append(result)
            else:
                allSubs2.append(result)
    else:
        for i in range(len(choice)-nums+1):
            result=res+choice[i]
            DFS(result,nums-1,choice[i+1:],index)

s1=input()
s2=input()
allSubs1=[]
allSubs2=[]
for i in range(1,len(s1)+1):
    DFS("",i,s1,1)
for i in range(1,len(s2)+1):
    DFS("",i,s2,2)
count=0
new_allSubs1=list(set(allSubs1))
for i in range(len(new_allSubs1)):
    num1=allSubs1.count(new_allSubs1[i])
    num2=allSubs2.count(new_allSubs1[i])
    count+=num1*num2
print(count)

