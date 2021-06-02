class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        rtn = []
        alpb_dict = {}
        
        for i in s:
            if i not in alpb_dict.keys():
                alpb_dict[i] = 1
            else:
                alpb_dict[i] += 1
        
        temp_list = []
        count = 0
        
        for i in s:
            if i not in temp_list:
                temp_list.append(i)
            alpb_dict[i] -= 1
            count += 1
            
            #check
            list_count = 0
            for k in temp_list:
                if alpb_dict[k] == 0:
                    list_count += 1
                    
            if list_count == len(temp_list):
                rtn.append(count)
                temp_list = []
                count = 0
            
        return rtn

#Runtime: 52 ms, faster than 14.76% of Python3 online submissions for Partition Labels.
#Memory Usage: 14.3 MB, less than 24.23% of Python3 online submissions for Partition Labels.