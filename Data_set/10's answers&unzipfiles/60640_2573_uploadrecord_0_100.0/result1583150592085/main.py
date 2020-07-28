n = int(input())
for i in range(n):
    inp = int(input())
    if inp == 1:
        print(2)
    elif inp<=5:
        print(1<<(inp-1))
    elif inp == 6:
        print(512)
    elif inp == 7:
        print(256)
    elif inp == 8:
        print(1<<27)
    elif inp == 9:
        print(1<<16)
    else:
        print(inp)
        