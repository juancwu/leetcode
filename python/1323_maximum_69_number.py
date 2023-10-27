class Solution:
    def maximum69Number (self, num: int) -> int:
        """
        1323. Maximum 69 Number
        https://leetcode.com/problems/maximum-69-number/
        
        6666 => 9666 would be the biggest
        we only need to check the biggest place if it is 9 or not
        if not we change
        
        we can even take advantage that there are only 6 and 9.
        so for 6 to become 9 we add 3
        for each place the 6 is we add 3 * 10 ^ i
        where i is 0 to place
        
        6666 => 9666
        6666 + x = 9666
        x = 3000 = 3 * 10 ^ 3
        """
        
        n = num
        i = 0
        k = -1
        while n > 0:
            if n % 10 == 6:
                k = i # the biggest place with 6 so far
            i += 1
            n //= 10
        
        if k != -1:
            num += 3 * 10 ** k
        
        return num
        