from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        [1,1,2,2,3,4,4]
        k points to the position we need to place
        i points to the next value
        we move i until we find a unique value
        we store the current k value in a variable, c
        
        [1,1,2,2,3,4,4]
         ^ ^
         c i
         k
         
         because c == nums[i] we continue incrementing i
         [1,1,2,2,3,4,4]
          ^   ^
          c   i
          k
          we found a new value so we set nums[k] = c
          update c = nums[i]
          k += 1
          
          [1,1,2,2,3,4,4]
             ^ ^ ^
             k c i
          c == nums[i], i++
          
          [1,1,2,2,3,4,4]
             ^ ^   ^
             k c   i
             c != nums[i]
             nums[k] = c
             c = nums[i]
             k++
            
          [1,2,2,2,3,4,4]
               ^   ^ ^
               k   c i
          c != nums[i]
          nums[k] = c
          c = nums[i]
          k += 1
          
          [1,2,3,2,3,4,4]
                 ^   ^ ^
                 k   c i
            c == nums[c] => i++
            
            end of loop
            set nums[k] = nums[-1]
            k += 1
            return k
        """
        
        k = 0 # place to insert
        c = nums[k] # current value
        for i in range(1,len(nums)):
            if c != nums[i]:
                nums[k] = c
                c = nums[i]
                k += 1
        
        nums[k] = nums[-1]
        k += 1
        
        return k
        