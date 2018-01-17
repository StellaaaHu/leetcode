#encoding:utf-8 
#Given a string, find the length of the longest substring without repeating characters.

#根据给出的字符串，找出该字符串中最长的没有重复字母的子字符串的长度

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = end = max_count = 0
        obj = {}
        for i in range(0,len(s)):
        	end += 1
        	obj[s[i]] = obj[s[i]] + 1 if s[i] in obj else 1
        	while obj[s[i]] > 1:
        		obj[s[start]] -= 1
        		start += 1
        	max_count = max(max_count, end - start)
        	i += 1
        return max_count
