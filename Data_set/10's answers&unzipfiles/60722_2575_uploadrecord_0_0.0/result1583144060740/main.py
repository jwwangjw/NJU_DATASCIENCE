seq=input()
num=0
for i in seq:
    if i=="(":
        num+=1
an=num//2
result=[0]*len(seq)
cur=0
for i,element in enumerate(seq):
    if element=="(":
        cur+=1
        if cur>an:
            result[i]=1
    else:
        if cur>an:
            result[i]=1
        cur-=1