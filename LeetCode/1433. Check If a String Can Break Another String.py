class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_list = sorted(list(s1))
        s2_list = sorted(list(s2))
        
        bigger = 0
        
        print(s1_list)
        print(s2_list)
        
        for i in range(len(s1_list)):
            if s1_list[i] > s2_list[i]:
                if bigger == 0:
                    bigger = 1
                elif bigger == 2:
                    return False
                
            elif s1_list[i] < s2_list[i]:
                if bigger == 0:
                    bigger = 2
                elif bigger == 1:
                    return False
            else:
                continue
        return True

#Runtime: 176 ms, faster than 47.49% of Python3 online submissions for Check If a String Can Break Another String.
#Memory Usage: 18.1 MB, less than 10.26% of Python3 online submissions for Check If a String Can Break Another String.