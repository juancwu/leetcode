class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """
        899. Orderly Queue
        https://leetcode.com/problems/orderly-queue/
        
        examples:
        s = "cba", k = 1
        output should be "acb"
        
        when we can only move one character at a time we are only left with the
        following possible combinations:
        
        "bac", "acb", "cba"
                        ^ this is repeated so it will loop
        from those three we choose the smallest one by lexicographical.
        we only even need to iterate len(s) - 1 times as well
        
        say we have s = "cbaa", k = 1
        possible combinations:
        
        "baac", "aacb", "acba", "cbaa"
                                   ^ loop
        we only iterate len(s) - 1
        and take the smallest one "aacb"
        
        now what if k > 1
        
        say we have s = "baaca", k = 3
        otuput = "aaabc"
        
        iteration steps:
        say we iterate len(s) - 1 times
        i = 0, s = "baaca"
        we of course select the biggest one to go to the back
        "baaca" => "aacab" <- same as i = 3
        
        i = 1, s = "aacab"
        "aacab" => "aaabc" move c cuz its the biggest
        
        i = 2, s = "aaabc"
        "aaabc" => "aabca"
        
        i = 3, s = "aabca"
        "aabca" => "aacab" LOOP! i = 0 is the same!
        
        this is actually just sorting the string
        "baaca" sorted is "aaabc"
        
        there is only lower case english characters
        so there we can sort the string by using
        an array of 26 elements and count the frequency of
        each char in s. then we can assembly the sorted string
        this would be O(n)
        
        when k == 1:
            we need to check every new substring and takes O(n) to build
            we are iterating N - 1 time, so its O(n)
            T = O(n^2)
        
        when k > 1:
            we sort array so its O(n)
        
        worst case: T = O(n^2)
                    S = O(n) where n is the string length
        """
        
        if k == 1:
            min_s = s
            for i in range(1, len(s)):
                min_s = min(min_s, s[i:] + s[:i])
            return min_s
        else:
            alpha = [0] * 26
            for c in s:
                alpha[ord(c) - ord('a')] += 1
            min_s = ""
            for i in range(26):
                min_s += chr(i + ord('a')) * alpha[i]
            return min_s