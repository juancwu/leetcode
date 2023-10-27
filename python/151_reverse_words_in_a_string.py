class Solution:
    def reverserWords_split_join(self, s: str) -> str:
        """
        use built in split function and join the reverse 
        of the split
        """
        s = s.split()
        s = " ".join(reversed(s))
        return s

    def reverseWords_pointers_method(self, s: str) -> str:
        """
        the sky is blue
                      ^
                      i
                      j
        
        the sky is blue
                  ^   ^
                  j   i
        """
        
        i = len(s) - 1
        words = []
        while i > -1:
            if s[i].isalpha() or s[i].isdigit():
                j = i
                while j > -1 and s[j] != ' ':
                    j -= 1
                words.append(s[j + 1:i + 1])
                i = j - 1
            else:
                i -= 1
        
        return " ".join(words)
