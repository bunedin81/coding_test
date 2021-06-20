class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        rtn = []
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    rtn.append(prices[i] - prices[j])
                    break
                if j == len(prices)-1:
                    rtn.append(prices[i])
        rtn.append(prices[-1])
        return rtn
        
#Runtime: 56 ms, faster than 47.59% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
#Memory Usage: 14.5 MB, less than 18.18% of Python3 online submissions for Final Prices With a Special Discount in a Shop.        