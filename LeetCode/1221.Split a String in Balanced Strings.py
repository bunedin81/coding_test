class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_stack = 0
        l_stack = 0
        rtn = 0
        
        for i in range(len(s)):
            if s[i] == 'L':
                l_stack += 1
            elif s[i] == 'R':
                r_stack += 1
            if l_stack == r_stack and (l_stack != 0 or r_stack != 0):
                rtn += 1
                l_stack = 0
                r_stack = 0
        
        return rtn

#Runtime: 28 ms, faster than 81.66% of Python3 online submissions for Split a String in Balanced Strings.
#Memory Usage: 14.2 MB, less than 39.87% of Python3 online submissions for Split a String in Balanced Strings.        