from typing import List
import bisect
    
class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> intervals:
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            lastStop = res[-1][-1]
            currStart = intervals[i][0]
            if currStart <= lastStop:
                res[-1] = [res[-1][0], max(res[-1][-1], intervals[i][1])]
            else:
                res.append(intervals[i])
        
        return res
    
    def insertInterval(self, intervals: List[List[int]], interval: List[int]) -> intervals:
        idx = bisect.bisect_left(intervals, newInterval)
        intervals.insert(idx, newInterval)
        intervals = self.mergeIntervals(intervals)
        
        return intervals
