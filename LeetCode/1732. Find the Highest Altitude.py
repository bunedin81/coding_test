class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        gain_sum = 0
        for i in gain:
            gain_sum += i
            if gain_sum > max:
                max = gain_sum
        return max
        
#Runtime: 32 ms, faster than 83.33% of Python3 online submissions for Find the Highest Altitude.
#Memory Usage: 14 MB, less than 97.61% of Python3 online submissions for Find the Highest Altitude.        