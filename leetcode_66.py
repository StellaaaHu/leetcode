#encoding:utf-8
#Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#You may assume the integer do not contain any leading zero, except the number 0 itself.
#The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        m = 0
        while m < len(digits):
        	if digits[m] < 9:
        		n = -1
        		while -n <= len(digits):
        			if digits[n] < 9:
        				digits[n] += 1
        				break
        			else:
        				digits[n] = 0
        			n -= 1
        		break
        	m += 1
        if m == len(digits):
        	for element in range(0, len(digits)):
        		digits[element] = 0
        	add_digits = [1]
        	digits =  add_digits + digits
        return digits