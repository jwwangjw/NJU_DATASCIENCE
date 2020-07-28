edges=eval(input())

def exe(chosen,start,end,edge):
    if [start,end] in edge:
        chosen.append([start,end])
        return chosen
    elif [end,start] in edge:
        chosen.append([end,start])
        return chosen
    else:
        for j in edge:
            if j[0]==end:
                chosen.append([j[0],j[1]])
                edge.remove(j)
                return exe(chosen,start,j[1],edge)
            elif j[1]==end:
                chosen.append([j[0],j[1]])
                edge.remove(j)
                return exe(chosen,start,j[0],edge)

judge=False
for i in edges:
    if judge:
        break
    circle=[]
    circle.append(i)
    temp=[]+edges
    temp.remove(i)
    result=exe(circle, i[0], i[1], temp)
    if result!=None:
        for j in range(len(edges)-1,-1,-1):
            if edges[j] in result:
                print(edges[j])
                judge=True
                break