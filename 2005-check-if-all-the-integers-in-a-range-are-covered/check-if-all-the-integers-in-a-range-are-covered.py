class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        needed = set(range(left, right + 1))

        for start, end in ranges:
            for x in range(start, end + 1):
                needed.discard(x)

        return len(needed) == 0
            
            
