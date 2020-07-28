for t in range(int(input())):
    n=int(input())
    arr = [ int(x) for x in input().split()]
    dict = {}
    for a in arr:
        if a in dict.keys():
            dict[a] +=1
        else:
            dict[a] = 1
    
    output = 0        
    for d in dict.keys():
        if dict[d] % 2 == 0:
            output +=dict[d]
        else:
            output+=int(dict[d]/2) * 2
    print(output)
            