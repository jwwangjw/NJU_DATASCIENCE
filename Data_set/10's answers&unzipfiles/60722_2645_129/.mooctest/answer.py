str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
piles=[]
for i in range(len(list1)):
    piles.append(int(list1[i]))
H=int(input())
ans=0
if len(piles) == H:
    ans=max(piles)
else:
    m = sum(piles)//H
    if m == 0:
        ans=1
    else:
        while sum([x//m+(1 if x%m else 0) for x in piles]) > H:
            m += 1
        ans=m
print(ans)
