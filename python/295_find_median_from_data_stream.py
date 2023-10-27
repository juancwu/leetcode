from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        """
        use max-heap to keep lower half
        use min-heap to keep higher half
        when size is odd, the median is top of max-heap
        when size is even, it can be derived from max-heap and min-heap
        """
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if len(self.maxheap) == 0 or -self.maxheap[0] >= num:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -heappop(self.minheap))
        

    def findMedian(self) -> float:
        n = len(self.maxheap) + len(self.minheap)
        if n & 1:
            return -self.maxheap[0]
        
        return (-self.maxheap[0] + self.minheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()