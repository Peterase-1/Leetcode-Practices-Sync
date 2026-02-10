class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        result = []
        for num in nums:
            if num != 0:
                result.append(num)
        zeros_count = n - len(result)
        result.extend([0] * zeros_count)
        return result
