A=input().split(",")
for i in range(len(A)):
    A[i]=int(A[i])
A.sort()
k=int(input())
differ=[]
for i in range(len(A)-1):
    differ.append(max(A[i]+k,A[len(A)-1]-k)-min(A[0]+k,A[i+1]-k))
differ.sort()
print(differ[0])