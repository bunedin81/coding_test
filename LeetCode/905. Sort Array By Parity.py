class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        rtn = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                rtn.insert(0, nums[i])
            else:
                rtn.append(nums[i])
        return rtn
    
#Runtime: 88 ms, faster than 24.63% of Python3 online submissions for Sort Array By Parity.
#Memory Usage: 15.1 MB, less than 55.08% of Python3 online submissions for Sort Array By Parity.    