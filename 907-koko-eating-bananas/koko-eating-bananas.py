class Solution(object):
    def minEatingSpeed(self, piles, h):
        
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            total_hours = 0
            
            for pile in piles:
                hours = (pile + mid - 1) // mid
                total_hours += hours
            
            if total_hours > h:
                left = mid + 1
            else:
                right = mid
        
        return left