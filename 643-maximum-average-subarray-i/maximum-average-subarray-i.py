class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        winsum = float(sum(nums[:k]))
        maxsum = winsum
        
        for i in range(k, len(nums)):
            winsum = winsum - nums[i - k] + nums[i]
            maxsum = max(maxsum, winsum)
        
        return maxsum / k