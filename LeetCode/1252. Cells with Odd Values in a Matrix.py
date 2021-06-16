class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        my_list = [[0 for i in range(n)] for j in range(m)]
        
        for indice in indices:
            #indice[0]
            row = indice[0]
            col = indice[1]
            
            copy_indice = my_list[row]
            for i in range(len(copy_indice)):
                copy_indice[i] += 1
                
            for j in my_list:
                j[col] += 1
            
        print(my_list)
        rtn = 0
        for i in my_list:
            for j in i:
                if j%2 == 1:
                    rtn += 1
        return rtn
            
#Runtime: 52 ms, faster than 54.51% of Python3 online submissions for Cells with Odd Values in a Matrix.
#Memory Usage: 14.4 MB, less than 20.13% of Python3 online submissions for Cells with Odd Values in a Matrix.                        