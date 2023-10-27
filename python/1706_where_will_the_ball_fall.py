from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        """
        1706. Where Will the Ball Fall
        https://leetcode.com/problems/where-will-the-ball-fall/
        
        #  1706. Where Will the Ball Fall
        ### Example grid:
        ```
         1  1  1 -1 -1 
         1  1  1 -1 -1 
        -1 -1 -1  1  1 
         1  1  1  1 -1 
        -1 -1 -1 -1 -1 
        ```

        ### Intuition
        valid path is only when` i - 1` or `i + 1` are equals to i
        this is cuz when opposite direction meet, it creates a cross
        that blocks the path.

        when falling in `\` direction, should check` i + 1`
        boundary, cannot fall when `i + 1 >= len(grid[col]) `
        because the ball would meet right wall

        when falling in `/` direction, should check `i - 1`
        boundary, cannot fall when` i - 1 < 0 `
        because the ball would meet left wall and get stuck

        each iteration we move diagonally depending
        in the direction the ball falls.
        so `\` should fall to an adjacent `\` as well to make `\ \`
        same for `/ /`

        observation:
        if `n1 = 0, n2 = n1 + grid[m][n1], m = 0`
        using above example:
        ```
        grid[m][n1] = 1
        n2 = n1 + grid[m][n1] = 1 + 1 = 2
        grid[m][n2] = 1
        grid[m][n1] == grid[m][n1]
        valid path
        ```

        time complexity: O(m*n)
        space complexity: O(n)
        """
        
        ret = []
        
        # a little different from other 2d array traversals
        # this time will go col then row
        for ball_i in range(len(grid[0])):
            col_1 = ball_i
            for row in range(len(grid)):
                # determine the if the adjacent cell
                # can make a valid path with current cell
                col_2 = col_1 + grid[row][col_1]
                
                # check for boundaries
                if col_2 < 0 or col_2 >= len(grid[0]) or grid[row][col_1] != grid[row][col_2]:
                    col_1 = -1
                    break;
                col_1 = col_2 # moving to next cell
            ret.append(col_1)
        
        return ret