class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = {}
        
        first_index = {}
        
        last_index = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            count[num] = count.get(num, 0) + 1
            
            if num not in first_index:
                first_index[num] = i
            
            last_index[num] = i
        
        degree = max(count.values())
        
        min_length = len(nums)
        
        for num in count:
            if count[num] == degree:
                length = last_index[num] - first_index[num] + 1
                min_length = min(min_length, length)
        
        return min_length