n=int(input())
matrix=[]
for i in range(n):
    string=input().split(",")
    for j in range(len(string)):
        string[j]=int(string[j])
    matrix.append(string)
row,col=len(matrix),len(matrix[0])
dp=[[0]*col for i in range(row)]
dp[-1][-1]=max(1-matrix[-1][-1],1)
for i in range(col-2,-1,-1):
    dp[-1][i]=max(1,dp[-1][i+1]-matrix[-1][i])
for i in range(row-2,-1,-1):
    dp[i][-1]=max(1,dp[i+1][-1]-matrix[i][-1])
for i in range(row-2,-1,-1):
    for j in range(col-2,-1,-1):
        dp[i][j]=max(1,min(dp[i+1][j],dp[i][j+1])-matrix[i][j])
print(dp[0][0])
