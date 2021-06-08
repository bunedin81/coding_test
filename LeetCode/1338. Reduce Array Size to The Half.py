class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        rtn = 0
        half = len(arr)/2
        
        arr_dic = {}
        for i in arr:
            if i not in arr_dic:
                arr_dic[i] = 1
            else:
                arr_dic[i] += 1
        
        lim_sum = 0
        arr_vals = list(arr_dic.values())
        arr_vals.sort(reverse=True)
        
        for i in range(len(arr_vals)):
            lim_sum += arr_vals[i]
            if lim_sum >= half:
                return i+1

#Runtime: 576 ms, faster than 71.56% of Python3 online submissions for Reduce Array Size to The Half.
#Memory Usage: 31.3 MB, less than 60.12% of Python3 online submissions for Reduce Array Size to The Half.                