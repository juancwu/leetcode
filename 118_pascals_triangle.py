class Solution:
    def generate(self, n: int) -> List[List[int]]:
        """
        
        """
        
        if n == 1:
            return [[1]]
        if n == 2:
            return [[1],[1,1]]
        
        triangle = [[1],[1,1]]
        for i in range(2, n):
            level = [0] * (i + 1)
            level[0] = 1
            level[-1] = 1
            for j in range(1, i):
                level[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            triangle.append(level)
        
        return triangle
            