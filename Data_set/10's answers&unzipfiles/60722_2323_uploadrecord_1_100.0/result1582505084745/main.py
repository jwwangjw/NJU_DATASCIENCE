A=input().split(",")
k=int(input())
for i in range(len(A)):
    A[i]=int(A[i])
result=0
if len(A)!=1 and max(A)-min(A)>2*k:
    result=abs(max(A)-min(A)-2*k)
print(result)