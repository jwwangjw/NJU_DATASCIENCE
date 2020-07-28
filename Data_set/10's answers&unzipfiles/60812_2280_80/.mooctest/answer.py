T=int(input())
for i in range(T):
    n = int(input())
    ans = n
    lst = list(map(int, input().split()))
    for idx, x in enumerate(lst):
        # print('idx: ', idx+ 1, 'x:', x)
        ans = ans ^ x ^ (idx + 1)

        # print(ans)
    # print('idx', idx)    
    # ans ^= n     
    print(ans)    