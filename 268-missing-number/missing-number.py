class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        needed = [i for i in range(n + 1)]

        for value in needed:
            if value not in nums:
                return value

