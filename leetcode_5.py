#encoding:utf-8 
#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

#根据给出的字符串，找出该字符串中最长的反转对称的子字符串，可以假设字符串最长不超过1000

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        root_str = s
        root_str_list = list(root_str)
        sub_str = temp = ''
        if len(root_str_list) >= 2:
            sub_str = root_str_list[0]
            n = 0
            while n < len(root_str_list) - 1:
                if root_str_list[n + 1] not in sub_str:
                    sub_str += root_str_list[n + 1]
                else:
                	if root_str_list[n + 1] == root_str_list[n]:
                		sub_str += root_str_list[n + 1]
                	else:

                    

                n += 1
            if len(sub_str) > len(temp):
                temp = sub_str
        elif len(root_str_list) == 1:
            temp = root_str_list[0]
        
        return len(temp)