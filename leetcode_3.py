#encoding:utf-8 
#Given a string, find the length of the longest substring without repeating characters.

#根据给出的字符串，找出该字符串中最长的没有重复字母的子字符串的长度

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        root_str = s
        root_str_list = list(root_str)
        sub_str = temp = ''
        if len(root_str_list) >= 2:
        	sub_str = root_str_list[0]
        	n = 0
        	while n < len(root_str_list) - 1:
        		if root_str_list[n + 1] != root_str_list[n] and root_str_list[n + 1] not in sub_str:
        			sub_str += root_str_list[n + 1]
        		else:
        			if len(sub_str) > len(temp):
        				temp = sub_str
        			sub_str = root_str_list[n + 1]
        		n += 1
        elif len(root_str_list) == 1:
        	temp = root_str_list[0]

        if len(sub_str) > len(temp):
        	return len(sub_str)
        else:
        	return len(temp)