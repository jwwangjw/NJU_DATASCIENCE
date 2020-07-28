s=input().split(" ")
N,M=int(s[0]),int(s[1])
seq=[[] for i in range(N)]
for i in range(M):
    s=input().split(" ")
    a,b=int(s[0]),int(s[1])
    seq[b-1].append(a)
for i in range(3):
    for j in range(N):
        for k in range(1,N+1):
            if k in seq[j]:
                seq[j]+=seq[k-1]
                seq[j]=list(set(seq[j]))
for i in range(N):
    if i+1 in seq[i]:
        seq[i].remove(i+1)
count=0
for i in range(N):
    if len(seq[i])==N-1:
        count+=1
print(count)