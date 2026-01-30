class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in hash map
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store current number and its index
            num_map[num] = i
        
        return []  # No solution found (though problem guarantees one exists)