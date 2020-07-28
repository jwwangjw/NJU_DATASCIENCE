res = []
for i in range(int(input())):
    exp=[]
    j = input()
    x = 0
    while x < len(j):
        if j[x] not in '+-/*':
            exp.append(int(j[x]))
        else:
            a = 0
            if j[x] == '+':
                a = exp[-2] + exp[-1]
            if j[x] == '-':
                a = exp[-2] - exp[-1]
            if j[x] == '/':
                a = exp[-2] // exp[-1]
            if j[x] == '*':
                a = exp[-2] * exp[-1]
            del exp[-1]
            del exp[-1]
            exp.append(a)
        x += 1
    res.append(exp[0])
    exp.clear()
for x in res:
    print(x)