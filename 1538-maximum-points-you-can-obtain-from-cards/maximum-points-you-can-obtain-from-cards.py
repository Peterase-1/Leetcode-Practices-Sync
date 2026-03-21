class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        
        if k == n:
            return sum(cardPoints)
        
        total = sum(cardPoints)
        window_size = n - k
        
        curr_sum = sum(cardPoints[:window_size])
        min_sum = curr_sum
        
        for i in range(window_size, n):
            curr_sum += cardPoints[i]
            curr_sum -= cardPoints[i - window_size]
            min_sum = min(min_sum, curr_sum)
        
        return total - min_sum