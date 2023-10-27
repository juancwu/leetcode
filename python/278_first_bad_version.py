# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        1 2 3 4 5 where 4 is bad
        
        
        binary search
        
        n // 2 = 2
        
        2 => false so check 2 .. 5
        (2 + 5) // 2 = 7 // 2 = 3
        
        3 => false so check 3 .. 5
        (3 + 5) // 2 = 4
        
        4 => true return
        
        
        T = O(log n)
        S = O(1)
        
        Runtime: 29ms, faster than 95.60% of python3
        Memory Usage: 13.8 MB, less tahn 63.90% of python3
        """
        
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low