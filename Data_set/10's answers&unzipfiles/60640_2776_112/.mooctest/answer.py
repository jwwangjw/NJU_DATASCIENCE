words=eval(input())
st={}
ans=[]
for w in words:
    st[w]=True
for word in words:
    n=len(word)
    dp=[False]*(n+1)
    dp[0]=True
    for i in range(n):
        if(not dp[i]):
            continue
        for j in range(i+1,n+1):
            if(j-i<n and word[i:j] in st):
                dp[j]=True
        if(dp[n]):
            ans.append(word)
            break
print(ans)