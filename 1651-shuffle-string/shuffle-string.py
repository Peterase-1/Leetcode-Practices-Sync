class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        shuffled = [''] * len(s)
    
        for i, char in enumerate(s):
            shuffled[indices[i]] = char
        
        return ''.join(shuffled)