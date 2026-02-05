from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sDict = Counter(s)
        for i,ch in enumerate(s):
            if sDict[ch] == 1:
                return i
        return -1