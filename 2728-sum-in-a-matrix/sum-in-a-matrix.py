class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        for row in nums:
            row.sort()
        
        score = 0
        cols = len(nums[0])
        
        for col in range(cols):
            max_in_col = 0
            for row in nums:
                max_in_col = max(max_in_col, row[col])
            score += max_in_col
        
        return score