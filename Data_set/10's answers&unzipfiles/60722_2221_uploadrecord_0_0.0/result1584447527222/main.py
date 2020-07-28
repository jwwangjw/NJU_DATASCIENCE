s=input().split(" ")
N,M=int(s[0]),int(s[1])
seq=[[] for i in range(N)]
for i in range(M):
    s=input().split(" ")
    a,b=int(s[0]),int(s[1])
    seq[b-1].append(a)
for i in range(N):
    for j in range(N):
        for k in range(N):
            if k in seq[j]:
                seq[j]+=seq[k-1]
                seq[j]=list(set(seq[j]))
for i in range(N):
    if i+1 in seq[i]:
        seq[i].remove(i+1)
result=[]
for i in range(N):
    if len(seq[i])==N-1:
        result.append(i+1)
print(" ".join(str(i) for i in result))