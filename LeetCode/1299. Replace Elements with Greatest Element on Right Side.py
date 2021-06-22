class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp_max = 0
        rtn = []
        for i in range(len(arr)-1):
            temp_max = max(arr[i+1:])
            rtn.append(temp_max)
        
        rtn.append(-1)
        return rtn
    
#Runtime: 3932 ms, faster than 31.20% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
#Memory Usage: 15.4 MB, less than 35.98% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.    