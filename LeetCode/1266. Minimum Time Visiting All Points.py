class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        for i in range(len(points)):
            if i == 0:
                continue
            before = points[i-1]
            curr = points[i]
            
            now_distance = min(abs(before[0]-curr[0]), abs(before[1]-curr[1]))
            left = max(abs(before[0]-curr[0]), abs(before[1]-curr[1])) - now_distance
            
            distance += now_distance + left
            
        return distance
        
#Runtime: 60 ms, faster than 62.14% of Python3 online submissions for Minimum Time Visiting All Points.
#Memory Usage: 14.3 MB, less than 36.16% of Python3 online submissions for Minimum Time Visiting All Points.     