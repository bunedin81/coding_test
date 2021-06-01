class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        rtn_val = 0
        
        sorted_nums = sorted(nums)
        
        while len(sorted_nums) > 0:
            max_val = sorted_nums[-1]
            min_val = sorted_nums[0]
            if rtn_val < max_val + min_val:
                rtn_val = max_val + min_val
            print(len(sorted_nums))
            del sorted_nums[len(sorted_nums)-1]
            del sorted_nums[0]
        
        return rtn_val

#Runtime: 4528 ms, faster than 5.20% of Python3 online submissions for Minimize Maximum Pair Sum in Array.
#Memory Usage: 29.8 MB, less than 6.72% of Python3 online submissions for Minimize Maximum Pair Sum in Array.