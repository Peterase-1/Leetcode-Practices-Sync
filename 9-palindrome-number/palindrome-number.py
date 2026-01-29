class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        revStr = str(x)
        revStr = revStr[::-1]

         

        if (x>=0 and str(x)==revStr):
            return True

        else:
            return False