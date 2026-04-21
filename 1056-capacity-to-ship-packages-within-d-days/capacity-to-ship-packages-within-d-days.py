class Solution(object):
    def shipWithinDays(self, weights, days):
        
        def canShip(capacity):
            used_days = 1
            current = 0
            
            for w in weights:
                if current + w > capacity:
                    used_days += 1
                    current = 0
                current += w
            
            return used_days <= days
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            if canShip(mid):
                right = mid 
            else:
                left = mid + 1
        
        return left