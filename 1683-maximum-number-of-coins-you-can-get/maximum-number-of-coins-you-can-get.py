class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles)
        res = 0
        
        left = 0
        right = n - 1
        
        while left < right:
            right -= 1        
            res += piles[right]
            right -= 1
            left += 1         
        
        return res