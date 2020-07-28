
for t in range(int(input())):
    n = int(input())
    b = bin(n)
    ones = (1 << len(b)-2)-1
    print(n^ones)