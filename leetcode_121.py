#encoding:utf-8
#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction 
#(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low_point = 10000
        time_stamp = 0
        benefit = 0
        while time_stamp < len(prices) - 1:
        	if prices[time_stamp + 1] > prices[time_stamp]:
        		low_point = prices[time_stamp]
        		for n in range(time_stamp + 1, len(prices)):
        			if prices[n] - low_point > benefit:
        				benefit = prices[n] - low_point
        	time_stamp += 1
        return benefit