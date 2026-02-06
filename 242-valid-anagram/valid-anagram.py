from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        if Counter(s)!=Counter(t):
            return False
        if all(letter in s for letter in t):
            return True
        return False