A=eval(input())
temp=int(input())
result=[]
for i in range(len(A)-1):
    for j in range(i,len(A)):
        s=0
        for k in range(i,j+1):
            s+=A[k]
        if s>=temp:
            result.append(s)
if len(result)==0:
    print(-1)
else:
    print(min(result))