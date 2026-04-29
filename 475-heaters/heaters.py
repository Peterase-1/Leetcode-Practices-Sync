class Solution(object):
    def findRadius(self, houses, heaters):
        
        houses.sort()
        heaters.sort()
        
        i = 0
        result = 0
        
        for house in houses:
            
            while i < len(heaters) - 1 and abs(heaters[i+1] - house) <= abs(heaters[i] - house):
                i += 1
            
            distance = abs(heaters[i] - house)
            
            result = max(result, distance)
        
        return result