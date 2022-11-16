class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        a stone can only be removed if and only if it shares
        the same row or col as another stone.
        
        to find the best way to remove all the stones
        we would do a dfs.
        
        we can mark those visited and keep a count of the number of
        stones we can keep.
        
        when we start a dfs it means that any adjacent stone from
        stone[i] starting point will not be kept, and the one remaining
        is the stone[i].
        
        to facilitate the search of adjacent stones we can create an adjacency list
        
        stones removed = n - k where k is the number of stones we can keep.
        """
        n = len(stones)
        
        # create adjacency list
        adj_list = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                a = stones[i]
                b = stones[j]
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        
        k = 0 # stones we can keep
        visited = [0] * n
        stack = []
        
        # start disconnecting stones
        for i in range(n):
            if not visited[i]:
                stack = [i]
                k += 1
                while stack:
                    pos = stack.pop()
                    visited[pos] = 1
                    for adj in adj_list[pos]:
                        if not visited[adj]:
                            stack.append(adj)
        
        return n - k