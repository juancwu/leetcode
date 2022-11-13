from bisect import insort
class MedianFinder:

    def __init__(self):
        """
        keep input values in a sorted array
        so finding the median would be faster
        """
        self.values = []

    def addNum(self, num: int) -> None:
        insort(self.values, num)

    def findMedian(self) -> float:
        n = len(self.values)
        mid = n >> 1
        median = self.values[mid] if n & 1 else (self.values[mid - 1] + self.values[mid]) / 2
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()