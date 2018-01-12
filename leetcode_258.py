#encoding:utf-8 
#Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#do it without any loop/recursion in O(1) runtime

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num >= 10:
            sum_up = 0
            while num >= 10:
            	sum_up += num % 10
            	num //= 10
            sum_up += num
            return Solution.addDigits(self, sum_up)
        else:
        	return num