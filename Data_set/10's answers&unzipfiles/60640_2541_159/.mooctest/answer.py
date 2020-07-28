import ast
num = int(input())
courses = ast.literal_eval(input())


def findOrder(numCourses, prerequisites):
    plen = len(prerequisites)
    if plen == 0:  # 没有课程限制，肯定能完成
        return [i for i in range(numCourses)]
    in_degrees = [0 for _ in range(numCourses)]  # 入度：此结点之前的待完成的课程数
    adj = [set() for _ in range(numCourses)]  # 邻接表：此结点之后的课程
    for second, first in prerequisites:
        in_degrees[second] += 1
        adj[first].add(second)

    res = []
    queue = []
    for i in range(numCourses):  # 首先遍历一遍，将入度为0的课程先加入队列
        if in_degrees[i] == 0:
            queue.append(i)

    while queue:
        top = queue.pop(0)
        res.append(top)

        for successor in adj[top]:  # 遍历此课程之后的课程
            in_degrees[successor] -= 1
            if in_degrees[successor] == 0:
                queue.append(successor)
    if len(res) != numCourses:
        return []
    return res

print(findOrder(num, courses))
