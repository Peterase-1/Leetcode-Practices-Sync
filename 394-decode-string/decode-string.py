class Solution(object):
    def decodeString(self, s):
        stack = []
        current_string = ""
        k = 0
        
        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
                
            elif char == '[':
                stack.append((current_string, k))
                current_string = ""
                k = 0
                
            elif char == ']':
                prev_string, num = stack.pop()
                current_string = prev_string + num * current_string
                
            else:
                current_string += char
        
        return current_string