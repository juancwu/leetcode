class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        treat the matrix as a 1d array
        left = 0
        right = m * n - 1
        
        to get the row col indeces we can use
        mid = left + (right - left) // 2
        row = mid // n
        col = mid % n
        
        where n is the length of each row
        """
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m * n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            row = mid // n
            col = mid % n
            
            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True
        
        return False