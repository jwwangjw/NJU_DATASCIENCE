n, m = [int(i) for i in input().split(' ')]
s = input()
for i in range(m):
    a, b, c, d = [int(j)-1 for j in input().split(' ')]
    match = temp = 0
    for j in range(a, b+1):
        if temp == d-c+1:
            break
        elif s[j] == s[c+temp]:
            temp += 1
        else:
            match = max(match, temp)
            temp = 0
    print(max(match, temp))