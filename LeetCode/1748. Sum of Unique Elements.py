class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        diction = {}
        rtn = 0
        for num in nums:
            if num not in diction.keys():
                diction[num] = 1
            else:
                diction[num] += 1
        for key, value in diction.items():
            if value == 1:
                rtn += key
        return rtn
                
#Runtime: 32 ms, faster than 81.79% of Python3 online submissions for Sum of Unique Elements.
#Memory Usage: 14.1 MB, less than 89.14% of Python3 online submissions for Sum of Unique Elements.        