"""
我们做BFS，上一层level和下一层level之间的关系为：
把所有上一层level中的每个元素都拿出来，列举出在删除一个括号后的所有可能的情况。
(不管删除以后是否合法），添加到下一个level中的元素。
使用set避免重复
"""


def is_valid(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            cnt -= 1
        if cnt < 0:
            return False  # 出现负值，说明有非法字符
    return cnt == 0


def remover_invalid(s):
    level = {s}
    while True:
        # filter可以筛选出所有合法字符
        valid = list(filter(is_valid, level))
        if valid:
            return valid
        next_level = set()
        for item in level:
            for i in range(len(item)):
                if item[i] in "()":  # 是括号就删除
                    next_level.add(item[:i]+item[i+1:])
        level = next_level


inp = input()
res = remover_invalid(inp)
res.sort()
print(res)
