from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        212. Word Search II
        https://leetcode.com/problems/word-search-ii/
        
        we can use a Trie to make a tree of the words
        
        reason to use a Trie tree is because we are
        searching for a prefix and it is easier to backtrack
        than using a hashmap. However, a typical trie tree
        would be too costly for its operations. 
        so we change it to use a hashmap based trie tree.
        
        we traverse each cell in the board and match words in the
        Trie tree. we recursively check neighbouring cells and check
        if any of the prefixes are present in the Trie tree.
        
        by the end of the algorithm, we should have a list of words
        that are on the board and are in sequence.
        """
        
        self.ret = []
        self.board = board
        self.n = len(board)
        self.m = len(board[0])
        
        # create trie tree
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
                
            # anchor, makes it easy to retrieve word and add to result
            node['$'] = word
        
        for row in range(self.n):
            for col in range(self.m):
                if board[row][col] in trie:
                    self.backtrack(row, col, trie)
        
        return self.ret
    
    def backtrack(self, row, col, root):
        letter = self.board[row][col]
        node = root[letter]
        
        match = node.pop('$', False)
        if match:
            self.ret.append(match)
            
        # add possible solution as visited
        self.board[row][col] = '#'
        
        # explore neighbour cells
        d = [(-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in d:
            if row + dy < 0 or row + dy > self.n - 1 or col + dx < 0 or col + dx > self.m - 1:
                continue
            if self.board[row + dy][col + dx] not in node:
                continue
            self.backtrack(row + dy, col + dx, node)
        
        # remove possible solution
        self.board[row][col] = letter
        
        if not node:
            root.pop(letter)