#encoding:utf-8
#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#If the last word does not exist, return 0

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = -1
        result_len = 0
        while -n <= len(s):
        	if s[-1] == ' ':
        		s = s[:-1]
        	else:
        		if s[n] != ' ':
        			result_len += 1
        		else:
        			break
        		n -= 1
        return result_len