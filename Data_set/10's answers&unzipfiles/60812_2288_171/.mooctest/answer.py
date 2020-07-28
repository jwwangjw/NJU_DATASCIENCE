while True:
    try:
        m, n = list(map(int, input().split()))
        seq, cnt = [m], 0
        while seq:
            tmp = seq.pop()
            if tmp <= n:
                cnt += 1
                tmpseq = [tmp * 2, tmp * 2 + 1]
                seq.extend(tmpseq)
        print(cnt)
    except:
        break