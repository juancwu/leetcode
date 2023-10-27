class Solution:
    def makeGood(self, s: str) -> str:
        """
        1544. Make The String Great
        https://leetcode.com/problems/make-the-string-great/
        
        l e E e e t c o d e => removes e E
        
        i = 2
        leetcode
        
        "abBAcC"
        i = 2
        aAcC
        
        actually just start from the beginning
        
        ok so KK or kk are valid, only different case is not valid
        
        doing a.isupper() and b.islower() or a.islower() and b.isupper() is good but seems like too much
        
        difference between lower and upper case for assci values
        
        ord('a') - ord('A') = 32
        
        soooooooooo
        
        ord('c') - ord('C') should be 32 as well
        
        
        we can change the above boolean expression to ord(a) - ord(b) == 32
        but ord('A') - ord('a') = -32 so we gotta take the abs
        
        T = O(n^2)
        S = O(1)
        
        use stack?
        so we just need to compare the current element with the top element on stack
        if their abs diff is 32 then we remove the top and continue
        at the end we reassemble the string using what is inside the stack
        
        T = O(n)
        S = O(n)
        """
        stack = [s[0]] # plain old array
        for i in range(1,len(s)):
            if len(stack):
                top = stack[-1]
                if abs(ord(top) - ord(s[i])) == 32:
                    # remove top
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            
        return ''.join(stack)