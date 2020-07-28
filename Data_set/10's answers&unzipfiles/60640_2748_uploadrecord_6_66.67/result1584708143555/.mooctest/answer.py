def solve():
    src=input()
    left,right=0,0
    res=[]

    def numOflr(s):
        nonlocal left,right
        for _s in s:
            if _s=='(':
                left+=1
            elif _s==')':
                if left==0:
                    right+=1
                else:
                    left-=1

    def dfs(src,start,left,right):
        nonlocal res
        if left==0 and right==0 and isValid(src):
            res.append(src)
            return
        for i in range(start,len(src)):
            if i!=start and src[i]==src[i-1]:
                continue
            if src[i]=='(' and left>0:
                current=src[0:i]+src[i+1:]
                dfs(current,i,left-1,right)
            if src[i]==')' and right>0:
                current=src[0:i]+src[i+1:]
                dfs(current,i,left,right-1)

    def isValid(src):
        left,right=0,0
        for s in src:
            if s=='(':
                left+=1
            elif s==')':
                if left==0:
                    return False
                else:
                    left-=1
        if left!=0:
            return False
        return True

    numOflr(src)
    dfs(src,0,left,right)
    if len(res)>1:
        temp=res[0]
        res[0]=res[1]
        res[1]=temp
    print(res)

if  __name__ == '__main__' :
    solve()