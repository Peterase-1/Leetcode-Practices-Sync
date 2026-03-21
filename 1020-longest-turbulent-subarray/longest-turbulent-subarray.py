class Solution(object):
    def maxTurbulenceSize(self, arr):
        if len(arr) == 1:
            return 1
        
        left = 0
        res = 1
        
        for right in range(1, len(arr)):
            if arr[right] == arr[right - 1]:
                left = right
            elif right == 1 or (arr[right] > arr[right - 1]) == (arr[right - 1] > arr[right - 2]):
                left = right - 1
            
            res = max(res, right - left + 1)
        
        return res