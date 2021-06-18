class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        rtn = 0
        
        for i in range(row):
            left = i
            right = (row-1)-i

            rtn += mat[i][left]
            rtn += mat[i][right]
            
            if left == right:
                rtn -= mat[i][left]
                
        return rtn

#Runtime: 100 ms, faster than 95.39% of Python3 online submissions for Matrix Diagonal Sum.
#Memory Usage: 14.5 MB, less than 73.31% of Python3 online submissions for Matrix Diagonal Sum.        