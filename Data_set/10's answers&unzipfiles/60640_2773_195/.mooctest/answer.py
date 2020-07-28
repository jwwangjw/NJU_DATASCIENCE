from sys import stdin
'''
mtrx=stdin.readlines()
mtrx.pop()
mtrx.pop(0)
for i in range(len(mtrx)-1):
    mtrx[i]=eval(mtrx[i][:-2].strip())
mtrx[-1]=eval(mtrx[-1][:-1].strip())
'''
mtrx=[[9,9,4],[6,6,8],[2,1,1]]
m = len(mtrx)
n = len(mtrx[0])
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
memorized=[]
for i in range(m):
    memorized.append([0]*n)
#使用了记忆化方法 注意 不能用[[0]*n]*m 因为这样会使每行持有相同引用 对一个单元的修改会影响到每一行


def longest_path():
    global m
    global n
    if len(mtrx)==0:
        return 0
    ans=0
    for i in range(m):
        for j in range(n):
            ans=max(ans,dfs(i,j))
    return ans


def dfs(i,j):
    if memorized[i][j] != 0:
        return memorized[i][j]
    for d in directions:
        x=i+d[0]
        y=j+d[1]
        if 0 <= x < m and 0 <= y < n and mtrx[x][y]>mtrx[i][j]:
            memorized[i][j] = max(memorized[i][j], dfs(x, y))
    memorized[i][j]=memorized[i][j]+1
    return memorized[i][j]


print(longest_path())