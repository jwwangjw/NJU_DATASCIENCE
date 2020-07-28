def print_tree(num,root,nodes):
    res = [[root]]
    while(num>1):
        temp = []
        for k in res[-1]:
            if k in nodes.keys():
                for j in nodes[k]:
                    if j!=0:
                        temp.append(j)
                        num-=1
        if temp:
            res.append(temp)
    return res
nodes = {}
num,root = map(int,input().split(' '))
for i in range(num):
    k, v1, v2 = map(int,input().split(' '))
    nodes[k] = [v1,v2]
res = print_tree(num,root,nodes)
for i in range(0,len(res)):
    print('Level '+str(i+1)+' : ' + ' '.join([str(k) for k in res[i]]))
for i in range(0,len(res)):
    if i%2==0:
        print('Level '+str(i+1)+' from left to right: ' + ' '.join([str(k) for k in res[i]]))
    else:
        print('Level '+str(i+1)+' from right to left: ' + ' '.join([str(k) for k in res[i][::-1]]))
