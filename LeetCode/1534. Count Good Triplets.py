class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        
        for i in range(0, len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        count += 1
                        #print(str(arr[i]) + str(arr[j]) + str(arr[k]))
        return count

#Runtime: 664 ms, faster than 65.66% of Python3 online submissions for Count Good Triplets.
#Memory Usage: 14.4 MB, less than 14.21% of Python3 online submissions for Count Good Triplets.