class Solution:
    def is_vowel(self, c):
        valid = (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u') \
            or (c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U')
        return valid
    
    def reverseVowels(self, s: str) -> str:
        """
        345. Reverse Vowels of a String
        https://leetcode.com/problems/reverse-vowels-of-a-string/
        
        input "aeiou"
        output "uoiea"
        
        a switch with u
        e switch with o
        and i doesnt switch cuz its in the middle
        
        two pointers approach
        
        T = O(n)
        S = O(1)
        
        """
        n = len(s)
        i, j = 0, n - 1
        s_arr = [c for c in s] # we need it in array form cuz in python str is unmutable
        
        while i < j:
            while i < n and not self.is_vowel(s[i]):
                i += 1
            while j > -1 and not self.is_vowel(s[j]):
                j -= 1
            
            # swap
            if i < j:
                s_arr[i], s_arr[j] = s_arr[j], s_arr[i]
                i += 1
                j -= 1
            
        
        
        return "".join(s_arr)