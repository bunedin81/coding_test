class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        for num in nums:
            if len(str(num))%2 == 0:
                even += 1
        return even
        
#Runtime: 48 ms, faster than 91.44% of Python3 online submissions for Find Numbers with Even Number of Digits.
#Memory Usage: 14.2 MB, less than 89.13% of Python3 online submissions for Find Numbers with Even Number of Digits.        