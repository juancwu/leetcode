class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """
        two pointers approach with sorted list
        we move the left and right pointer according to
        
        if nums[left] + nums[right] >= k:
            right--
        elif nums[left] + nums[right] < k:
            ans = max(ans, nums[left] + nums[right])
            left++
        """
        nums.sort()
        ans = -1
        left = 0
        right = len(nums) - 1
        
        while left < right:
            s = nums[left] + nums[right]
            if s >= k:
                right -= 1
            else:
                ans = max(ans, s)
                left += 1
        
        return ans