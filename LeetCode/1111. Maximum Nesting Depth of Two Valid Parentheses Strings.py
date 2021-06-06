class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        a_opener = 0
        b_opener = 0
        ab_list = []
        
        for i in seq:
            if i == '(':
                if a_opener > b_opener:
                    b_opener += 1
                    ab_list.append(1)
                else:
                    a_opener += 1
                    ab_list.append(0)
            else:
                if a_opener > 0:
                    a_opener -= 1
                    ab_list.append(0)
                else:
                    b_opener -= 1
                    ab_list.append(1)
        return ab_list

#Runtime: 104 ms, faster than 5.49% of Python3 online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.
#Memory Usage: 15 MB, less than 40.93% of Python3 online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.        