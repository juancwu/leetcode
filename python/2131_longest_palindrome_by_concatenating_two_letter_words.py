from collections import defaultdict
from typing import List
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        2131. Longest Palindrome by Concatenating Two Letter Words
        https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
        
        there are only two possible combinations for a word
        either the two letters are the same, palindrome word
        or the two letters are different, non-palindrome word
        
        "xx" -> palindrome  word
            imagine if we have even numbers of such combination
            then we can use them all
            "xx" + "xx" => "xxxx" => palindrome
            
            now, if we have odd number of such combination
            count of "xx" is 3
            we can use count - 1, so 2 making it as above
            or we can use one as middle.
            notice that the middle word as to be a palindrome word
            and there can only be one usage.
        
        "xy" -> non-palindrome word
            the only way this can make it into the final
            palindrome is to have a mirror of this word
            "yx" is the one we are looking for
            
            if we have "xy" = 2 but "yx" = 1,
            it is obvious that we cannot use both "xy"
            so we are taking the min count of both
            we taking 1 each so is 1 + 1 = 2
            math: 2 * x = 2, x = 1 where x is the count
        """
        
        # we first count
        count = defaultdict(int)
        for word in words:
            count[word] += 1

        # now we begin differentiating
        length = 0
        flag = False # we need to know whether there is odd of palindrome word
        for word, n in count.items():
            # palindrome word
            if word[0] == word[1]:
                if n & 1:
                    length += n - 1
                    flag = True
                else:
                    length += n
            elif word[1] > word[0] and word[1] + word[0] in count: # > to not repeat count, "xy" repeats when "yx" if set to !=
                # non-palindrome word
                length += 2 * min(n, count[word[1] + word[0]])
        
        if flag:
            length += 1
        
        return length * 2