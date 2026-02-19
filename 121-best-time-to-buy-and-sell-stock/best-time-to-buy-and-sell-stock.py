class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            
            if profit > max_profit:
                max_profit = profit
            
            if prices[i] < min_price:
                min_price = prices[i]
        
        return max_profit