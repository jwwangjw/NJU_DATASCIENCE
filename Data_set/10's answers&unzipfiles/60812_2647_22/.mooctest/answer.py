
for i in range (int(input())):
    n=int(input())
    bi=str(bin(n)[2:])
    b=list(bi)
    print(b.count('1'))