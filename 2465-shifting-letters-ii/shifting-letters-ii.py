class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)
        
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            if end + 1 < n:
                diff[end + 1] -= val
        
        res = []
        curr = 0
        
        for i in range(n):
            curr += diff[i]
            
            shift = curr % 26
            
            new_char = (ord(s[i]) - ord('a') + shift) % 26
            
            res.append(chr(new_char + ord('a')))
        
        return "".join(res)