import heapq

class MedianFinder:
    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap
    
    def addNum(self, num: int) -> None:
        # If the current number is bigger than the 
        # smallest number in the max heap, add it to
        # the max heap. Otherwise, add it to the min heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        # if the two heaps vary in length by more than
        # one, then we need to adjust the heaps
        if len(self.small) > len(self.large) + 1:
            number = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, number)
        if len(self.large) > len(self.small) + 1:
            number = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * number)
    
    def findMedian(self) -> float:
        # If small is greater, then top value is the median
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        # if large is greater, then the top value is the median
        elif len(self.large) > len(self.small):
            return self.large[0]
        # if they are both equal, we take the half of both tops
        else:
            return (-1 * self.small[0] + self.large[0]) / 2

# Time | Space : O(log(n)) | O(n)
        
    