A=input().split(",")
for i in range(len(A)):
    A[i]=int(A[i])
circum=[]
for i in range(len(A)-2):
    for j in range(i+1,len(A)-1):
        for k in range(j+1,len(A)):
            if A[i]+A[j]>A[k] and A[i]+A[k]>A[j] and A[j]+A[k]>A[i]:
                circum.append(A[i]+A[j]+A[k])
circum.sort()
if len(circum)!=0:
    print(circum[len(circum)-1])
else:
    print(0)