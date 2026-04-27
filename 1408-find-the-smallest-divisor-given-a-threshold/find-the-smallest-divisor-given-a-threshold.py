import math

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        def compute_sum(divisor):
            total = 0
            for num in nums:
                total += (num + divisor - 1) // divisor
            return total
        
        left = 1
        right = max(nums)

        while left < right:
            mid = (left + right) // 2
            

            if compute_sum(mid) <= threshold:
                right = mid
            else:
                left = mid + 1
        
        return left