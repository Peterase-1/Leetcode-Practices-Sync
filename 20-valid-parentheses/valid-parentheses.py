class Solution:
    def isValid(self, s):
        stack = []
        
        # Mapping closing -> opening
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0
