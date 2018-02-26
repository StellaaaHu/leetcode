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
        vowels_arr = ['a', 'e', 'i', 'o', 'u']
        sort_out_arr = sorted_vowels = []
        for i in range(0, len(s)):
        	if s[i] in vowels_arr:
        		sort_out_arr.append(s[i])
        if len(sort_out_arr) > 0:
        	n = -1
        	while -n <= len(sort_out_arr):
        		sorted_vowels.append(sort_out_arr[n])
        		n -= 1
        	m = 0
        	while m < len(s):
        		if s[m] in vowels_arr:
        			left_s = s[:m]
        			right_s = s[(m + 1):]
        			s = left_s + sorted_vowels[0] + right_s
        			del sorted_vowels[0]
        		m += 1
        return s