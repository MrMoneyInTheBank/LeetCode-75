from typing import List
from math import inf

class Solution:
    def eraseOverlappingIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        count = 0
        lastEnd = -inf
        
        for start, end in intervals:
            if start >= lastEnd:
                lastEnd = end
            else:
                count += 1 
        
        return count
