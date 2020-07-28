def y(m):
    
    import collections
    r,c=len(m),len(m[0])
    data=collections.defaultdict(list)
    for i in range(r):
        for j in range(c):
            data[i-j].append(m[i][j])
    for i in data:
        data[i].sort()
    for i in range(r):
        for j in range(c):
            m[i][j]=data[i-j].pop(0)
    print(m)

if __name__ == '__main__':
    y([[int(k) for k in i.split(',')] for i in [j for j in input()[2:-2].split('],[')]])
