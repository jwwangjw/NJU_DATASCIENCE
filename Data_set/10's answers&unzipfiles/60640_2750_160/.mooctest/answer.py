from typing import List
class Solution:
    def findMinHeightTrees(self, n: 'int',edges: 'List[List[int]]') -> 'List[int]':
        if n == 1: return [0]
        paths = [set() for _ in range(n)]
        for node1, node2 in edges:
            paths[node1].add(node2)
            paths[node2].add(node1)
        leaves = [node for node in range(n) if len(paths[node]) == 1]
        roots = n
        while roots > 2:
            roots -= len(leaves)
            newleaves = []
            for node in leaves:
                parent = paths[node].pop()
                paths[parent].remove(node)
                if len(paths[parent]) == 1: newleaves.append(parent)
            leaves = newleaves
        return leaves
n=int(input())
ed=eval(input())
print(Solution().findMinHeightTrees(n,ed))