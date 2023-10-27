class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
        if r * c > m * n or r * c < m * n:
            return original because it is impossible to reshape
            
        create a new matrix of size r * c
        
        use pointers row and col to keep track of the new matrix
        loop through all the values in the matrix and fill into the new matrix
        """
        m, n = len(mat), len(mat[0])
        new_dim = r * c
        old_dim = m * n
        
        if new_dim > old_dim or new_dim < old_dim:
            return mat
        
        new_mat = [[0 for _ in range(c)] for _ in range(r)]
        row, col = 0, 0
        
        for i in range(m):
            for j in range(n):
                new_mat[row][col] = mat[i][j]
                if col < c - 1:
                    col += 1
                else:
                    col = 0
                    row += 1
        
        return new_mat