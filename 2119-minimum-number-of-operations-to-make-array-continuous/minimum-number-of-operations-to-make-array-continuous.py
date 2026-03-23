class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        
        nums = sorted(set(nums))
        
        max_window = 0
        left = 0
        
        for right in range(len(nums)):
            
            while nums[right] - nums[left] > n - 1:
                left += 1
            
            window_size = right - left + 1
            max_window = max(max_window, window_size)
        
        return n - max_window