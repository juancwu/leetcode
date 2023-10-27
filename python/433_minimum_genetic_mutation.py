from collections import deque, defaultdict
from typing import List
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        433. Minimum Genetic Mutation
        https://leetcode.com/problems/minimum-genetic-mutation/
        
        start = AAAAACCC
        end = AACCCCCC
        bank = [AAAACCCC, AAACCCCC, AACCCCCC]
        
        bank stores the valid mutations.
        so start can only mutate to something that is in bank.
        
        there are at max 10 genes in bank so 10 * 8 = 80 characters at most
        there are only four different types of char in a gen so 4 * 8 = 32 characters at most
        
        mutation happens with 1 character of difference
        we can search for the 1 difference neighbour in bank
        when the current gene is the end gene, we are done.
        """
        
        q = deque([(start, 0)])
        visited = defaultdict(int)
        
        while q:
            curr, m = q.popleft()
            if curr == end:
                return m
            for gene in bank:
                valid = sum([1 for i in range(len(gene)) if gene[i] != curr[i]]) == 1
                if valid and gene not in visited:
                    q.append((gene, m + 1))
                    visited[gene] = 1
    
        return -1
    