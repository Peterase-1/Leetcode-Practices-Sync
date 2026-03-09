class Solution(object):
    def numberOfBoomerangs(self, points):
        total = 0
        
        for i in range(len(points)):
            dist_count = {}
            
            for j in range(len(points)):
                if i == j:
                    continue
                    
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dist = dx*dx + dy*dy
                
                dist_count[dist] = dist_count.get(dist, 0) + 1
            
            for m in dist_count.values():
                total += m * (m - 1)
        
        return total