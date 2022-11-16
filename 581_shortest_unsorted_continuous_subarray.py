class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        use a stack to keep track of when the left boundary is not sorted
        another stack to keep track of when the right boundary is not sorted
        everything in between those boundaries have to be sorted
        """
        
        stack = [] 
        left = len(nums)
        right = 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                left = min(left, idx)
            stack.append(i)
        
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                right = max(right, idx)
            stack.append(i)
            
        return right - left + 1 if right - left > 0 else 0
                    