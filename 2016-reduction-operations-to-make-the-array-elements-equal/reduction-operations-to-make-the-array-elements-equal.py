class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        operations = 0
        distinct_levels = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                distinct_levels += 1
            operations += distinct_levels
        
        return operations