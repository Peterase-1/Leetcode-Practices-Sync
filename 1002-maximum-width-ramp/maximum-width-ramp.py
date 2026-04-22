class Solution(object):
    def maxWidthRamp(self, nums):
        n = len(nums)
        
        indices = list(range(n))
        indices.sort(key=lambda i: nums[i])
        
        max_width = 0
        min_index = float('inf')
        
        for i in indices:
            if i < min_index:
                min_index = i
            
            width = i - min_index
            if width > max_width:
                max_width = width
        
        return max_width