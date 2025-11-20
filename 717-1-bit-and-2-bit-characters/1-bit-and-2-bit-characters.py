class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)
        
        while i < n - 1:
            # If current bit is 1, it must be the start of a two-bit character
            if bits[i] == 1:
                i += 2  # Skip next bit (it's part of the two-bit character)
            else:
                i += 1  # Current bit is 0, it's a one-bit character
        
        # If we land exactly at the last position, the last character is one-bit
        return i == n - 1