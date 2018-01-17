#encoding:utf-8 
#Given an array of integers, every element appears twice except for one. Find that single one.

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listed_arr = sorted(nums)
        if len(listed_arr) <= 1:
        	result = listed_arr[0]
        else:
        	if listed_arr[0] != listed_arr[1]:
        		result = listed_arr[0]
        	elif listed_arr[-1] != listed_arr[-2]:
        		result = listed_arr[-1]
        	else:
        		n = 1
        		while n < len(listed_arr) - 1:
        			if listed_arr[n] != listed_arr[n - 1]:
        				if listed_arr[n + 1] != listed_arr[n]:
        					result = listed_arr[n]
        			n += 1
        return result