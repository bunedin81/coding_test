class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rtn = 0
        
        for i in range(row):
            if grid[i][0] < 0:
                rtn += col
                continue
            for j in range((col-1), -1, -1):
                if grid[i][j] >= 0:
                    break
                else:
                    rtn += 1
        return rtn
    
#Runtime: 124 ms, faster than 40.60% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
#Memory Usage: 15.2 MB, less than 45.07% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.    