from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dictNums = Counter(nums)

        for k,v in dictNums.items():
            if v > (len(nums)//2):
                return k
        return result
        
