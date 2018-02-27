#encoding:utf-8
#Write a function that takes a string as input and reverse only the vowels of a string.
#Example 1:
#Given s = "hello", return "holle".
#Example 2:
#Given s = "leetcode", return "leotcede".

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sort_out_arr = []
        new_str = ''
        for i in range(0, len(s)):
        	if s[i] in vowels_arr:
        		sort_out_arr.append(s[i])
        if len(sort_out_arr) > 0:
        	m = 0
        	while m < len(s):
        		if s[m] not in vowels_arr:
        			new_str += s[m]
        		else:
        			new_str += sort_out_arr[-1]
        			del sort_out_arr[-1]
        		m += 1
        	return new_str
        else:
        	return s