class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        n = len(s)
        
        for i in range(0, n, 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)