T = int(input())
for i in range(T):
    s = input()
    c = sorted(input())
    k = len(c)
    n = len(s)
    num = 0
    for i in range(n-k+1):
        if sorted(s[i:i+k]) == c:
            num += 1
    print(num)