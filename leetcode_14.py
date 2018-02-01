#encoding:utf-8
#Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_control = 1
        result_control = str_control = 0
        result = strs[0] if len(strs) > 0 else ''
        temp = ''
        while strs_control < len(strs):
        	result_control = str_control = 0
        	while str_control < len(strs[strs_control]) and result_control < len(result):
        		if strs[strs_control][str_control] == result[result_control]:
        			temp += strs[strs_control][str_control]
        			str_control += 1
        			result_control += 1
        		else:
        			break
        	result = temp
        	temp = ''
        	strs_control += 1
        	if result == '':
        		break
        return result