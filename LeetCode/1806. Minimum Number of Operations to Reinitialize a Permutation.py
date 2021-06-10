from copy import deepcopy

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        init = deepcopy(perm)
        arr = deepcopy(perm)
        cnt = 0
        
        while True:
            cnt += 1
            for i in range(len(arr)):
                if i%2 == 0:
                    arr[i] = perm[int(i/2)]
                else:
                    arr[i] = perm[int((n+i-1)/2)]
            if init == arr:
                return cnt
            perm = deepcopy(arr)
            
#Runtime: 2420 ms, faster than 5.21% of Python3 online submissions for Minimum Number of Operations to Reinitialize a Permutation.
#Memory Usage: 14.4 MB, less than 36.73% of Python3 online submissions for Minimum Number of Operations to Reinitialize a Permutation.        