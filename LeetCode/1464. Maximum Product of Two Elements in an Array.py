class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max = 0
        second_max = 0
        for num in nums:
            if num > second_max:
                second_max = num
            if second_max > first_max:
                temp = second_max
                second_max = first_max
                first_max = temp
        return (first_max-1)*(second_max-1)
        
#Runtime: 52 ms, faster than 62.86% of Python3 online submissions for Maximum Product of Two Elements in an Array.
#Memory Usage: 14.1 MB, less than 98.09% of Python3 online submissions for Maximum Product of Two Elements in an Array.        