class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opener = 0
        invalider = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                opener += 1
            elif s[i] == ')':
                if opener > 0:
                    opener -= 1
                else:
                    invalider += 1
        
        return invalider + opener
        
#Runtime: 24 ms, faster than 95.28% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
#Memory Usage: 14.2 MB, less than 39.78% of Python3 online submissions for Minimum Add to Make Parentheses Valid.