class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        
        n = len(s)
        target = n // 4
        count = Counter(s)
        

        if all(count[c] == target for c in "QWER"):
            return 0
        
        min_len = n
        left = 0

        for right in range(n):
            count[s[right]] -= 1
            
            while left <= right and all(count[c] <= target for c in "QWER"):
                min_len = min(min_len, right - left + 1)
                count[s[left]] += 1
                left += 1
                
        return min_len