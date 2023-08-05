from typing import List

class Interval(object):
	def __init__(self, start: int, end: int) -> None:
		self.start = start
		self.end = end
	
class Solution:
	def minMeetingRooms(self, intervals: List[Interval]) -> int:
		start = sorted([i.start for i in intervals])
		end = sorted([i.end for i in intervals])
		
		res, count = 0, 0
		ptr1, ptr2 = 0, 0
		
		while ptr1 < len(intervals):
			if start[ptr1] < end[ptr2]:
				ptr1 += 1
				count += 1
			else:
				ptr2 += 1
				count -= 1
			res = max(res, count)
		
		return res
