#encoding:utf-8
#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        origin_str = s
        s_arr = sorted(origin_str)
        temp_arr = []
        if len(origin_str) > 0:
        	n = 1
        	temp_str = s_arr[0]
        	while n < len(s_arr):
        		if  s_arr[n] != s_arr[n - 1]:
        			if temp_str != '':
        				temp_arr.append(temp_str)
        			temp_str = s_arr[n]
        		else:
        			temp_str = ''
        		n += 1
        	if temp_str != '':
        		temp_arr.append(temp_str)
        	if len(temp_arr) > 0:
        		m = 0
        		output_index = len(origin_str)
        		while m < len(temp_arr):
        			arr_index = origin_str.find(temp_arr[m])
        			if arr_index < output_index:
        				output_index = arr_index
        			m += 1
        	else:
        		output_index = -1
        else:
        	output_index = -1
        return output_index
