class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        greedy algorithm
        
        we can use two pointers left and right
        where left and right start at the same place
        but the right pointer later becomes the further position
        we can reach at the moment,
        
        as long as right is not at n - 1
        we keep looking for the maximum reach we can do at i index
        """
        
        left, right, jumps, reach = 0, 0, 0, 0
        while right < len(nums) - 1:
            for i in range(left, right + 1):
                reach = max(reach, nums[i] + i) # i are the steps we have taken so far
            
            left = right + 1
            right = reach
            jumps += 1
        
        return jumps