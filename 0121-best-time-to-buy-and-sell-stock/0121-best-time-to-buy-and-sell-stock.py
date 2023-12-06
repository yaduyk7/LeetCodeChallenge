class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit_list=[0] #if 'min_price' is getting updated after every loop(i.e the prices list is sorted in decending order, then no profit is possible, in that case 0 has to be returned. And if there is no profit, no element will get appended to 'profit_list'. So, if there is a default zero in 'profit_list', finally when max() is called it will return 0
        min_price=prices[0]
        for i in range(1,len(prices)):
            if(prices[i]<min_price):
                min_price=prices[i]
            else:
                profit=prices[i]-min_price
                profit_list.append(profit)
        return max(profit_list)
                    