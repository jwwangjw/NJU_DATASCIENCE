def solve():
    box=eval(input())
    out=eval(input())
    res=[]
    r,c=len(box),len(box[0])

    def bfs():
        nonlocal box
        box1=[[0 for i in range(c)] for j in range(r)]
        for _ in range(c):
            q=[(0,_)]
            while q:
                x,y=q.pop(0)
                if box[x][y]==0:
                    continue
                box1[x][y]=1
                for i,j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    x1, y1 = x + i, y + j
                    if 0 <= x1 < r and 0 <= y1 < c and box1[i][j]!=1:
                        q.append((x1,y1))
        box=box1[:]

    for _out in out:
        box[_out[0]][_out[1]]=0
        total1=sum(map(sum,box))
        bfs()
        total2=sum(map(sum,box))
        res.append(total1-total2)

    print(res)

if  __name__ == '__main__' :
    solve()