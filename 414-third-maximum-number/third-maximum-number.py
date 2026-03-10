class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        
        nums.sort()
        
        if len(nums) >= 3:
            return nums[-3]
        else:
            return nums[-1]