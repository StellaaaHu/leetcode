#encoding:utf-8
#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > 0:
        	haystack_count = needle_count = 0
        	result = -1
        	while haystack_count < len(haystack):
        		if haystack[haystack_count] == needle[0] and len(needle) <= len(haystack) - haystack_count:
        			temp = result_control = haystack_count
        			while needle_count < len(needle):
        				if needle[needle_count] != haystack[temp]:
        					result_control = -1
        					needle_count = 0
        					break
        				temp += 1
        				needle_count += 1
        			if result_control != -1:
        				result = result_control
        		if result != -1:
        			break
        		haystack_count += 1
        else:
        	result = 0
        return result