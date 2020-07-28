def solve():
    k,n=map(int,input().split(','))
    res=[]
    def dfs(k,n,path=[]):
        nonlocal res
        if k==1:
            if n>9 or n<=path[len(path)-1]:
                return
            res.append(path+[n])
        else:
            if len(path)==0:
                low=1
            else:
                low=path[len(path)-1]+1
            up=min(n,9)
            for i in range(low,up+1):
                dfs(k-1,n-i,path+[i])
    dfs(k,n,[])
    print(res)

if  __name__ == '__main__' :
    solve()