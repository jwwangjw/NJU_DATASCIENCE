
#print(allprimes)
testCases = int(input().strip())
while testCases > 0:
    testCases -= 1
    r = int(input().strip())
    area = (2 * r) ** 2
    ct = 0
    for w in range(1, 2 * r, 1):
        h2 = area - w * w
        ct += int(h2 ** 0.5)
    print(ct)