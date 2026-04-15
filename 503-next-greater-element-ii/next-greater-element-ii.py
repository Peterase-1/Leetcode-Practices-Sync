class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                idx = stack.pop()
                res[idx] = nums[i % n]
            
            if i < n:
                stack.append(i)
        
        return res