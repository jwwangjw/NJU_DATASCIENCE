def x(l):
    l.sort(reverse=True)
    for i in range(len(l)-2):
        if l[i+1]+l[i+2]>l[i]:
            print(l[i]+l[i+1]+l[i+2])
            return
    print(0)
if __name__ == '__main__':
    x([int(i) for i in input()[1:-1].split(',')])
