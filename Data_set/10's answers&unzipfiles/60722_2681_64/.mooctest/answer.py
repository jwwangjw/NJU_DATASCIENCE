for t in range(int(input())):
    b = bin(int(input()))
    print(len(b)-2 + b.count('1') - 1)