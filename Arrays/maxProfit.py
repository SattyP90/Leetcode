class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """


        maxprofit = 0 #set max profit to 0
        minprice = float('inf') #set min price to a very high number

        for price in prices: #iterate over the prices
            if price < minprice: 
                minprice = price

            else:
                profit = price - minprice #calculate the profit 
                if profit > maxprofit: #check if the new profit is better then the max profit
                    maxprofit = profit

        return maxprofit

            


        