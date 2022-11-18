class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        a valid sudoku is when all numbers in the same row are unique
        and all numbers in the same col are unique
        as well as all numbers in a 3x3 block are unique
        """
        
        # first iterate through all rows and cols
        for col in range(9):
            val_check = [0] * 10
            for row in range(9):
                # check if all cols have unique values
                if not board[row][col].isdigit():
                    continue
                
                n = int(board[row][col])
                if val_check[n]:
                    return False
                val_check[n] = 1
        
        for row in range(9):
            val_check = [0] * 10
            for col in range(9):
                if not board[row][col].isdigit():
                    continue
                
                n = int(board[row][col])
                if val_check[n]:
                    return False
                val_check[n] = 1
        
        # now check 3x3 block
        for i in range(9):
            row = (i // 3) * 3
            col = (i % 3) * 3
            val_check = [0] * 10
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    if not board[r][c].isdigit():
                        continue
                    
                    n = int(board[r][c])
                    if val_check[n]:
                        return False
                    val_check[n] = 1
        
        return True
                