class Solution(object):
    def numberOfSubarrays(self, nums, k):
        from collections import defaultdict

        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        odd_count = 0
        result = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            result += prefix_count[odd_count - k]
            prefix_count[odd_count] += 1

        return result