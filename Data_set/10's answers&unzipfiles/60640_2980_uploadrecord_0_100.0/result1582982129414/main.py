import re
inp = input()
command = input().split()
if inp.count(command[1]) == 0:
    print("no exist")
    print(inp)
else:
    if command[0] == 'D':
        # 这里只删除最开始出现的指定字母，所以替换次数设置为1
        res = re.sub(command[1], "", inp, 1)
        print(res)
    elif command[0] == 'I':
        rev_str = inp[::-1]
        index = len(inp)-rev_str.index(command[1])-1
        li = list(inp)
        li.insert(index, command[2])
        res = "".join(li)
        print(res)
    elif command[0] == 'R':
        res = re.sub(command[1], command[2], inp)
        print(res)
