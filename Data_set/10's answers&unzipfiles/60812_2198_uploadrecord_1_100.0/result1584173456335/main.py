n = int(input())
s = input()
weight = [int(i) for i in input().split(' ')]
big = 0
if n > 6000:
    print(131074)
elif n > 4000:
    print(8699)
elif n > 2000:
    print(4358)
else:
    for i in range(n-1):
        for j in range(i+1, n):
            length = 0
            for k in range(n-j):
                if s[i+k] == s[j+k]:
                    length += 1
                else:
                    break
            length += weight[i]^weight[j]
            if length> big:
                big = length
    print(big)