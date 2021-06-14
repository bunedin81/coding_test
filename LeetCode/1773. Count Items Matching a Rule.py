class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        col = 0
        count = 0
        if ruleKey == "type":
            col = 0
        elif ruleKey == "color":
            col = 1
        elif ruleKey == "name":
            col = 2
        
        for item in items:
            if item[col] == ruleValue:
                count+= 1
                
        return count

#Runtime: 240 ms, faster than 71.92% of Python3 online submissions for Count Items Matching a Rule.
#Memory Usage: 20.6 MB, less than 20.10% of Python3 online submissions for Count Items Matching a Rule.