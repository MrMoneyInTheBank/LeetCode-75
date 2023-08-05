from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        starts = [course for course in range(numCourses) if in_degree[course] == 0]
        
        if starts == []:
            return False
        
        # Step 3: Perform BFS
        q = deque(starts)
        visited = set(starts)
        count = numCourses - len(starts)
        
        while q:
            curr_course = q.popleft()
            
            for next_course in graph[curr_course]:
                in_degree[next_course] -= 1
                
                if in_degree[next_course] == 0:
                    if next_course in visited:
                        # Cycle detected
                        return False
                    count -= 1
                    q.append(next_course)
                    visited.add(next_course)
        
        # Step 4: Check if all courses have been visited
        return count == 0
