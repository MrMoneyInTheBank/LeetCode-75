import collections
from typing import List 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = {node: False for node in range(n)}
        count = 0

        for node in range(n):
            if seen[node]:
                continue
            else:
                count += 1
                stack = [node]

                while stack != []:
                    curr = stack.pop()
                    if seen[curr]:
                        continue
                    # mark as visited
                    seen[curr] = True
                    for child in graph[curr]:
                        stack.append(child)
        return count
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # not connected, or there must be a cycle        
        if n - 1 != len(edges):
            return False 

        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        components = self.countComponents(n, edges)
        return components == 1



### ALTERNATE

# class Solution:
#     """
#     @param n: An integer
#     @param edges: a list of undirected edges
#     @return: true if it's a valid tree, or false
#     """

#     def validTree(self, n, edges):
#         if not n:
#             return True
#         adj = {i: [] for i in range(n)}
#         for n1, n2 in edges:
#             adj[n1].append(n2)
#             adj[n2].append(n1)

#         visit = set()

#         def dfs(i, prev):
#             if i in visit:
#                 return False

#             visit.add(i)
#             for j in adj[i]:
#                 if j == prev:
#                     continue
#                 if not dfs(j, i):
#                     return False
#             return True

#         return dfs(0, -1) and n == len(visit)
    
    
    
#     # alternative solution via DSU O(ElogV) time complexity and 
#     # save some space as we don't recreate graph\tree into adjacency list prior dfs and loop over the edge list directly
#     class Solution:
#     """
#     @param n: An integer
#     @param edges: a list of undirected edges
#     @return: true if it's a valid tree, or false
#     """
#     def __find(self, n: int) -> int:
#         while n != self.parents.get(n, n):
#             n = self.parents.get(n, n)
#         return n

#     def __connect(self, n: int, m: int) -> None:
#         pn = self.__find(n)
#         pm = self.__find(m)
#         if pn == pm:
#             return
#         if self.heights.get(pn, 1) > self.heights.get(pm, 1):
#             self.parents[pn] = pm
#         else:
#             self.parents[pm] = pn
#             self.heights[pm] = self.heights.get(pn, 1) + 1
#         self.components -= 1

#     def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
#         # init here as not sure that ctor will be re-invoked in different tests
#         self.parents = {}
#         self.heights = {}
#         self.components = n

#         for e1, e2 in edges:
#             if self.__find(e1) == self.__find(e2):  # 'redundant' edge
#                 return False
#             self.__connect(e1, e2)

#         return self.components == 1  # forest contains one tree


