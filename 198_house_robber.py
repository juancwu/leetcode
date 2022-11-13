class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        the robber cannot take from adjacent houses
        this means that the relation is taking the best between
        
        dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        is robbing the next house yield greater profit than the current and next possible house
        
        use recursion with memoization

        """
        self.memo = [-1] * 101 # max number of houses is 100
        self.nums = nums
        return self.decideRob(0)
    
    def decideRob(self, i):
        if i >= len(self.nums):
            return 0
        
        if self.memo[i] != -1:
            return self.memo[i]
        
        self.memo[i] = max(self.decideRob(i + 1), self.decideRob(i + 2) + self.nums[i])
        
        return self.memo[i]