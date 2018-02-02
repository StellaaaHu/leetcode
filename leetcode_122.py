#encoding:utf-8
#Say you have an array for which the ith element is the price of a given stock on day i.
#Design an algorithm to find the maximum profit. You may complete as many transactions as you like
#(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time 
#(ie, you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low_price = prices[0] if len(prices) > 0 else 0
        benefit = 0
        for n in range(0, len(prices) - 1):
        	if prices[n + 1] < prices[n]:
        		benefit += prices[n] - low_price
        		low_price = prices[n + 1]
        if len(prices) > 0:
        	if prices[-1] > low_price:
        		benefit += prices[-1] - low_price
        return benefit