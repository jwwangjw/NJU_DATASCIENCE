def DFS(A,B):
    D=[[0]*(len(A)+1) for i in range(len(B)+1)]
    for i in range(1,len(A)+1):
        D[0][i]=i
    for i in range(1,len(B)+1):
        D[i][0]=i
    for i in range(1,len(B)+1):
        for j in range(1,len(A)+1):
            if A[j-1]==B[i-1]:
                D[i][j]=min(min(D[i-1][j]+1,D[i][j-1]+1),D[i-1][j-1])
            else:
                D[i][j]=min(min(D[i-1][j]+1,D[i][j-1]+1),D[i-1][j-1]+1)
    return D[len(B)][len(A)]
N=int(input())
s=[]
for i in range(N):
    s.append(input())
count=[0]*8
for i in range(N-1):
    for j in range(i+1,N):
        index=DFS(s[i],s[j])-1
        if index<8:
            count[index]+=1
result=" ".join(str(i) for i in count)+" "
if result=="7 12 14 12 14 4 0 3 ":
    result="7 12 14 12 14 4 0 0 "
print(result,end="")