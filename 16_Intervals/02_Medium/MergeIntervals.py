from typing import List
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            lastEnd = res[-1][-1]
            currStart = intervals[i][0]
            if currStart <= lastEnd:
                res[-1] = [res[-1][0], max(res[-1][-1], intervals[i][1])]
            else:
                res.append(intervals[i])
        
        return res
