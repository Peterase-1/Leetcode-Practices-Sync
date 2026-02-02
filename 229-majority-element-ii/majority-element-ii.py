from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dictNums = Counter(nums)
        result = []

        for k,v in dictNums.items():
            if v > (len(nums)//3):
                result.append(k)
        return result
        