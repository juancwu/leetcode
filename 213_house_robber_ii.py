from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        if first and last house are connected,
        it means that the range is now 0 to n - 2
        and 1 to n -1
        
        we just gotta find out the best out of all of them
        """
        if len(nums) == 1:
            return nums[0]
        
        self.nums = nums
        
        return max(self.calculate(0, len(nums) - 2), self.calculate(1, len(nums) - 1))
    
    def calculate(self, l, r):
        n = len(self.nums)
        rob_next = 0
        rob_next_next = 0
        
        for i in range(l, r + 1):
            curr = max(rob_next, rob_next_next + self.nums[i])
            rob_next_next = rob_next
            rob_next = curr
        
        return rob_next
        