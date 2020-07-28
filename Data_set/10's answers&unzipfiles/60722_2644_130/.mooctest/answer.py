a=eval(input())
k=int(input())
length=len(a)
mi=length
for i in range(length,0,-1):
    left=0
    while left+i<=length:
        s=sum(a[left:left+i])
        if s>=k:
            mi=i
            break
        i+=1
if sum(a)<k:
    mi=-1
print(mi)