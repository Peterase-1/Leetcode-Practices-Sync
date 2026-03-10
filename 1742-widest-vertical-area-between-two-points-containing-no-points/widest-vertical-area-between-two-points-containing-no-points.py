class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        xs = []
        for p in points:
            xs.append(p[0])
        
        xs.sort()
        
        max_width = 0
        for i in range(1, len(xs)):
            width = xs[i] - xs[i-1]
            max_width = max(max_width, width)
        
        return max_width