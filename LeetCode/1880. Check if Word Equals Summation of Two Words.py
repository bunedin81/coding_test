class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        fi = get_to_num(firstWord, len(targetWord))
        se = get_to_num(secondWord, len(targetWord))
        th = get_to_num(targetWord, len(targetWord))
        
        if fi + se != th:
            return False
        else:
            return True
    
def get_to_num(stra, n):
    list_temp = []
    for i in range(len(stra)):
        list_temp.append(str(ord(stra[i]) - 97))
    return int(''.join(list_temp))

#Runtime: 40 ms, faster than 44.55% of Python3 online submissions for Check if Word Equals Summation of Two Words.
#Memory Usage: 14.2 MB, less than 83.27% of Python3 online submissions for Check if Word Equals Summation of Two Words.