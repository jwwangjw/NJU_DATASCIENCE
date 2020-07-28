
T = int(input().strip())

while T > 0:
    T -= 1
    #st = list(filter(lambda c: c.isalpha(),list(input().strip())))
    #n = int(input().strip())
    st, n = (input().strip().split())
    n = int(n)
    lumpSize = list(map(lambda l: len(l) + 1, st.split("1")))
    #print(lumpSize)
    l = len(lumpSize)
    if n == 0:
        print(sum(list(map(lambda x: x * (x-1) // 2, lumpSize))))
    else:
        totalCount = 0
        for i in range(l - n):
            totalCount += lumpSize[i] * lumpSize[i+n]
        
        print(totalCount)
    