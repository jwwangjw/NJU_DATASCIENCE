w=eval(input())
mask=[0]*len(w)
ans=0
for i in range(len(w)):
    for c in w[i]:
        mask[i]|=1<<(ord(c)-ord('a'))
    for j in range(i):
        if(mask[i]&mask[j]==0):
            ans=max(ans,len(w[i])*len(w[j]))
print(ans)            