seq=input()
num=0
cur=0
for i in seq:
    if i=="(":
        cur+=1
        num=max(cur,num)
    else:
        cur-=1
an=num//2
result=[0]*len(seq)
for i,element in enumerate(seq):
    if element=="(":
        cur+=1
        if cur>an:
            result[i]=1
    else:
        if cur>an:
            result[i]=1
        cur-=1
print(result)