#encoding:utf-8
#Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        count_arr = []
        if a < 0:
        for n in range(0, a):
        	count_arr.append(n)
        n = 0
        for n in range(0, b):
        	count_arr.append(n)
        result = len(count_arr)
        return result