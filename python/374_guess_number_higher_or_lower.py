# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        binary search method
        pick middle number and decrase or increase accordingly
        if n is 33, correct number is 14
        
        low = 1
        high = 33
        mid = (1 + 33) // 2 = 17
        
        guess => -1 (17 > 14)
        high = 17
        low = 1
        mid = (1 + 17) // 2 = 9
        
        guess => 1
        low = 9
        high = 17
        mid = (9 + 17) // 2 = 13
        
        guess => 1
        low = 13
        high = 17
        mid = (13 + 17) // 2 = 15
        
        guess => -1
        high = 15
        low = 13
        mid = (13 + 15) // => 14
        
        guess => 0
        found number! 
        """
        
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            my_guess = guess(mid)
            if my_guess == -1:
                high = mid - 1
            elif my_guess == 1:
                low = mid + 1
            else:
                return mid
        
        return low
        
        
        
        