class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sorted_nums = sorted(nums)
        
        smaller_count = {}
        for i, num in enumerate(sorted_nums):
            if num not in smaller_count:
                smaller_count[num] = i
        
        result = [smaller_count[num] for num in nums]
        return result
            