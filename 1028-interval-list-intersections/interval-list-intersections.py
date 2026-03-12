class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        result = []

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            if start1 <= end2 and start2 <= end1:
                result.append([max(start1, start2), min(end1, end2)])

            if end1 < end2:
                i += 1
            else:
                j += 1

        return result