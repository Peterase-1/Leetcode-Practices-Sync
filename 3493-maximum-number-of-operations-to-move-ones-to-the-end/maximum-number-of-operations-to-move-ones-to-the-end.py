class Solution(object):
    def maxOperations(self, s):
        result = 0
        ones_count = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones_count += 1
            elif i > 0 and s[i-1] == '1':
                result += ones_count
        return result
