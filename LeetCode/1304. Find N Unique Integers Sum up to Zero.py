class Solution:
    def sumZero(self, n: int) -> List[int]:
        rtn = []
        isOdd = False if n%2 == 0 else True
        
        if isOdd:
            rtn.append(0)
        for i in range(1, int(n/2)+1):
            rtn.append(i)
            rtn.append(i*-1)
        return rtn
        
#Runtime: 32 ms, faster than 80.32% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
#Memory Usage: 14.4 MB, less than 15.23% of Python3 online submissions for Find N Unique Integers Sum up to Zero.        