class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0
        # XOR all characters in both strings
        for char in s:
            result ^= ord(char)
        for char in t:
            result ^= ord(char)
        return chr(result)