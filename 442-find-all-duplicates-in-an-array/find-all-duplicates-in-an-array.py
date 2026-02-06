from collections import Counter
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        frqNums = Counter(nums)
        for k,v in frqNums.items():
            if v>=2:
                ans.append(k)

        return ans