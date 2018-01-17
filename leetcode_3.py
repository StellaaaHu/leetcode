#encoding:utf-8 
#Given a string, find the length of the longest substring without repeating characters.

#根据给出的字符串，找出该字符串中最长的没有重复字母的子字符串的长度

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        root_str_list = list(s)
        sub_str = temp = root_str_list[0] if len(root_str_list) > 0 else root_str_list
        n = 1
        while n < len(root_str_list):
            if root_str_list[n] not in sub_str:
                sub_str += root_str_list[n]
            else:
                if len(sub_str) > len(temp):
                    temp = sub_str
                split = sub_str.find(root_str_list[n])
                sub_str = sub_str[(split + 1):]
                sub_str += root_str_list[n]
            n += 1
        if len(sub_str) > len(temp):
            temp = sub_str
        
        return len(temp)