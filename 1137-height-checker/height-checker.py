class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        hs = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if hs[i]!=heights[i]:
                count+=1

        return count