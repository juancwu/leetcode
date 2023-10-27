class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        1047. Remove All Adjacent Duplicates In String
        https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

        remove adjacent characters if they are the same
        recursively remove until the string has no adjacent duplicates
        Time limit exceeded using recursion
        
        we can use a stack instead
        we compare last one with current one
        if they are the same we pop the last one and skip the current one
        
        at the end we join the characters in the stack
        
        T = O(n)
        S = O(n)
        """
        
        stack = [s[0]]
        for i in range(1,len(s)):
            if len(stack) and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        
        t = ""
        for c in stack:
            t += c
            
        return t