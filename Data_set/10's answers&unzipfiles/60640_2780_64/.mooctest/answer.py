


testCases = int(input().strip())
while testCases > 0:
    testCases -= 1
    #l, target = (list(map(int, input().strip().split())))
    l = int(input().strip())
    array = list(map(int, input().strip().split()))
    k = int(input().strip())
    mult = 1
    
    for a in array:
        mult *= a
        mult %= k
        if mult == 0:
            break
        
    print(mult)