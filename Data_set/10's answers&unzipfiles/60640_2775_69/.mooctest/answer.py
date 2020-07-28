

testCases = int(input().strip())
while testCases > 0:
    testCases -= 1
    #l, target = (list(map(int, input().strip().split())))
    l = int(input().strip())
    if l % 3 == 0:
        l = l // 3
        print(l-1, l, l+1)
    else:
        print(-1)
#    array = list(map(int, input().strip().split()))
  