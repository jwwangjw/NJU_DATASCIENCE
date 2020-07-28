i = -1
while True:
    i += 1
    a = input().split()
    try:
        j = a.index("1")
        print(abs(2-i)+abs(2-j))
        break
    except ValueError:
        continue
