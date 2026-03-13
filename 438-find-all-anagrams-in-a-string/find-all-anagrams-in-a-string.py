class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        
        if len(p) > len(s):
            return result
        

        p_count = [0] * 26
        s_count = [0] * 26
        
        for char in p:
            p_count[ord(char) - ord('a')] += 1
        
        for i in range(len(p)):
            s_count[ord(s[i]) - ord('a')] += 1
        
        if s_count == p_count:
            result.append(0)
        
        for i in range(len(p), len(s)):
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            
            s_count[ord(s[i]) - ord('a')] += 1
            
            if s_count == p_count:
                result.append(i - len(p) + 1)
        
        return result