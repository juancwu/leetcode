from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        check for case abs(ord(k) - ord(p)) <= 32 totally useless
        
        frequency count
        
        odd count can only be in the middle, and only one can be added if there are multiple
        odd counts
        
        even count can be added at both ends so they fully count
        
        case where odd count are all the same characters
        
        
        """
        
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        middle = False
        length = 0
        for letter, count in freq.items():
            while count > 0:
                if count & 1:
                    middle = True
                    count -= 1
                else:
                    length += 2
                    count -= 2
        
        if middle:
            length += 1
        
        return length