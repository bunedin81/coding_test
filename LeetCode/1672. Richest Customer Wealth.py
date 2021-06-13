class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for account in accounts:
            account_sum = sum(account)
            if account_sum > max:
                max = account_sum
        return max
        

#Runtime: 56 ms, faster than 48.54% of Python3 online submissions for Richest Customer Wealth.
#Memory Usage: 14.3 MB, less than 26.35% of Python3 online submissions for Richest Customer Wealth.