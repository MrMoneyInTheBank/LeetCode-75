from typing import List
import collections


class Solution:
    def countComponents(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = {node: False for node in graph}
        count = 0

        for node in graph:
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
