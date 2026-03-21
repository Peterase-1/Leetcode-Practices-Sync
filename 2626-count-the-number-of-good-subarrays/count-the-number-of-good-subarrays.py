class Solution(object):
    def countGood(self, nums, k):
        count = {}
        left = 0
        pairs = 0
        res = 0
        
        for right in range(len(nums)):
            val = nums[right]
            if val in count:
                pairs += count[val]
                count[val] += 1
            else:
                count[val] = 1
            
            while pairs >= k:
                res += len(nums) - right
                count[nums[left]] -= 1
                pairs -= count[nums[left]]
                left += 1
        
        return res