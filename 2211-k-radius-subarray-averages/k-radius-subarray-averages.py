class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        result = [-1] * n
        
        window_size = 2 * k + 1
        
        if window_size > n:
            return result
        
        window_sum = sum(nums[:window_size])
        
        for i in range(k, n - k):
            result[i] = window_sum // window_size
            
            if i + k + 1 < n:
                window_sum += nums[i + k + 1] 
                window_sum -= nums[i - k]     
        
        return result