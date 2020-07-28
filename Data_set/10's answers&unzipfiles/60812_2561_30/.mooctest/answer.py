




testCases = int(input().strip())
while testCases > 0:
    testCases -= 1
    #l, target = (list(map(int, input().strip().split())))
    n, tgt = (map(int, input().strip().split()))
    
    mat1 = dict()
    mat2 = dict()
    for _ in range(n):
        array = list(map(int, input().strip().split()))
        for a in array:
            mat1[a] = mat1.get(a, 0) + 1
         
    for _ in range(n):
        array = list(map(int, input().strip().split()))
        for a in array:
            mat2[a] = mat2.get(a, 0) + 1
 
    k1 = sorted(mat1.keys())
    k2 = sorted(mat2.keys())
    
    li = 0
    ri = len(k2) - 1
    ct = 0
    
    while li <= len(k1) - 1 and ri >= 0:
        sm = k1[li] + k2[ri]
        if sm == tgt:
            ct += mat1[k1[li]] * mat2[k2[ri]]
            li += 1
            ri -= 1
        elif sm > tgt:
            ri -= 1
        else:
            li += 1
    print(ct)