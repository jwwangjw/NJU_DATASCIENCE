import operator
from filecmp import cmp


def paixu(li):
    for i in range(len(li)):
        for k in range(i + 1, len(li)):
            if (int(li[i]) > int(li[k])):
                a = li[i]
                li[i] = li[k]
                li[k] = a
    return li
def findqh(li):
    ans=[]
    for i in range(len(li) - 1):
        if (li[i] > li[i + 1]):
            ans.append(i+1)
            break
    for i in range(0,len(li)):
        if(li[len(li)-i-1]<li[len(li)-i-2]):
            if(i>len(li)-3):
                ans.append(len(li)-i)
                break
            else:
                ans.append(len(li)-i+1)
            break
    if(len(ans)==1):
        ans.append(0)
    return ans
n=input()
b=input()
c=b.split(' ')
li=list(map(int,c))
c=li.copy()
number=[]
for i in range(len(li)):
    a=0
    for k in range(i+1,len(li)):
        if(int(li[i])>int(li[k])):
            a=li[i]
            li[i]=li[k]
            li[k]=a
ans=findqh(c)
number.append(ans)
r=[]
r1=[]
r2=[]
r=paixu(c[ans[0]-1:ans[1]])
if(ans[0]!=1):
    r1=c[0:ans[0]-1]
    r1.extend(r)
else:
    r1=r.copy()
if(ans[1]!=len(c)):
    r2=c[ans[1]:len(c)]
    r1.extend(r2)
while(operator.eq(li,r1)==False):
    ans=findqh(r1)
    r=[]
    r2=[]
    r3=[]
    number.append(ans)
    r = paixu(li[ans[0] - 1:ans[1] ])
    if (ans[0] != 1):
        r2 = li[0:ans[0]]
        r2.extend(r)
    else:
        r2 = r.copy()
    if (ans[1] != len(c)):
        r3 = li[ans[1]:len(c)]
        r2.extend(r3)
    r1=r2.copy()
print(len(number))
for i in range(0,len(number)):
    print(number[i][0],end=' ')
    print(number[i][1])