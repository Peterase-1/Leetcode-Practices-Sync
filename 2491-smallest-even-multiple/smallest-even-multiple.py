import math
class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_num = max(2, n)

        while True:
            if max_num % 2 == 0 and max_num % n == 0:
                return max_num
                break
            max_num += 1
        