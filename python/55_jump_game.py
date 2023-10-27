class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        [2,3,1,1,4]
        we can just keep track to the right boundary
        
        say we start at the end right = n - 1
        
        for i = n - 2 to 0:
            if i + right reaches end:
                new right boundary is i
        
        by the end of the iteration,
        if we reached the right boundary reaches 0 means reach the end else cannot
        """
        right = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= right:
                right = i
        
        return right == 0