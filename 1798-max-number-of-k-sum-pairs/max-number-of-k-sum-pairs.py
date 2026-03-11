class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        operations = 0
        
        while left < right:
            s = nums[left] + nums[right]
            
            if s == k:
                operations += 1
                left += 1
                right -= 1
            elif s < k:
                left += 1
            else:
                right -= 1
        
        return operations
