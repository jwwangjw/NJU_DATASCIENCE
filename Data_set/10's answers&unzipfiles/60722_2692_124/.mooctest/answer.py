def possible(weight,val,day):
    j=1
    cur=0
    for i in range(len(weight)):
        if cur+weight[i]<=val:
            cur+=weight[i]
        else:
            j+=1
            cur=weight[i]
        if j>D:
            return False
    return True
str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
weights=[]
for i in range(len(list1)):
    weights.append(int(list1[i]))
D=int(input())
l=max(weights)
r=sum(weights)
while l<r:
    m=l+(r-l)//2;
    if possible(weights,m,D):
        r=m
    else:
        l=m+1
print(l)
