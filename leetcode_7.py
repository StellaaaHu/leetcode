#encoding:utf-8 
#Given a 32-bit signed integer, reverse digits of an integer.
#Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. 
#For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

#给出一个32位int以内的带有符号的整数，倒序输出，数字位数溢出时输出0

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        one_num = x
        if one_num > 0:
        	sign = True
        elif one_num == 0:
        	return 0
        else:
        	sign = False
        	one_num *= -1
        one_num_list = list(str(one_num))
        while one_num_list[-1] == '0':
        	one_num_list.pop()
        tmp = ''.join(one_num_list[::-1])
        result = int(tmp)
        if sign:
        	if result <= 2147483647:
        		return result
        	else:
        		return 0
        else:
        	result *= -1
        	if result >= -2147483648:
        		return result
        	else:
        		return 0