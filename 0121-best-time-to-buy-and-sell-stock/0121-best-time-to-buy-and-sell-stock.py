class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        min_price=prices[0]
        for i in range(1,len(prices)):
            if(prices[i]<min_price):
                min_price=prices[i]
            else:
                profit=prices[i]-min_price
                max_profit=max(profit,max_profit)
        return max_profit
                    
        