while True:
    try:
        n=int(input().strip())
        #print(n)
        inp=list(map(int,input().strip().split(' ')))
        #print(inp)
        result=0
        while len(inp)!=1:
            inp=sorted(inp)
            one=inp.pop(0)
            two=inp.pop(0)
            re=one+two
            inp.append(re)
            result+=re
        print(result)
    except:
        break
