testcases=int(input())
def LCS(x,y,m,n):
    L=[[0]*(n+1) for i in range(m+1)]
    
    for i in range(1,(m+1)):
        for j in range(1,(n+1)):
            if (x[i-1]==y[j-1]):
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    return L[m][n]
    
    
    
for i in range(testcases):
    s=list(input().split(" "))
    s1=s[0]
    s2=s[1]
    t=LCS(s1,s2,len(s1),len(s2))
    print(len(s1)+len(s2)-t)
    
    