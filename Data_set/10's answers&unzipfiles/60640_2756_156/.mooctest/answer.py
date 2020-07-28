from typing import List
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        from collections import defaultdict

        red_colloction = defaultdict(list)
        blue_collection = defaultdict(list)
        for point in red_edges:
            red_colloction[point[0]].append(point[1])
        for point in blue_edges:
            blue_collection[point[0]].append(point[1])

        red_visit = {0:True}
        blue_visit = {0:True}
        queue = [(0, 0, "red"), (0, 0, "blue")]
        ans = [float("inf") for i in range(n)]
        while queue:
            curr, level, color = queue.pop(0)
            if(color == "red"):
                for point in red_colloction[curr]:
                    if(point not in red_visit):
                        red_visit[point] = True
                        queue.append((point, level+1, "blue"))
                        ans[point] = min(ans[point], level+1)
            else:
                for point in blue_collection[curr]:
                    if(point not in blue_visit):
                        blue_visit[point] = True
                        queue.append((point, level+1, "red"))
                        ans[point] = min(ans[point], level+1)
        ans = [-1 if x==float("inf") else x for x in ans]
        ans[0] = 0
        return ans
n=int(input())
r=eval(input())
b=eval(input())
print(Solution().shortestAlternatingPaths(n,r,b))