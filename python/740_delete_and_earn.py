from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        this question is actually similar to House Robber
        once we select a number, we cannot select adjacent numbers
        
        we can take advantage that there are only 10^4 max integer
        """
        points = [0] * (max(nums) + 1)
        for n in nums:
            points[n] += n
        
        # perfrom house robber algorithm
        prev = 0
        curr = 0
        for n in points:
            max_ = max(prev + n, curr)
            prev = curr
            curr = max_
        
        return curr
            