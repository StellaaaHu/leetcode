#encoding:utf-8
#Write a function that takes a string as input and returns the string reversed

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = -1
        result_str = ''
        while -n <= len(s):
        	result_str += s[n]
        	n -= 1
        return result_str