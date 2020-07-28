T = int(input().strip())
while T > 0:
    T -= 1
    n = list(input().strip())
    for i,d in enumerate(n):
        if d == '6':
            n[i] = '3'
        else:
            n[i] = '0'
    n = int(''.join(n))
    print(n)
    
    