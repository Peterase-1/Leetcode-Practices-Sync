class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        left = 0
        pairs = 0
        max_length = 1
        
        for right in range(1, len(s)):
            
            if s[right] == s[right - 1]:
                pairs += 1
            
            while pairs > 1:
                if s[left] == s[left + 1]:
                    pairs -= 1
                left += 1
            
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        
        return max_length