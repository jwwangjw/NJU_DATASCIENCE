def solve():
    def putin(src=[]):
        input()
        source=input().replace('"','')
        while(source[-1:]==','):
            src.append(list(map(int,source[3:-2].split(','))))
            source=input().replace('"','')
        src.append(list(map(int,source[3:-1].split(','))))
        input()

    src=[]
    putin(src)
    x_Board=len(src[0])
    y_Board=len(src)
    res=0

    def point(y,x):
        x1=x
        while(x1<x_Board):
            line(x,x1+1,y)
            x1+=1
            if x1<x_Board:
                if src[y][x1]==0:
                    break
            else:
                break

    def line(x1,x2,y):
        nonlocal res
        s=0
        lines=1
        y+=1
        while(y<y_Board):
            if checkLine(x1,x2,y):
                lines+=1
                y+=1
            else:
                break
        s=(x2-x1)*lines
        if res<s:
            res=s

    def checkLine(x1,x2,y):
        for i in range(x1,x2):
            if src[y][i]==0:
                return False
        return True

    for i in range(y_Board):
        for j in range(x_Board):
            if src[i][j]==1:
                point(i,j)

    print(res)

if  __name__ == '__main__' :
    solve()