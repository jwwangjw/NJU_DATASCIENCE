
def set_bits(n, l, r):
    setter = 0
    for i in range(1, r+1):
        if i >= l:
            setter |= 1<<i-1
        else:
            setter |= 0
    #print(bin(setter), bin(n))
    return n | setter
    

T = int(input())

for _ in range(T):
    n, l, r = map(int, input().split())
    ans = set_bits(n, l, r)
    print(ans)