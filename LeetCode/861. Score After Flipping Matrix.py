class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        answer = 0
        
        col_len = len(grid[0])
        if col_len == 1 and len(grid) == 1:
            return 1
        
        #Step 1.
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(col_len):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = 1
        #print(grid)
        
        #Step 2.
        col_one_count = [0 for i in range(col_len)]
        for row in grid:
            for i in range(col_len):
                if row[i] == 1:
                    col_one_count[i] += 1         
        #print(col_one_count)
        
        #Step 3.
        if col_len > 1:
            for i in range(1, col_len):
                if len(grid) - col_one_count[i] > col_one_count[i]:
                    col_one_count[i] = len(grid) - col_one_count[i]
        #print(col_one_count)
        
        #Step 4.
        squre = 1
        for i in range(col_len-1, -1, -1):
            answer += squre * col_one_count[i]
            squre *= 2
            
        return answer
                
#Runtime: 52 ms, faster than 12.08% of Python3 online submissions for Score After Flipping Matrix.
#Memory Usage: 14.3 MB, less than 63.75% of Python3 online submissions for Score After Flipping Matrix.