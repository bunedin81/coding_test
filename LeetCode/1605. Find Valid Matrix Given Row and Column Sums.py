class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        rtn_mtx = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]
        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                rtn_mtx[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= rtn_mtx[i][j]
                colSum[j] -= rtn_mtx[i][j]
        
        return rtn_mtx

#Runtime: 1120 ms, faster than 51.10% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.
#Memory Usage: 19.1 MB, less than 63.79% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.