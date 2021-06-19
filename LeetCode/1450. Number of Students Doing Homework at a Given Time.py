class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        rtn = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                rtn += 1
        return rtn
        
#Runtime: 28 ms, faster than 98.63% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
#Memory Usage: 14.3 MB, less than 19.26% of Python3 online submissions for Number of Students Doing Homework at a Given Time.        