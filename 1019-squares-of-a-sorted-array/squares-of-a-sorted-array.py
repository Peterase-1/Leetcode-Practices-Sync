class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sqrtNum = [num*num for num in nums]
        sqrtNum.sort()
        return sqrtNum
