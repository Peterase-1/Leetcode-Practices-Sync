class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            strx = str(x)
            revx = strx[::-1]
            intx = int(revx)
        else:
            strx = str(-1 * x)
            revx = strx[::-1]   
            intx = int(revx) * -1

        if intx < -2**31 or intx > 2**31 - 1:
            return 0

        return intx