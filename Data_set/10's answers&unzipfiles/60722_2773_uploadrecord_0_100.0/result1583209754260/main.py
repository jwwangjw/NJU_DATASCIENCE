l=input()
one=input()
one=eval(one[2:len(one)-1])
matrix=[one]
for i in range(1,len(one)-1):
    row=input()
    row=eval(row[2:len(row)-1])
    matrix.append(row)
row=input()
row=eval(row[2:len(row)])
matrix.append(row)
r=input()
row,col=len(matrix),len(matrix[0])
result=0
memo=[[0]*col for i in range(row)]

def DFS(i,j):
    if memo[i][j]!=0:
        return memo[i][j]
    temp=1
    for x,y in [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]:
        if 0<=x<row and 0<=y<col and matrix[x][y]>matrix[i][j]:
            temp=max(temp,1+DFS(x,y))
    memo[i][j]=temp
    return temp

for i in range(row):
    for j in range(col):
        DFS(i,j)
for i in range(row):
    result=max(result,max(memo[i]))
print(result)
