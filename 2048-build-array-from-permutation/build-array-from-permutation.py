class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        
        for num in nums:
            ans.append(nums[num])

        return ans