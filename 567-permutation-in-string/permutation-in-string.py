class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        for ch in s1:
            if ch in s1_count:
                s1_count[ch] += 1
            else:
                s1_count[ch] = 1
        
        for i in range(len(s2) - len(s1) + 1):
            window_count = {}
            for j in range(i, i + len(s1)):
                ch = s2[j]
                if ch in window_count:
                    window_count[ch] += 1
                else:
                    window_count[ch] = 1
            
            if window_count == s1_count:
                return True
        
        return False