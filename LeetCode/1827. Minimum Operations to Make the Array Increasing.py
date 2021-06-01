class Solution:
    def minOperations(self, nums: List[int]) -> int:
        rtn = 0
        if len(nums) == 0:
            return 0
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                continue
            rtn += ((nums[i-1]+1) - nums[i])
            nums[i] = nums[i-1]+1
        return rtn

#Runtime: 200 ms, faster than 6.99% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
#Memory Usage: 14.9 MB, less than 94.17% of Python3 online submissions for Minimum Operations to Make the Array Increasing.