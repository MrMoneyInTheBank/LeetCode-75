# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hm = {}

        seen = set()

        def dfs(node):
            nonlocal hm
            if node in seen:
                return
            if not node:
                return
            seen.add(node)
            hm[node] = Node(node.val)

            for child in node.neighbors:
                dfs(child)
        dfs(node)

        start = Node(node.val)
        visit = set()

        stack = [start]

        while stack is not None:
            node = stack.pop()
            if node in visit:
                continue
            visit.add(node)
            copy = hm[node]
            copy.neighbors = start.neighbors if start.neighbors != [] else []

            for child in start.neighbours:
                stack.append(child)

        return hm[node]
