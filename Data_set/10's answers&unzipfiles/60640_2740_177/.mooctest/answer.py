def solve():
    src=input()[1:-1].replace('"','').split(',')
    src=list(map(lambda x:x.split(':'),src))
    times=list(map(lambda x:int(x[0])*60+int(x[1]),src))
    res=1400
    def dif(t1,t2):
        middle=720
        result=abs(t1-t2)
        if result>middle:
            result=2*middle-result
        return result
    for i in range(len(times)-1):
        for j in range(i+1,len(times)):
            current=dif(times[i],times[j])
            if current<res:
                res=current
    print(res)

if  __name__ == '__main__' :
    solve()
